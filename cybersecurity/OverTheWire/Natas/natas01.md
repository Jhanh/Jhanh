# Level 1 -> Level 2

You can find the password for the next level on this page, but rightclicking has been blocked!

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 0)

- **URL**: `http://natas1.natas.labs.overthewire.org`
- **Username**: `natas1`
- **Password**: `scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 1

### Thử thách
Khi truy cập trang web, giao diện hiển thị thông báo:
> *"You can find the password for the next level on this page, but rightclicking has been blocked!"*

Nếu bạn thử click chuột phải vào trang web để chọn *Inspect* hoặc *View Page Source*, trình duyệt sẽ bật lên một hộp thoại cảnh báo: **"right clicking has been blocked!"** và không cho mở menu ngữ cảnh.

### Cơ chế chặn chuột phải hoạt động như thế nào?
Trang web sử dụng thuộc tính sự kiện của thẻ `<body>` trong HTML:
```html
<body oncontextmenu="javascript:alert('right clicking has been blocked!');return false;">
```
- Sự kiện `oncontextmenu` được kích hoạt khi người dùng nhấn chuột phải.
- Đoạn mã JavaScript gọi hộp thoại `alert(...)` và trả về `return false;` nhằm hủy bỏ hành vi mặc định (ngăn không cho menu chuột phải xuất hiện).

### Nguyên lý bảo mật quan trọng: Vượt qua cơ chế kiểm soát Client-Side (Client-Side Bypass)
- **"Không bao giờ tin tưởng Client (Never trust the client)"**: Đây là nguyên tắc cốt lõi trong bảo mật web.
- Mọi logic kiểm tra, cấm đoán hoặc xác thực nếu chỉ được xử lý ở phía trình duyệt (bằng HTML, CSS hoặc JavaScript) đều **không có giá trị bảo mật thực sự**. Nó chỉ mang tính chất gây khó khăn nhẹ (Security through Obscurity).
- Vì toàn bộ mã nguồn đã được tải về máy khách của bạn, bạn nắm quyền kiểm soát 100% cách máy bạn hiển thị hoặc phân tích dữ liệu đó.

---

## 3. CÁC PHƯƠNG PHÁP VƯỢT QUA CƠ CHẾ CHẶN (BYPASS)

Có nhiều cách linh hoạt để lấy mã nguồn mà không cần click chuột phải:

### Cách 1: Sử dụng phím tắt bàn phím (Khuyên dùng)
Trình duyệt chặn sự kiện chuột nhưng không chặn phím tắt hệ thống:
- **`Ctrl + U`**: Mở trực tiếp tab xem mã nguồn HTML (View Source).
- **`F12`** (hoặc **`Ctrl + Shift + I`**): Mở bộ công cụ nhà phát triển (DevTools) $\rightarrow$ xem tab **Elements**.

### Cách 2: Sử dụng tiền tố `view-source:` trên thanh địa chỉ
Gõ trực tiếp vào thanh địa chỉ (Address Bar) của trình duyệt:
```text
view-source:http://natas1.natas.labs.overthewire.org
```
Trình duyệt sẽ tự động hiển thị mã nguồn mà không kích hoạt sự kiện `oncontextmenu`.

### Cách 3: Vô hiệu hóa JavaScript (Disable JavaScript)
Vì cơ chế chặn được viết bằng JavaScript, nếu tắt JavaScript thì đoạn code đó sẽ hoàn toàn vô hiệu hóa:
1. Nhấn `F12` mở DevTools.
2. Nhấn `F1` (hoặc biểu tượng bánh răng Settings).
3. Tìm mục **Debugger** $\rightarrow$ tích chọn **Disable JavaScript**.
4. Giờ đây bạn có thể click chuột phải bình thường.

### Cách 4: Sử dụng dòng lệnh cURL (CLI)
Công cụ dòng lệnh như `curl` chỉ tải dữ liệu văn bản thô qua giao thức HTTP và không chạy bất kỳ bộ máy JavaScript nào, do đó các bẫy JavaScript phía client hoàn toàn vô tác dụng.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 2

### Cách 1: Thao tác trên Trình duyệt

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas1.natas.labs.overthewire.org
  ```
  Đăng nhập với thông tin tài khoản:
  - **User**: `natas1`
  - **Pass**: `scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7`

- **Bước 2**: Mở mã nguồn trang web:
  - **Cách A**: Nhấn tổ hợp phím **`Ctrl + U`** (hoặc phím **`F12`**).
  - **Cách B**: Dán trực tiếp đường dẫn sau vào thanh địa chỉ của trình duyệt:
    ```text
    view-source:http://natas1.natas.labs.overthewire.org
    ```

- **Bước 3**: Tìm đến khối `<div id="content">`:
  ```html
  <div id="content">
  You can find the password for the
  next level on this page, but rightclicking has been blocked!

  <!--The password for natas2 is vsDOxoXyq3wckCP1ZmTZ71ngIA606odB -->
  </div>
  ```

---

### Cách 2: Sử dụng dòng lệnh PowerShell / Terminal

Chạy lệnh `curl.exe` cùng tài khoản vừa nhận được:

```powershell
curl.exe -s -u natas1:scfWG6qNEIdzqVyfRwEGXyNUfFZkZeQ7 http://natas1.natas.labs.overthewire.org
```

*Đầu ra in ra terminal:*
```html
...
<!--The password for natas2 is vsDOxoXyq3wckCP1ZmTZ71ngIA606odB -->
...
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 2

```text
Password natas2: [vsDOxoXyq3wckCP1ZmTZ71ngIA606odB]
```

