# Level 21 -> Level 22

A program is running automatically at regular intervals from *cron*, the time-based job scheduler. Look in */etc/cron.d/* for the configuration and see what command is being executed.

Commands you may need to solve this level:
`cron`, `crontab`, `crontab(5)`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 20)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit21`
- **Password**: `bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 21

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit21@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 21

- **Thử thách**: Mật khẩu của `bandit22` được tạo và sao chép tự động theo chu kỳ thời gian bởi hệ thống **cron**. Ta cần lần theo dấu vết các file cấu hình và kịch bản (script) để tìm ra nơi mật khẩu được lưu.

- **Khái niệm Lập lịch tác vụ tự động - `cron`**:
  - `cron` là dịch vụ chạy ngầm của Linux chuyên thực hiện các tác vụ tự động theo lịch trình cố định (tương tự Windows Task Scheduler).
  - Thư mục chứa các file lịch trình hệ thống là: `/etc/cron.d/`.
  - Cấu trúc 5 dấu sao `* * * * *` biểu thị lịch chạy: (Phút - Giờ - Ngày trong tháng - Tháng - Ngày trong tuần). Chuỗi `* * * * *` có nghĩa là: **tác vụ này tự động chạy lặp lại sau mỗi 1 phút**.

- **Quy trình điều tra từng bước**:
  1. Kiểm tra thư mục `/etc/cron.d/` để tìm file cấu hình liên quan đến `bandit22`.
  2. Đọc file cấu hình để biết script shell nào đang được chạy.
  3. Đọc mã nguồn script đó để biết nó ghi mật khẩu ra file nào trong `/tmp`.
  4. Đọc file tạm đó để lấy mật khẩu.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 22

- **Bước 1**: Liệt kê các cấu hình cron trong hệ thống:
  ```bash
  ls -la /etc/cron.d/
  ```
  *Kết quả hiển thị*: file cấu hình có tên là `cronjob_bandit22`.

- **Bước 2**: Đọc file cấu hình để xem lệnh đang chạy định kỳ:
  ```bash
  cat /etc/cron.d/cronjob_bandit22
  ```
  *Kết quả*: Màn hình hiển thị lệnh chạy sau mỗi phút:
  ```text
  * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
  ```
  *(Điều này có nghĩa: Cứ mỗi 1 phút, user `bandit22` tự động chạy script `/usr/bin/cronjob_bandit22.sh`).*

- **Bước 3**: Đọc nội dung script shell `/usr/bin/cronjob_bandit22.sh`:
  ```bash
  cat /usr/bin/cronjob_bandit22.sh
  ```
  *Kết quả*: Bạn sẽ thấy đoạn mã copy mật khẩu sang một file trong `/tmp`, có dạng:
  ```bash
  cat /etc/bandit_pass/bandit22 > /tmp/<tên_file_ngẫu_nhiên>
  ```

- **Bước 4**: Đọc file tạm trong `/tmp` vừa tìm được ở Bước 3:
  ```bash
  cat /tmp/<tên_file_ngẫu_nhiên>
  ```

Màn hình sẽ in ra chuỗi mật khẩu chính thức của bandit22!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 22

```text
Password bandit22: [RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz]
```
