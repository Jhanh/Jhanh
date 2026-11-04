# Level 14 -> Level 15

The password for the next level can be retrieved by submitting the password of the current level to *port 30000 on localhost*.

Commands you may need to solve this level:
`ssh`, `telnet`, `nc`, `openssl`, `s_client`, `nmap`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 13)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit14`
- **Password**: `aaWecNkG4FhxJQxz07uiwzVP6bJiYS65`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 14

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit14@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, nhập password: `aaWecNkG4FhxJQxz07uiwzVP6bJiYS65`. Hoặc bạn vẫn có thể dùng khóa: `ssh -i bandit14.key bandit14@bandit.labs.overthewire.org -p 2220`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 14

- **Thử thách**: Trên máy chủ có một dịch vụ mạng đang chạy ngầm và lắng nghe (listening) tại cổng `30000` trên `localhost`. Để lấy mật khẩu của Level 15, bạn phải gửi mật khẩu hiện tại của `bandit14` vào cổng mạng này.

- **Lệnh mới kinh điển của giới an ninh mạng - `nc` (Netcat)**:
  - Netcat thường được mệnh danh là "con dao pha Thụy Sĩ" trong mạng máy tính. Nó cho phép bạn kết nối, gửi và nhận dữ liệu thô qua các cổng TCP/UDP một cách trực tiếp.
  - Cú pháp kết nối:
    ```bash
    nc <địa_chỉ_host> <cổng_port>
    ```
  - Áp dụng vào thử thách:
    ```bash
    nc localhost 30000
    ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 15

### Cách 1: Tương tác nhập thủ công
1. Chạy lệnh mở kết nối đến cổng 30000:
   ```bash
   nc localhost 30000
   ```
2. Khi con trỏ đứng đợi dữ liệu, bạn dán mật khẩu của `bandit14` vào rồi nhấn Enter:
   ```text
   aaWecNkG4FhxJQxz07uiwzVP6bJiYS65
   ```
3. Máy chủ kiểm tra đúng và in ra kết quả:
   ```text
   Correct!
   <mật_khẩu_của_bandit15>
   ```

### Cách 2: Dùng đường ống Pipe `|` (Ngắn gọn và chuyên nghiệp)
Bạn có thể tận dụng file mật khẩu có sẵn trên hệ thống để truyền thẳng vào cổng 30000 chỉ bằng một dòng lệnh duy nhất:
```bash
cat /etc/bandit_pass/bandit14 | nc localhost 30000
```

Chuỗi ký tự in ra ở dòng `Correct!` chính là mật khẩu của bandit15!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 15

```text
Password bandit15: [pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7]
```
