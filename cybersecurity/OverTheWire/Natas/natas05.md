# Level 5 -> Level 6

Access disallowed. You are not logged in

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 4)

- **URL**: `http://natas5.natas.labs.overthewire.org`
- **Username**: `natas5`
- **Password**: `e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 5

### Thử thách
Sau khi đăng nhập thành công bằng tài khoản `natas5`, giao diện trang web lập tức hiển thị dòng chữ:
> *"Access disallowed. You are not logged in"*

*(Tạm dịch: Truy cập bị từ chối. Bạn chưa đăng nhập).*

Mặc dù chúng ta đã vượt qua bước xác thực HTTP Basic Auth ở cấp độ máy chủ, ứng dụng web bên trong vẫn cho rằng chúng ta "chưa đăng nhập" vào phiên làm việc của nó.

### Manh mối & Kiến thức cốt lõi: HTTP Cookie & Quản lý phiên

1. **HTTP Cookie là gì?**:
   - Giao thức HTTP vốn là **phi trạng thái (Stateless)** — nghĩa là máy chủ không thể tự nhớ bạn là ai giữa các lượt bấm chuyển trang.
   - Để nhận diện người dùng, máy chủ sử dụng **Cookie**:
     - Khi bạn truy cập, máy chủ gửi về tiêu đề phản hồi: `Set-Cookie: tên_cookie=giá_trị`.
     - Trình duyệt sẽ lưu mẩu thông tin này trên máy của bạn và tự động đính kèm tiêu đề `Cookie: tên_cookie=giá_trị` vào **mọi request gửi đi sau đó**.

2. **Phát hiện manh mối trong gói tin phản hồi (Response Header)**:
   - Khi quan sát gói tin phản hồi của máy chủ, ta thấy dòng:
     ```http
     Set-Cookie: loggedin=0
     ```
   - Trang web dùng một biến cookie có tên là `loggedin` với giá trị là `0` (nghĩa là `False` - Chưa đăng nhập).

3. **Lỗ hổng bảo mật: Thao túng Cookie (Cookie Tampering / Insecure Session Management)**:
   - Toàn bộ Cookie đều được lưu trữ trực tiếp trên máy của người dùng.
   - Ứng dụng web đã mắc phải sai lầm nghiêm trọng khi **ủy thác quyền xác thực cho phía Client**: chỉ kiểm tra xem giá trị cookie `loggedin` gửi lên là `0` hay `1` mà không có chữ ký mã hóa (Signature) hay lưu Session an toàn trên máy chủ.
   - Vì vậy, người dùng hoàn toàn có thể tự sửa đổi giá trị từ `0` thành `1` (`True` - Đã đăng nhập) để đánh lừa máy chủ cấp quyền truy cập.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Burp Suite Community Edition**: Công cụ bắt và can thiệp gói tin chuyên nghiệp.
- **Trình duyệt Web (DevTools)**: Dùng phím `F12` để sửa trực tiếp Cookie trong trình duyệt.
- **Dòng lệnh CLI (cURL)**: Dùng cờ `--cookie` để gửi cookie tùy biến qua terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 6

---

### Cách 1: Sử dụng Burp Suite

#### Phương án A: Dùng Proxy Intercept (Chặn và sửa trực tiếp)

*(Lưu ý về cơ chế: Ở lần truy cập đầu tiên, trình duyệt chưa có dữ liệu nên gói tin chưa có header `Cookie:`. Sau khi máy chủ gửi `Set-Cookie: loggedin=0` về, từ lượt F5 tiếp theo trình duyệt mới tự động đính kèm cookie để ta can thiệp).*

- **Bước 1**: Mở Burp Suite $\rightarrow$ Tab **`Proxy`** $\rightarrow$ Đảm bảo nút **`Intercept is off`** (màu xám) để trình duyệt tải bình thường.
- **Bước 2**: Bấm nút **`Open browser`** trên Burp Suite và truy cập đường dẫn:
  ```text
  http://natas5.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas5`
  - **Pass**: `e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M`

  *(Lúc này trang web tải xong và máy chủ đã chính thức gán cookie `loggedin=0` vào trình duyệt).*

- **Bước 3**: Quay lại Burp Suite, bấm vào nút để chuyển thành **`Intercept is on`** (màu xanh - bắt đầu bật chế độ chặn).
- **Bước 4**: Quay lại trình duyệt và nhấn phím **`F5`** (tải lại trang).
- **Bước 5**: Gói tin tải lại bị giữ lại tại tab `Intercept`. Lúc này bạn sẽ thấy xuất hiện dòng:
  ```http
  Cookie: loggedin=0
  ```
  Sửa số `0` thành số `1`:
  ```http
  Cookie: loggedin=1
  ```
- **Bước 6**: Bấm nút màu cam **`Forward`** để gửi gói tin đi. Trang web trên trình duyệt sẽ hiển thị ngay mật khẩu của `natas6`.

---

#### Phương án B: Dùng Repeater (Thử nghiệm và gửi thủ công)

1. Mở Burp Suite $\rightarrow$ Tab **`Proxy`** $\rightarrow$ Đảm bảo **`Intercept is off`** $\rightarrow$ Bấm **`Open browser`** truy cập:
   ```text
   http://natas5.natas.labs.overthewire.org
   ```
2. Chuyển sang tab **`Proxy`** $\rightarrow$ **`HTTP history`** $\rightarrow$ Click chuột phải vào request của `natas5` $\rightarrow$ Chọn **`Send to Repeater`** (`Ctrl + R`).
3. Chuyển sang tab **`Repeater`**, sửa dòng Cookie:
   ```http
   Cookie: loggedin=1
   ```
4. Đảm bảo có dòng trống ở cuối cùng của gói tin, sau đó bấm nút **`Send`**.
5. Mật khẩu xuất hiện tại khung **Response** bên phải.

---

> [!TIP]
> **Mẹo làm siêu tốc trong Repeater (Dán trực tiếp không cần qua Browser)**:
> Bạn có thể bấm dấu cộng **`+`** ở Repeater để mở một tab mới tinh, dán trọn gói nội dung sau vào khung Request rồi bấm **Send**:
> ```http
> GET / HTTP/1.1
> Host: natas5.natas.labs.overthewire.org
> Authorization: Basic bmF0YXM1OmU0ejJOb3kzb3F3UEpVV3pKSDBkc2VONjdDbjFzeTJN
> Cookie: loggedin=1
> Connection: close
> 
> ```
> *(Có sẵn dòng trống ở cuối để không bao giờ bị timeout).*

---

### Cách 2: Sử dụng công cụ DevTools trên Trình duyệt thường (F12)

Bạn có thể chỉnh sửa trực tiếp Cookie đang lưu trong trình duyệt thông thường:

1. Mở trình duyệt (Chrome, Edge, Firefox) và truy cập đường dẫn:
   ```text
   http://natas5.natas.labs.overthewire.org
   ```
   Đăng nhập với User: `natas5` / Pass: `e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M`.

2. Nhấn phím **`F12`** (hoặc click chuột phải chọn **Inspect** / Kiểm tra).

3. Trên thanh tab của DevTools:
   - Chọn tab **Application** (đối với Chrome/Edge) hoặc tab **Storage** (đối với Firefox).
   - Ở cột menu bên trái, tìm mục **Cookies** $\rightarrow$ chọn `http://natas5.natas.labs.overthewire.org`.

4. Bạn sẽ thấy bảng chứa danh sách cookie:
   - Cột **Name**: `loggedin`
   - Cột **Value**: đang là `0`.
   - **Click đúp chuột vào số `0`** và đổi thành số **`1`**, sau đó nhấn Enter.

5. Nhấn phím **`F5`** (hoặc nút Reload) để tải lại trang web $\rightarrow$ Mật khẩu sẽ xuất hiện ngay trên màn hình!

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Tham số `--cookie` (hoặc `-b`) cho phép bạn đính kèm trực tiếp cookie theo ý muốn:

```powershell
curl.exe -s -u natas5:e4z2Noy3oqwPJUWzJH0dseN67Cn1sy2M --cookie "loggedin=1" http://natas5.natas.labs.overthewire.org
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 6

```text
Password natas6: [7mhjtShJAcld2NYbKHEadnhEwRn2P8VT]
```

