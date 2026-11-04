# Level 16 -> Level 17

The credentials for the next level can be retrieved by submitting the password of the current level to *a port on localhost in the range 31000 to 32000*. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Helpful note: Getting "HEARTBEATING" and "Read R BLOCK"? Use -ign_eof with openssl s_client

Commands you may need to solve this level:
`ssh`, `telnet`, `nc`, `openssl`, `s_client`, `nmap`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 15)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit16`
- **Password**: `kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 16

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit16@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 16

- **Thử thách**: Mật khẩu không nằm ở 1 cổng cố định biết trước. Nó đang mở ở một cổng ngẫu nhiên trong dải từ **31000 đến 32000** trên `localhost`.
- **Đặc điểm các cổng trong dải này**:
  - Đa số các cổng đều đóng.
  - Một số cổng mở nhưng chỉ là máy chủ "vẹt" (echo server - bạn gửi gì thì nó lặp lại y hệt).
  - Chỉ có **duy nhất 1 cổng mở hỗ trợ mã hóa SSL/TLS** và sẽ trả về thông tin đăng nhập màn sau khi nhận đúng mật khẩu!
  - Thông tin nhận về ở màn này là **SSH Private Key** của `bandit17` (tương tự như màn 13).

- **Lệnh mới kinh điển - `nmap` (Công cụ quét cổng mạng số 1 thế giới)**:
  - `nmap` (Network Mapper) là công cụ kiểm thử bảo mật hàng đầu dùng để rà quét các cổng mạng đang mở và xác định dịch vụ đang chạy.
  - Quét dải cổng từ 31000 đến 32000:
    ```bash
    nmap -p 31000-32000 localhost
    ```
  - Quét nâng cao (nhận diện cả phiên bản dịch vụ và SSL):
    ```bash
    nmap -sV -p 31000-32000 localhost
    ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 17

### Bước 1: Quét dải cổng tìm các cổng đang mở và có SSL
Chạy lệnh sau trên terminal của bandit16:
```bash
nmap -sV -p 31000-32000 localhost
```
*(Lưu ý: Trong lúc nmap đang chạy, bạn có thể nhấn phím **Enter** hoặc phím **Space** để xem tiến độ % đã hoàn thành).*

*Kết quả*: `nmap` sẽ liệt kê danh sách các cổng đang mở (`open`). Hãy chú ý cổng nào hiển thị dịch vụ là **`ssl`**.

### Bước 2: Kết nối SSL đến cổng vừa tìm được
Dùng `openssl s_client` để gửi mật khẩu của `bandit16` vào cổng đó:
```bash
cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:<cổng_ssl_tìm_được> -ign_eof
```
*(Thay `<cổng_ssl_tìm_được>` bằng số cổng bạn thấy ở Bước 1, ví dụ `31790`).*

*Kết quả*: Màn hình sẽ phản hồi `Correct!` và in ra một đoạn khóa bảo mật dạng:
```text
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
...
-----END OPENSSH PRIVATE KEY-----
```

### Bước 3: Lưu khóa SSH và đăng nhập vào Bandit 17
1. Sao chép toàn bộ đoạn khóa từ `-----BEGIN...` đến `-----END...`.
2. Tạo file `bandit17.key` trên máy tính của bạn và dán nội dung khóa vào.
3. Truy cập vào đúng vị trí thư mục chứa file `bandit17.key` trên PowerShell.
4. Khóa quyền file trên PowerShell của máy bạn (để tránh lỗi `Permissions too open`):
   ```powershell
   icacls .\bandit17.key /inheritance:r
   icacls .\bandit17.key /grant:r "$($env:USERNAME):(R)"
   ```
5. Thoát khỏi bandit16 (`exit`), sau đó từ máy bạn SSH vào `bandit17`:
   ```bash
   ssh -i bandit17.key bandit17@bandit.labs.overthewire.org -p 2220
   ```
6. Khi đã vào `bandit17@bandit:~$`, đọc mật khẩu chính thức:
   ```bash
   cat /etc/bandit_pass/bandit17
   ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 17

```text
Password bandit17: [pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2]
```
