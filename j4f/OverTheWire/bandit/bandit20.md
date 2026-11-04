# Level 20 -> Level 21

There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you think

Commands you may need to solve this level:
`ssh`, `nc`, `cat`, `bash`, `screen`, `tmux`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 19)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit20`
- **Password**: `4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 20

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit20@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 20

- **Thử thách**: Trong thư mục có file chạy SUID tên là `suconnect`.
  - Cơ chế hoạt động của `suconnect`: Bạn truyền vào cho nó 1 số cổng (ví dụ `./suconnect 12345`). Nó sẽ tự động kết nối vào cổng đó trên `localhost`, đọc dữ liệu gửi tới. Nếu dữ liệu gửi tới đúng là mật khẩu của `bandit20`, nó sẽ gửi trả lại mật khẩu của `bandit21`!
  - Nhiệm vụ của bạn: **Tự mở một cổng dịch vụ lắng nghe (listener)** trên máy chủ và chuẩn bị sẵn mật khẩu `bandit20` để gửi cho `suconnect`.

- **Khái niệm Lắng nghe mạng với Netcat (`nc -l`)**:
  - Ở các màn trước, ta dùng Netcat làm máy khách (client) để kết nối đến cổng người khác.
  - Ở màn này, ta biến Netcat thành **máy chủ lắng nghe (server)** bằng cờ `-l` (listen):
    ```bash
    nc -l -p <cổng_tự_chọn>
    ```
    *(Ví dụ cổng `12345`, `23456`, `45678`... Bạn có thể chọn số cổng tùy ý từ 1024 đến 65535).*

- **Kỹ thuật chạy ngầm (Background Job) với dấu `&`**:
  - Khi chạy lệnh lắng nghe mạng, terminal sẽ bị dừng lại chờ kết nối.
  - Thêm ký tự `&` ở cuối dòng lệnh giúp đẩy tiến trình đó chạy ngầm dưới nền, giải phóng ngay terminal để bạn gõ tiếp lệnh khác!

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 21

### Cách 1: Chạy ngầm trong 1 cửa sổ duy nhất (Khuyên dùng - Nhanh nhất)
1. Khởi động một dịch vụ mạng lắng nghe ở cổng `12345`, nạp sẵn mật khẩu của bandit20 và đẩy chạy ngầm:
   ```bash
   echo "4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA" | nc -l -p 12345 &
   ```
   *(Nếu thấy báo lỗi `Address already in use`, chỉ cần đổi sang cổng khác như `23456` hoặc `45678`).*

2. Chạy ngay file `suconnect` kết nối vào cổng `12345` bạn vừa mở:
   ```bash
   ./suconnect 12345
   ```

*Kết quả*: File `suconnect` sẽ kết nối vào cổng 12345, nhận mật khẩu bandit20 và in ra thông báo:
```text
Read: 4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA
Password matches, sending next password
<mật_khẩu_của_bandit21>
```

---

### Cách 2: Mở 2 cửa sổ Terminal song song (Rất trực quan)
- **Cửa sổ 1**: Đăng nhập `bandit20`, bật cổng lắng nghe:
  ```bash
  echo "4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA" | nc -l -p 12345
  ```
  *(Cửa sổ này sẽ đứng chờ kết nối).*

- **Cửa sổ 2**: Mở một tab Terminal mới, cũng SSH vào `bandit20`, rồi gõ:
  ```bash
  ./suconnect 12345
  ```
  *(Cửa sổ 2 sẽ nhận được ngay mật khẩu của bandit21).*

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 21

```text
Password bandit21: [bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY]
```
