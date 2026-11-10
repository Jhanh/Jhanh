# Level 3 -> Level 4

There is nothing on this page
<!-- No more information leaks!! Not even Google will find it this time... -->

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 2)

- **URL**: `http://natas3.natas.labs.overthewire.org`
- **Username**: `natas3`
- **Password**: `K30JrSRHzjxq3paUQuwozY4MNvmNFyhI`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 3

### Thử thách
Giao diện trang chủ hiển thị:
> *"There is nothing on this page"*

Khi kiểm tra mã nguồn HTML (`Ctrl + U`), ta bắt gặp một dòng ghi chú thú vị:
```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```
*(Tạm dịch: Không còn rò rỉ thông tin nữa đâu!! Lần này thì ngay cả Google cũng sẽ không tìm thấy nó...)*

### Manh mối & Kiến thức cốt lõi: Tệp tin `robots.txt`

1. **Google tìm kiếm dữ liệu bằng cách nào?**:
   - Google và các công cụ tìm kiếm khác sử dụng các bot tự động (được gọi là Web Crawlers / Spiders, ví dụ: Googlebot) để thu thập thông tin của các trang web trên Internet.
   - Để kiểm soát những trang/thư mục nào **được phép** hoặc **không được phép** bot lập chỉ mục (index), các quản trị viên sử dụng chuẩn **Robots Exclusion Protocol** thông qua một tập tin có tên là `robots.txt`.

2. **Bản chất của tệp `robots.txt`**:
   - Tập tin này luôn được đặt công khai ngay tại thư mục gốc của website: `http://<domain>/robots.txt`.
   - Cú pháp cơ bản:
     - `User-agent: *` $\rightarrow$ Áp dụng quy tắc cho tất cả các con bot.
     - `Disallow: /duong-dan/` $\rightarrow$ Yêu cầu bot không được thu thập hay hiển thị đường dẫn này lên kết quả tìm kiếm.

3. **Góc nhìn An ninh mạng (Security Risk)**:
   - **`robots.txt` không phải là một cơ chế bảo mật**: Nó chỉ là một thỏa thuận có tính chất tự nguyện, chỉ các bot đứng đắn mới tuân thủ.
   - **"Lạy ông tôi ở bụi này"**: Vì `robots.txt` là tệp công khai, bất kỳ ai cũng có thể đọc được. Các pentester / hacker thường kiểm tra tệp này đầu tiên trong giai đoạn do thám (Reconnaissance) để tìm ra những thư mục nhạy cảm, file bí mật mà quản trị viên cố tình muốn che giấu khỏi Google!

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Dùng phím tắt `Ctrl + U` và thanh địa chỉ URL.
- **Dòng lệnh CLI (cURL)**: Tải và đọc tệp `robots.txt` trực tiếp qua terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 4

### Cách 1: Thao tác trên Trình duyệt

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas3.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas3`
  - **Pass**: `K30JrSRHzjxq3paUQuwozY4MNvmNFyhI`

- **Bước 2**: Nhấn **`Ctrl + U`** xem mã nguồn, nhận thấy gợi ý nhắc đến Google:
  ```html
  <!-- No more information leaks!! Not even Google will find it this time... -->
  ```

- **Bước 3**: Kiểm tra tệp hướng dẫn bot của trang web bằng đường dẫn:
  ```text
  http://natas3.natas.labs.overthewire.org/robots.txt
  ```
  Nội dung tệp hiển thị:
  ```text
  User-agent: *
  Disallow: /s3cr3t/
  ```
  Phát hiện thư mục bí mật đang bị chặn thu thập dữ liệu: `/s3cr3t/`.

- **Bước 4**: Truy cập trực tiếp vào thư mục bí mật đó:
  ```text
  http://natas3.natas.labs.overthewire.org/s3cr3t/
  ```
  Giao diện hiển thị danh sách thư mục **Index of /s3cr3t** chứa tập tin `users.txt`.

- **Bước 5**: Nhấp vào `users.txt` hoặc truy cập trực tiếp đường dẫn:
  ```text
  http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
  ```
  Nội dung tập tin trả về mật khẩu của `natas4`!

---

### Cách 2: Sử dụng dòng lệnh PowerShell / Terminal

- **Bước 1**: Tải và đọc tệp `robots.txt`:
  ```powershell
  curl.exe -s -u natas3:K30JrSRHzjxq3paUQuwozY4MNvmNFyhI http://natas3.natas.labs.overthewire.org/robots.txt
  ```

- **Bước 2**: Khám phá thư mục bí mật `/s3cr3t/`:
  ```powershell
  curl.exe -s -u natas3:K30JrSRHzjxq3paUQuwozY4MNvmNFyhI http://natas3.natas.labs.overthewire.org/s3cr3t/
  ```

- **Bước 3**: Đọc trực tiếp nội dung tập tin `users.txt`:
  ```powershell
  curl.exe -s -u natas3:K30JrSRHzjxq3paUQuwozY4MNvmNFyhI http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
  ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 4

```text
Password natas4: [JDrPnuZAKyl6MkiqQGFIddrqpvgOASth]
```
