# Level 6 -> Level 7

Input secret: [      ]
Submit Query

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 5)

- **URL**: `http://natas6.natas.labs.overthewire.org`
- **Username**: `natas6`
- **Password**: `7mhjtShJAcld2NYbKHEadnhEwRn2P8VT`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 6

### Thử thách
Trang chủ hiển thị một biểu mẫu nhập liệu (Form) với một ô input: `Input secret: [      ]` và nút bấm **Submit Query**.
Bên dưới biểu mẫu có một liên kết: **`View sourcecode`**.

Mục tiêu của bài là tìm ra chuỗi bí mật (**Secret**) chính xác để nhập vào ô và gửi lên máy chủ.

### Phân tích mã nguồn PHP (Source Code Review)
Khi bấm vào liên kết **View sourcecode**, ta đọc được đoạn mã xử lý phía máy chủ (Server-side code):

```php
<?
include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
            print "Access granted. The password for natas7 is <censored>";
        } else {
            print "Wrong secret";
        }
    }
?>
```

### Manh mối & Kiến thức cốt lõi: Rò rỉ mã nguồn từ tệp `.inc` (Source Code Disclosure)

1. **Lệnh `include` trong PHP**:
   - Dòng lệnh `include "includes/secret.inc";` dùng để nạp nội dung của một tệp tin khác vào chạy cùng chương trình.
   - Điều này có nghĩa là biến `$secret` được khởi tạo và lưu giá trị bí mật bên trong tệp `includes/secret.inc`.

2. **Lỗ hổng cấu hình máy chủ Web (Web Server Misconfiguration)**:
   - Các máy chủ web như Apache được cấu hình để gửi các tệp có đuôi `.php` qua trình thông dịch PHP nhằm chạy mã và chỉ trả về kết quả HTML cho người dùng.
   - Tuy nhiên, tệp `secret.inc` lại có phần mở rộng là **`.inc`** (viết tắt của include). Theo mặc định, Apache **không xem đuôi `.inc` là tệp mã cần thực thi**, mà đối xử với nó như một tập tin văn bản tĩnh thông thường (plain text).
   - Vì tệp tin này nằm trực tiếp trong thư mục web (`includes/`), người dùng bên ngoài hoàn toàn có thể truy cập thẳng vào URL của nó để đọc trực tiếp toàn bộ mã nguồn bên trong!

3. **Lưu ý khi mở tệp trên Trình duyệt**:
   - Do nội dung tệp bắt đầu bằng cú pháp `<? ... ?>`, trình duyệt web có thể hiểu lầm đây là một thẻ HTML không hợp lệ và hiển thị ra một trang trắng tinh.
   - Khi gặp trường hợp này, chỉ cần nhấn tổ hợp phím **`Ctrl + U`** (View Source) là toàn bộ mã nguồn sẽ hiện ra.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Dùng để xem mã nguồn và nhập dữ liệu vào biểu mẫu.
- **Burp Suite**: Bắt gói tin POST và chỉnh sửa tham số `secret` (tùy chọn).
- **Dòng lệnh CLI (cURL)**: Đọc file `.inc` và gửi request POST trực tiếp từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 7

### Cách 1: Thao tác trực tiếp trên Trình duyệt

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas6.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas6`
  - **Pass**: `7mhjtShJAcld2NYbKHEadnhEwRn2P8VT`

- **Bước 2**: Nhấp vào liên kết **View sourcecode** hoặc truy cập đường dẫn:
  ```text
  http://natas6.natas.labs.overthewire.org/index-source.html
  ```
  Đọc mã nguồn PHP và phát hiện đường dẫn tệp bí mật: `includes/secret.inc`.

- **Bước 3**: Truy cập trực tiếp vào tệp chứa mã bí mật bằng đường dẫn:
  ```text
  http://natas6.natas.labs.overthewire.org/includes/secret.inc
  ```

- **Bước 4**: Nếu màn hình hiển thị trang trắng, nhấn **`Ctrl + U`** để xem nguồn trang:
  ```php
  <?
  $secret = "FOEIUWGHFEEUHOFUOIU";
  ?>
  ```
  Sao chép chuỗi bí mật:
  ```text
  FOEIUWGHFEEUHOFUOIU
  ```

- **Bước 5**: Quay lại trang chủ:
  ```text
  http://natas6.natas.labs.overthewire.org
  ```
  Dán chuỗi `FOEIUWGHFEEUHOFUOIU` vào ô **Input secret** và nhấn nút **Submit Query**.

- **Bước 6**: Màn hình trả về thông báo chấp thuận kèm mật khẩu của `natas7`!

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Trên trình duyệt của Burp Suite, truy cập đường dẫn:
  ```text
  http://natas6.natas.labs.overthewire.org/includes/secret.inc
  ```
  Nhấn `Ctrl + U` để lấy chuỗi bí mật `FOEIUWGHFEEUHOFUOIU`.

- **Bước 2**: Bật chế độ chặn: **`Intercept is on`**.

- **Bước 3**: Tại trang chủ `http://natas6.natas.labs.overthewire.org`, nhập một giá trị bất kỳ vào ô Secret và bấm **Submit Query**.

- **Bước 4**: Trong tab **`Intercept`** của Burp Suite, quan sát phần nội dung (Body) ở cuối gói tin HTTP POST:
  ```http
  secret=FOEIUWGHFEEUHOFUOIU&submit=Submit
  ```
  Đảm bảo tham số `secret` mang giá trị `FOEIUWGHFEEUHOFUOIU`.

- **Bước 5**: Bấm nút cam **`Forward`**. Trình duyệt sẽ hiển thị mật khẩu của `natas7`.

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

- **Bước 1**: Tải và đọc trực tiếp tệp `secret.inc`:
  ```powershell
  curl.exe -s -u natas6:7mhjtShJAcld2NYbKHEadnhEwRn2P8VT http://natas6.natas.labs.overthewire.org/includes/secret.inc
  ```
  *Đầu ra hiển thị:*
  ```php
  <?
  $secret = "FOEIUWGHFEEUHOFUOIU";
  ?>
  ```

- **Bước 2**: Gửi request POST chứa chuỗi bí mật vừa tìm được:
  ```powershell
  curl.exe -s -u natas6:7mhjtShJAcld2NYbKHEadnhEwRn2P8VT -d "secret=FOEIUWGHFEEUHOFUOIU&submit=Submit" http://natas6.natas.labs.overthewire.org
  ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 7

```text
Password natas7: [B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0]
```

