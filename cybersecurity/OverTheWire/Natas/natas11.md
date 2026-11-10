# Level 11 -> Level 12

Cookies are protected with XOR encryption

Background color: [#ffffff] [Set color]

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 10)

- **URL**: `http://natas11.natas.labs.overthewire.org`
- **Username**: `natas11`
- **Password**: `VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 11

### Thử thách
Trang web cho phép người dùng thay đổi màu nền thông qua một ô input `bgcolor`.
Dòng thông báo trên trang ghi:
> *"Cookies are protected with XOR encryption"*

*(Tạm dịch: Cookie được bảo vệ bằng mã hóa XOR).*

Bên dưới có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát thấy đoạn mã xử lý quan trọng:

```php
<?
$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

function xor_encrypt($in) {
    $key = '<censored>';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

function loadData($def) {
    global $_COOKIE;
    $mydata = $def;
    if(array_key_exists("data", $_COOKIE)) {
        $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
        if(is_array($tempdata)) {
            if(array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
                if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
                    $mydata['showpassword'] = $tempdata['showpassword'];
                    $mydata['bgcolor'] = $tempdata['bgcolor'];
                }
            }
        }
    }
    return $mydata;
}

function saveData($d) {
    setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
}
?>
```

Và điều kiện để in ra mật khẩu của `natas12`:
```php
<?
if($data["showpassword"] == "yes") {
    print "The password for natas12 is <censored><br>";
}
?>
```

### Manh mối & Kiến thức cốt lõi: Tấn công bản rõ đã biết trên mã hóa XOR (Known-Plaintext Attack)

1. **Tính chất toán học đặc biệt của phép XOR (`^`)**:
   - Phép toán XOR có tính chất tự đảo nghịch:
     $$C = P \oplus K \iff K = P \oplus C$$
     *(Trong đó: $P$ là Plaintext - bản rõ; $C$ là Ciphertext - bản mã; $K$ là Key - khóa bí mật).*
   - Nếu bạn có trong tay cả **bản rõ ($P$)** và **bản mã ($C$)**, bạn chỉ cần lấy $P \text{ XOR } C$ là sẽ tìm ra ngay **khóa bí mật ($K$)**!

2. **Thu thập $P$ và $C$ từ hệ thống**:
   - **Bản rõ ($P$)**: Mảng `$defaultdata` ban đầu được định nghĩa sẵn trong mã nguồn:
     ```php
     array("showpassword"=>"no", "bgcolor"=>"#ffffff")
     ```
     Khi qua hàm `json_encode()` sẽ trở thành chuỗi:
     ```json
     {"showpassword":"no","bgcolor":"#ffffff"}
     ```
   - **Bản mã ($C$)**: Được máy chủ gửi về và lưu trong Cookie `data`:
     ```text
     EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=
     ```
     Giải mã Base64 chuỗi cookie trên, ta thu được dữ liệu nhị phân của bản mã $C$.

3. **Tìm khóa bí mật $K$**:
   - Thực hiện: $\text{Key} = P \oplus C$.
   - Vì khóa được lặp lại theo chu kỳ (`$i \% \text{strlen}(\$key)`), kết quả XOR trả về một chuỗi lặp:
     ```text
     kBSwkBSwkBSwkBSwkBSwkBSwkBSwkBSw...
     ```
   - Ta tìm được chính xác khóa bí mật của máy chủ là:
     ```text
     kBSw
     ```

4. **Làm giả Cookie mang quyền hạn Admin (`showpassword = yes`)**:
   - Ta tạo bản rõ mới mong muốn ($P_{new}$):
     ```json
     {"showpassword":"yes","bgcolor":"#ffffff"}
     ```
   - Mã hóa bản rõ mới với khóa $K = \text{"kBSw"}$:
     $$C_{new} = P_{new} \oplus K$$
   - Mã hóa Base64 chuỗi $C_{new}$ thu được Cookie giả mạo hoàn chỉnh:
     ```text
     EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
     ```

---

## 3. CÔNG CỤ CẦN DÙNG

- **Python**: Dùng để tính toán khóa XOR và tạo chuỗi cookie giả mạo nhanh chóng.
- **Trình duyệt Web (DevTools F12)**: Thay đổi trực tiếp cookie `data`.
- **Burp Suite**: Can thiệp và gửi cookie qua Repeater / Proxy.
- **Dòng lệnh CLI (cURL)**: Gửi request đính kèm cookie đã làm giả.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 12

### Bước 1: Lấy giá trị Cookie ban đầu
- Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas11.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas11`
  - **Pass**: `VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd`

- Nhấn **`F12`** $\rightarrow$ Tab **Application** (Chrome/Edge) hoặc **Storage** (Firefox) $\rightarrow$ Mục **Cookies** $\rightarrow$ Nhấp vào trang `http://natas11.natas.labs.overthewire.org`.
- Thu thập giá trị cookie có tên `data`:
  ```text
  EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY=
  ```

---

### Bước 2: Chạy Script Python để tìm Key và tạo Cookie giả mạo

Sử dụng tệp kịch bản [src/solve11.py](src/solve11.py) với nội dung:

```python
import base64

# Dữ liệu thu thập từ Natas 11
default_data = b'{"showpassword":"no","bgcolor":"#ffffff"}'
cookie_b64 = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY="
cookie_raw = base64.b64decode(cookie_b64)

# 1. Tìm khóa XOR (Key = Plaintext XOR Ciphertext)
key = bytes([p ^ c for p, c in zip(default_data, cookie_raw)])[:4]
print(f"[+] Key tim duoc: {key.decode()}")

# 2. Tạo cookie mới với quyền hiển thị mật khẩu ("showpassword":"yes")
target_data = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
forged_bytes = bytes([target_data[i] ^ key[i % len(key)] for i in range(len(target_data))])
forged_cookie = base64.b64encode(forged_bytes).decode()
print(f"[+] Cookie gia mao: {forged_cookie}")
```

Chạy script bằng lệnh:
```powershell
python src/solve11.py
```

*(Hoặc chạy lệnh inline nhanh trong PowerShell / Terminal):*
```powershell
python -c "import base64; p = b'{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}'; c = base64.b64decode('EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY='); key = bytes([x ^ y for x, y in zip(p, c)])[:4]; target = b'{\"showpassword\":\"yes\",\"bgcolor\":\"#ffffff\"}'; forged = bytes([target[i] ^ key[i % len(key)] for i in range(len(target))]); print('Key tim duoc:', key.decode()); print('Cookie gia mao:', base64.b64encode(forged).decode())"
```

*Kết quả in ra màn hình:*
- **Key tìm được**: `kBSw`
- **Cookie giả mạo**:
  ```text
  EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
  ```

---

### Bước 3: Gửi Cookie giả mạo lên máy chủ

Bạn có thể chọn 1 trong 3 phương pháp sau:

#### Cách 1: Sửa Cookie trực tiếp trên Trình duyệt thường (F12)
1. Trong cửa sổ DevTools (tab **Application** / **Storage** $\rightarrow$ **Cookies**).
2. Click đúp chuột vào giá trị của cookie `data`.
3. Xóa giá trị cũ và dán giá trị cookie giả mạo mới vào:
   ```text
   EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk/
   ```
4. Nhấn Enter và bấm phím **`F5`** để tải lại trang web $\rightarrow$ Dòng mật khẩu của `natas12` sẽ xuất hiện ngay trên màn hình!

---

#### Cách 2: Sử dụng Burp Suite
1. Mở trình duyệt của Burp Suite (`Open browser`) và truy cập đường dẫn:
   ```text
   http://natas11.natas.labs.overthewire.org
   ```
   Đăng nhập tài khoản:
   - **User**: `natas11`
   - **Pass**: `VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd`

   *(Đăng nhập trên trình duyệt trước giúp gói tin tự động có header `Authorization`, tránh bị máy chủ trả về lỗi `401 Unauthorized`).*

2. Vào tab **`Proxy`** $\rightarrow$ **`HTTP history`** $\rightarrow$ Click chuột phải vào request `natas11` (Status 200) $\rightarrow$ chọn **`Send to Repeater`** (`Ctrl + R`).
3. Trong tab **`Repeater`**, tìm dòng `Cookie: data=...` và thay thế bằng:
   ```http
   Cookie: data=EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk%2F
   ```
   *(Ký tự `/` ở cuối cookie được URL-encode thành `%2F`).*
4. Bấm nút màu cam **`Send`**. Khung **Response** bên phải sẽ trả về mật khẩu của `natas12`.

---

#### Cách 3: Sử dụng dòng lệnh PowerShell / Terminal với cURL
```powershell
curl.exe -s -u natas11:VUMQDmuITOEHzhviLE5V0VG9cPMQkyxd --cookie "data=EGAgHwQ1IxYYMSQYGSZxTUk7NgRJbnEVDCE8GwQwcU1JYTURDSQ1EUk%2F" http://natas11.natas.labs.overthewire.org
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 12

```text
Password natas12: [EAGkE8uzFTxeoTT2mMst9Xy7PX6guEng]
```
