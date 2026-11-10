# Level 0 -> Level 1 

Natas teaches the basics of serverside web-security.

Each level of natas consists of its own website located at `http://natasX.natas.labs.overthewire.org`, where `X` is the level number. There is no SSH login. To access a level, enter the username for that level (e.g. `natas0` for level 0) and its password.

Each level has access to the password of the next level. Your job is to somehow obtain that next password and level up. All passwords are also stored in `/etc/natas_webpass/`. E.g. the password for natas5 is stored in the file `/etc/natas_webpass/natas5` and only readable by natas4 and natas5.

You can find the password for the next level on this page.

---

## 1. THÔNG TIN TRUY CẬP

- **URL**: `http://natas0.natas.labs.overthewire.org`
- **Username**: `natas0`
- **Password**: `natas0`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. KIẾN THỨC NỀN TẢNG CẦN NẮM

- **Mã nguồn phía máy khách (Client-Side Source Code)**:
  - Khi bạn truy cập một trang web, máy chủ web (Web Server) sẽ gửi toàn bộ mã HTML, CSS và JavaScript về máy tính của bạn để trình duyệt dựng (render) giao diện trực quan.
  - Bất kỳ nội dung nào được gửi về máy khách đều có thể được người dùng xem được đầy đủ, không có gì bị che giấu trên máy của bạn.

- **Ghi chú HTML (HTML Comments)**:
  - Cú pháp: `<!-- Nội dung ghi chú ở đây -->`
  - Mục đích chính của ghi chú là để lập trình viên giải thích mã nguồn cho nhau đọc hoặc tạm thời ẩn một đoạn mã trong lúc phát triển.
  - Trình duyệt sẽ **bỏ qua** và không hiển thị nội dung ghi chú này lên màn hình giao diện.

- **Lỗ hổng rò rỉ thông tin (Information Disclosure)**:
  - Việc nhà phát triển bất cẩn để lại thông tin nhạy cảm (như mật khẩu, tài khoản admin, API keys, đường dẫn bí mật, cấu trúc cơ sở dữ liệu) ngay trong ghi chú HTML là một trong những lỗi sơ đẳng và phổ biến nhất trong an toàn ứng dụng web.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt web**: Bất kỳ trình duyệt nào (Google Chrome, Firefox, Microsoft Edge, Brave...).
  - Phím tắt xem mã nguồn (View Source): `Ctrl + U`
  - Phím tắt mở công cụ phát triển (DevTools / Inspect Elements): `F12` hoặc `Ctrl + Shift + I`
- **Dòng lệnh CLI (kế thừa từ Bandit)**:
  - Lệnh `curl` (hoặc `curl.exe` trên PowerShell): Công cụ gửi request HTTP/HTTPS trực tiếp từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 1

### Cách 1: Sử dụng Trình duyệt Web (GUI)

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas0.natas.labs.overthewire.org
  ```

- **Bước 2**: Khi trình duyệt hiện hộp thoại yêu cầu đăng nhập:
  - Nhập **Username**: `natas0`
  - Nhập **Password**: `natas0`

- **Bước 3**: Sau khi trang web tải xong, bạn sẽ thấy dòng chữ:
  > *"You can find the password for the next level on this page."*

- **Bước 4**: Xem mã nguồn trang web bằng một trong hai cách:
  - **Cách A**: Nhấn tổ hợp phím **`Ctrl + U`** (hoặc click chuột phải vào vùng trống bất kỳ trên trang $\rightarrow$ chọn **View page source** / Xem nguồn trang).
  - **Cách B**: Nhấn phím **`F12`** $\rightarrow$ chọn tab **Elements**.

- **Bước 5**: Kiểm tra nội dung mã nguồn HTML, tại thẻ `<div id="content">` (khoảng dòng 15):
  ```html
  <!--The password for natas1 is scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7 -->
  ```
  Mật khẩu của `natas1` đã được tìm thấy!

---

### Cách 2: Sử dụng dòng lệnh Terminal / PowerShell (CLI)

Bạn có thể vận dụng ngay kỹ năng dòng lệnh đã học từ Bandit bằng cách gửi HTTP request kèm xác thực Basic Auth:

```powershell
curl.exe -s -u natas0:natas0 http://natas0.natas.labs.overthewire.org
```

**Giải thích tham số:**
- `-s` (silent): Ẩn thanh tiến trình tải.
- `-u natas0:natas0`: Cung cấp thông tin xác thực `username:password` cho HTTP Basic Auth.

*Kết quả in ra terminal sẽ chứa toàn bộ mã nguồn HTML kèm mật khẩu của natas1.*

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 1

```text
Password natas1: [scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7]
```
