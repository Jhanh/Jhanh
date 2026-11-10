# Level 8 -> Level 9

Input secret: [      ]
Submit Query

---

## 1. THÔNG TIN TRUY CẬP (DÙNG PASSWORD TÌM ĐƯỢC TỪ NATAS 7)

- **URL**: `http://natas8.natas.labs.overthewire.org`
- **Username**: `natas8`
- **Password**: `ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc`
- **Giao thức xác thực**: HTTP Basic Authentication

---

## 2. THỬ THÁCH & KIẾN THỨC NỀN TẢNG CỦA LEVEL 8

### Thử thách
Tương tự như Level 6, trang web hiển thị một biểu mẫu nhập chuỗi bí mật (**Secret**). Khi nhập đúng, máy chủ sẽ cung cấp mật khẩu của `natas9`.

Bên dưới biểu mẫu có liên kết **`View sourcecode`**.

### Phân tích mã nguồn PHP (`index-source.html`)
Khi mở mã nguồn, ta đọc được đoạn mã xử lý sau:

```php
<?
$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
        print "Access granted. The password for natas9 is <censored>";
    } else {
        print "Wrong secret";
    }
}
?>
```

### Manh mối & Kiến thức cốt lõi: Phân biệt Mã hóa dữ liệu (Encoding) và Mật mã học (Encryption)

1. **Encoding không phải là Encryption**:
   - **Mã hóa biểu diễn dữ liệu (Encoding)** như Base64, Hexadecimal (`bin2hex`) hay đảo chuỗi (`strrev`) **không có tính bảo mật**.
   - Mục đích của encoding chỉ là chuyển đổi định dạng dữ liệu để truyền tải an toàn qua các giao thức mạng, hoàn toàn **không cần khóa bí mật (Secret Key)** để giải mã.
   - Bất kỳ ai nhìn thấy thuật toán encode đều có thể thực hiện quá trình đảo ngược (Reversible) để khôi phục dữ liệu gốc 100%.

2. **Quy trình mã hóa ban đầu**:
   Chuỗi gốc `$secret` đã trải qua 3 bước biến đổi liên tiếp:
   ```text
   [Secret] ──> base64_encode() ──> strrev() ──> bin2hex() ──> [3d3d516343746d4d6d6c315669563362]
   ```

3. **Thuật toán đảo ngược để tìm Secret**:
   Để tìm lại `$secret`, ta chỉ cần thực hiện các hàm đối nghịch theo thứ tự ngược lại từ phải sang trái:
   ```text
   [3d3d516343746d4d6d6c315669563362] ──> hex2bin() ──> strrev() ──> base64_decode() ──> [Secret]
   ```

   - **Bước 1 (Chuyển Hex sang chuỗi text - `hex2bin`)**:
     Chuỗi `3d3d516343746d4d6d6c315669563362` $\rightarrow$ `==QcCtmMml1ViV3b`
   - **Bước 2 (Đảo ngược chuỗi - `strrev`)**:
     Chuỗi `==QcCtmMml1ViV3b` $\rightarrow$ `b3ViV1lmMmtCcQ==`
     *(Dấu đệm `==` quen thuộc của Base64 đã xuất hiện ở cuối chuỗi).*
   - **Bước 3 (Giải mã Base64 - `base64_decode`)**:
     Chuỗi `b3ViV1lmMmtCcQ==` $\rightarrow$ `oubWYf2kBq`

---

## 3. CÔNG CỤ CẦN DÙNG

- **Trình duyệt Web**: Xem mã nguồn và gửi dữ liệu qua biểu mẫu.
- **Python / PHP CLI / Burp Suite Decoder**: Dùng để viết kịch bản giải mã một dòng nhanh chóng.
- **Dòng lệnh CLI (cURL)**: Kiểm tra và gửi request POST.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 9

### Bước 1: Xem mã nguồn để lấy chuỗi đã mã hóa
- Mở trình duyệt và truy cập đường dẫn:
  ```text
  http://natas8.natas.labs.overthewire.org
  ```
  Đăng nhập với tài khoản:
  - **User**: `natas8`
  - **Pass**: `ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc`

- Bấm vào liên kết **View sourcecode** hoặc truy cập đường dẫn:
  ```text
  http://natas8.natas.labs.overthewire.org/index-source.html
  ```
- Thu thập giá trị chuỗi `$encodedSecret`:
  ```text
  3d3d516343746d4d6d6c315669563362
  ```

---

### Bước 2: Thực hiện giải mã ngược để lấy Secret

Bạn có thể chọn 1 trong các cách sau:

#### Cách A: Sử dụng Python trên PowerShell / Terminal (Khuyên dùng)
Chạy lệnh sau trên terminal của bạn:
```powershell
python -c "import base64; print(base64.b64decode(bytes.fromhex('3d3d516343746d4d6d6c315669563362').decode('ascii')[::-1]).decode('ascii'))"
```
*Kết quả in ra màn hình:*
```text
oubWYf2kBq
```

#### Cách B: Sử dụng PHP trực tiếp từ dòng lệnh
```powershell
php -r 'echo base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362"))) . PHP_EOL;'
```

#### Cách C: Sử dụng công cụ Decoder trong Burp Suite
1. Trong Burp Suite, bấm vào tab **`Decoder`** trên thanh menu chính.
2. Dán chuỗi `3d3d516343746d4d6d6c315669563362` vào khung trên cùng.
3. Ở menu bên phải, chọn **Decode as...** $\rightarrow$ chọn **`ASCII hex`** *(Lưu ý: Không chọn mục `Hex` vì `Hex` sẽ hiểu là một con số và đổi sang hệ thập phân)* $\rightarrow$ thu được chuỗi `==QcCtmMml1ViV3b` ở khung thứ 2.
4. Vì Burp Decoder không có sẵn tính năng đảo ngược chuỗi (`strrev`), bạn copy chuỗi `==QcCtmMml1ViV3b` và đảo ngược thứ tự các ký tự lại thành:
   ```text
   b3ViV1lmMmtCcQ==
   ```
5. Dán chuỗi `b3ViV1lmMmtCcQ==` vào một khung mới $\rightarrow$ chọn **Decode as...** $\rightarrow$ **`Base64`** $\rightarrow$ thu được kết quả: `oubWYf2kBq`.

---

### Bước 3: Nhập Secret và nhận mật khẩu Level 9

#### Thao tác trên Trình duyệt:
1. Quay lại trang chủ:
   ```text
   http://natas8.natas.labs.overthewire.org
   ```
2. Dán chuỗi bí mật vừa giải mã vào ô **Input secret**:
   ```text
   oubWYf2kBq
   ```
3. Bấm **Submit Query** $\rightarrow$ Máy chủ in ra mật khẩu của `natas9`.

#### Thao tác qua dòng lệnh cURL:
```powershell
curl.exe -s -u natas8:ugXL95KQmUAJJj6bMezOlBNDyI9Imwkc -d "secret=oubWYf2kBq&submit=Submit" http://natas8.natas.labs.overthewire.org
```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 9

```text
Password natas9: [UdxmI27dTaXmnd1rxKQTfws6jihTdcQ9]
```
