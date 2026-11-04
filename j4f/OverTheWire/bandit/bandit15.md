# Level 15 -> Level 16

The password for the next level can be retrieved by submitting the password of the current level to *port 30001 on localhost* using SSL/TLS encryption.

Helpful note: Getting "HEARTBEATING" and "Read R BLOCK"? Use -ign_eof with openssl s_client

Commands you may need to solve this level:
`ssh`, `telnet`, `nc`, `openssl`, `s_client`, `nmap`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 14)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit15`
- **Password**: `pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 15

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 15

- **Thử thách**: Tương tự như màn 14, ta cần gửi mật khẩu hiện tại vào cổng `30001` trên `localhost`. Tuy nhiên, cổng dịch vụ này bắt buộc phải sử dụng giao thức kết nối **mã hóa SSL/TLS**.
- **Tại sao không thể dùng `nc` như màn trước?**
  Lệnh `nc` (Netcat) chỉ truyền dữ liệu thô dạng không mã hóa (plaintext). Cổng 30001 yêu cầu bắt tay mã hóa SSL/TLS, do đó Netcat sẽ không thể giao tiếp được.

- **Lệnh mới kinh điển - `openssl s_client` (Client kết nối SSL/TLS)**:
  - `openssl` là bộ công cụ mật mã học tiêu chuẩn trong Linux.
  - Phân hệ `s_client` hoạt động tương tự như Netcat nhưng có tích hợp khả năng mã hóa đường truyền SSL/TLS.
  - Cú pháp cơ bản:
    ```bash
    openssl s_client -connect <host>:<port>
    ```
    *(Lưu ý: giữa host và port ngăn cách bởi dấu hai chấm `:`, ví dụ `localhost:30001`).*
  - Tham số `-ign_eof` (ignore end-of-file): Giúp giữ kết nối ổn định, không bị tự động ngắt khi bạn gửi mật khẩu vào.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 16

### Cách 1: Tương tác nhập thủ công
1. Mở kết nối SSL/TLS đến cổng 30001:
   ```bash
   openssl s_client -connect localhost:30001 -ign_eof
   ```
2. Màn hình sẽ hiện ra thông tin bắt tay chứng chỉ SSL (Certificate). Khi con trỏ đứng đợi, bạn dán mật khẩu của `bandit15` vào và nhấn Enter:
   ```text
   pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7
   ```
3. Máy chủ sẽ in ra thông báo:
   ```text
   Correct!
   <mật_khẩu_của_bandit16>
   ```

### Cách 2: Dùng đường ống Pipe `|` (Ngắn gọn và tự động)
```bash
cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001 -ign_eof
```

Sau khi kết nối và bắt tay mã hóa thành công, bạn nhìn xuống các dòng cuối cùng sẽ thấy dòng `Correct!` đi kèm mật khẩu của bandit16!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 16

```text
Password bandit16: [kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V]
```
