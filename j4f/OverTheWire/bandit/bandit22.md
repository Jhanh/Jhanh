# Level 22 -> Level 23

A program is running automatically at regular intervals from *cron*, the time-based job scheduler. Look in */etc/cron.d/* for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read.

Commands you may need to solve this level:
`cron`, `crontab`, `crontab(5)`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 21)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit22`
- **Password**: `RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 22

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit22@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 22

- **Thử thách**: Màn này tiếp tục liên quan đến một tác vụ `cron` tự động sao chép mật khẩu sang `/tmp`. Tuy nhiên, tên file đích trong `/tmp` không còn cố định nữa mà được tính toán bằng một công thức mã băm (MD5 hash) bên trong script shell.

- **Kỹ năng đọc hiểu Script Shell (Bash Script)**:
  - Khả năng đọc và phân tích mã nguồn shell script của hệ thống là kỹ năng cực kỳ quan trọng trong an toàn thông tin và quản trị Linux.
  - Các thành phần trong script của màn này:
    - `myname=$(whoami)`: Biến lưu tên người dùng đang chạy script. (Khi cronjob tự động chạy, người sở hữu tiến trình là **`bandit23`**).
    - `mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)`: Công thức tính toán tên file đích bằng cách băm chuỗi văn bản sang mã MD5.
    - `cat /etc/bandit_pass/$myname > /tmp/$mytarget`: Mật khẩu của `bandit23` được ghi vào file `/tmp/<mã_băm_tính_được>`.

- **Chiến thuật giải quyết**:
  - Vì cron chạy dưới quyền `bandit23`, ta chỉ cần thay thế `$myname` bằng `bandit23` rồi tự chạy lại công thức đó để tìm ra tên file đích trong `/tmp`!

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 23

- **Bước 1**: Xem file cấu hình cron của bandit23:
  ```bash
  cat /etc/cron.d/cronjob_bandit23
  ```
  *Kết quả*: Thấy cronjob chạy script `/usr/bin/cronjob_bandit23.sh` mỗi phút.

- **Bước 2**: Đọc nội dung script shell `/usr/bin/cronjob_bandit23.sh`:
  ```bash
  cat /usr/bin/cronjob_bandit23.sh
  ```
  *Kết quả*: Hiển thị đoạn mã tính toán tên file đích:
  ```bash
  myname=$(whoami)
  mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
  cat /etc/bandit_pass/$myname > /tmp/$mytarget
  ```

- **Bước 3**: Tự tính toán tên file đích dành cho bandit23:
  Chạy lệnh sau trên terminal để tính chuỗi mã băm:
  ```bash
  echo I am user bandit23 | md5sum | cut -d ' ' -f 1
  ```
  *Kết quả*: In ra một chuỗi mã băm MD5 gồm 32 ký tự (ví dụ: `8ca3103b12c45c72f337742580b192a5`).

- **Bước 4**: Đọc file mật khẩu trong `/tmp` bằng tên vừa tính được:
  ```bash
  cat /tmp/<chuỗi_mã_băm_vừa_tính_được>
  ```
  *(Hoặc lệnh 1 dòng tự động điền: `cat /tmp/$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)`)*

Màn hình sẽ in ra chuỗi mật khẩu chính thức của bandit23!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 23

```text
Password bandit23: [gKXDTAXnIz3OBxiPjRZ2uqutUlPZrBsw]
```
