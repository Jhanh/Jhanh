# Level 2 -> Level 3

There is nothing on this page

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 1)

- **URL**: `http://natas2.natas.labs.overthewire.org`
- **Username**: `natas2`
- **Password**: `vsDOxoXyq3wckCP1ZmTZ71ngIA606odB`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 2

### Thử thách
Giao diện trang web chỉ có duy nhất một dòng thông báo ngắn:
> *"There is nothing on this page"*

Khi kiểm tra mã nguồn HTML (`Ctrl + U`), chúng ta không còn thấy mật khẩu được giấu sẵn trong comment nữa, mà chỉ thấy:
```html
<div id="content">
There is nothing on this page
<img src="files/pixel.png">
</div>
```

### Manh mối & Kiến thức cốt lõi: Lỗ hổng Directory Listing (Liệt kê thư mục)

1. **Đường dẫn tài nguyên tĩnh (`files/pixel.png`)**:
   - Thẻ `<img>` tham chiếu đến một bức ảnh vô hình (pixel 1x1) nằm trong thư mục `files/`.
   - Điều này tiết lộ rằng trên máy chủ tồn tại một thư mục có tên là `/files/`.

2. **Lỗ hổng duyệt thư mục (Directory Listing / Directory Browsing)**:
   - Trên các máy chủ web (như Apache, Nginx), khi người dùng truy cập vào một thư mục (ví dụ `/files/`):
     - Nếu thư mục đó **không có** file chỉ mục mặc định (như `index.html`, `index.php`), và
     - Máy chủ **bật tính năng liệt kê thư mục** (mặc định trong Apache là `Options Indexes`).
   - Máy chủ sẽ tự động tạo một trang web hiển thị danh sách toàn bộ các tập tin và thư mục con đang có (tiêu đề thường là *Index of /files*).
   - **Rủi ro an ninh**: Kẻ tấn công có thể xem được các tệp tin không được bảo vệ mà quản trị viên vô tình lưu trữ (như file mã nguồn, file cấu hình, file tài liệu, tệp log hoặc dữ liệu người dùng).

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Dùng phím tắt `Ctrl + U` để xem mã nguồn và thanh địa chỉ URL để điều hướng thư mục.
- **Dòng lệnh CLI (cURL)**: Kiểm tra mã nguồn và nội dung thư mục trực tiếp qua terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 3

### Cách 1: Thao tác trên Trình duyệt

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas2.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas2`
  - **Pass**: `vsDOxoXyq3wckCP1ZmTZ71ngIA606odB`

- **Bước 2**: Nhấn tổ hợp phím **`Ctrl + U`** để xem mã nguồn trang, phát hiện thẻ ảnh:
  ```html
  <img src="files/pixel.png">
  ```

- **Bước 3**: Thử truy cập trực tiếp vào thư mục cha của bức ảnh bằng đường dẫn:
  ```text
  http://natas2.natas.labs.overthewire.org/files/
  ```

- **Bước 4**: Trang web hiển thị giao diện **Index of /files** chứa 2 tập tin:
  - `pixel.png` (bức ảnh hiển thị ngoài trang chủ)
  - `users.txt` (tập tin văn bản đáng ngờ)

- **Bước 5**: Nhấp vào liên kết `users.txt` hoặc truy cập trực tiếp đường dẫn:
  ```text
  http://natas2.natas.labs.overthewire.org/files/users.txt
  ```

  Nội dung file hiển thị danh sách tài khoản:
  ```text
  # username:password
  alice:BYNdCesZqW
  bob:jw2ueICLvT
  charlie:G5vCxkVV3m
  natas3:K30JrSRHzjxq3paUQuwozY4MNvmNFyhI
  eve:zo4mJWyNj2
  mallory:9urtcpzBmH
  ```
  Mật khẩu của tài khoản `natas3` đã lộ diện!

---

### Cách 2: Sử dụng dòng lệnh PowerShell / Terminal

- **Bước 1**: Xem mã nguồn trang chủ:
  ```powershell
  curl.exe -s -u natas2:vsDOxoXyq3wckCP1ZmTZ71ngIA606odB http://natas2.natas.labs.overthewire.org
  ```

- **Bước 2**: Khám phá thư mục `/files/`:
  ```powershell
  curl.exe -s -u natas2:vsDOxoXyq3wckCP1ZmTZ71ngIA606odB http://natas2.natas.labs.overthewire.org/files/
  ```

- **Bước 3**: Đọc trực tiếp nội dung tập tin `users.txt`:
  ```powershell
  curl.exe -s -u natas2:vsDOxoXyq3wckCP1ZmTZ71ngIA606odB http://natas2.natas.labs.overthewire.org/files/users.txt
  ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 3

```text
Password natas3: [K30JrSRHzjxq3paUQuwozY4MNvmNFyhI]
```
