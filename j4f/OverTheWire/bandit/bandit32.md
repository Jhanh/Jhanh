# Level 32 -> Level 33

After all this git stuff it’s time for another escape. Good luck!

Commands you may need to solve this level:
`sh`, `man`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ LEVEL 31)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit32`
- **Password**: `pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 32

Mở Terminal / PowerShell trên máy bạn và chạy:

```bash
ssh bandit32@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, nhập password: `pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 32

1. **Thử thách Vỏ bọc chữ hoa (The Uppercase Shell)**:
   - Khi đăng nhập thành công vào `bandit32`, bạn sẽ bị đưa vào một shell tự chế có tên là **Uppercase Shell** với lời chào:
     ```text
     WELCOME TO THE UPPERCASE SHELL
     >>
     ```
   - Shell này tự động chuyển đổi mọi ký tự bạn gõ thành chữ in hoa. Do các lệnh trong Linux phân biệt chữ hoa chữ thường (Case-Sensitive), các câu lệnh quen thuộc như `ls`, `cat`, `whoami` sẽ bị đổi thành `LS`, `CAT`, `WHOAMI` và báo lỗi `command not found`.

2. **Kỹ thuật Breakout Shell bằng biến `$0` (Positional Parameter Escape)**:
   - Trong Linux shell, `$0` là một biến đặc biệt (tham số vị trí số 0) luôn lưu giữ tên của chương trình hoặc trình thông dịch shell đang chạy lệnh đó (thường là `/bin/sh` hoặc `/bin/bash`).
   - Vì `$0` chứa ký tự số `0` (số không có khái niệm chữ hoa hay chữ thường), shell chữ hoa không thể thay đổi được giá trị này.
   - Khi bạn gõ `$0` và nhấn Enter, hệ thống sẽ thực thi ngay chính trình thông dịch shell nguyên bản (`/bin/sh`), giúp bạn thoát ra một terminal bình thường.

3. **Kế thừa quyền SUID của `bandit33`**:
   - Chương trình Uppercase Shell được cấu hình SUID thuộc quyền sở hữu của người dùng `bandit33`. Do đó, khi bạn gọi `$0` để sinh ra shell con từ chương trình này, shell con sẽ tự động kế thừa quyền của `bandit33`, cho phép bạn đọc trực tiếp mật khẩu của bài cuối cùng!

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 33

### Bước 1: Kết nối SSH vào bandit32
*(Thực hiện trên Terminal / PowerShell máy của bạn)*

Chạy lệnh kết nối:
```bash
ssh bandit32@bandit.labs.overthewire.org -p 2220
```
Nhập mật khẩu: `pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT`

Màn hình sẽ hiển thị giao diện Uppercase Shell:
```text
WELCOME TO THE UPPERCASE SHELL
>>
```

---

### Bước 2: Thoát khỏi Uppercase Shell
*(Thực hiện tại dấu nhắc `>>`)*

Gõ biến tham số vị trí:
```text
$0
```
và nhấn **Enter**.

Ngay lập tức, dấu nhắc `>>` sẽ biến mất và chuyển thành dấu nhắc shell thông thường:
```text
$
```

---

### Bước 3: Kiểm tra quyền và lấy mật khẩu bandit33
*(Thực hiện trên terminal mới vừa thoát ra)*

1. Kiểm tra danh tính hiện tại:
   ```bash
   whoami
   ```
   *(Kết quả sẽ trả về bạn đang có quyền của `bandit33`).*

2. Đọc file mật khẩu của `bandit33`:
   ```bash
   cat /etc/bandit_pass/bandit33
   ```
   *Màn hình sẽ in ra mật khẩu chính thức của Level 33!*

---

### Bước 4: Thoát khỏi kết nối
1. Thoát khỏi shell con để quay lại Uppercase Shell:
   ```bash
   exit
   ```
   *(Dấu nhắc sẽ trở lại `>>`).*

2. Thoát hẳn khỏi Uppercase Shell:
   - Tại dấu nhắc `>>`, nếu bạn gõ chữ `exit` thì shell này sẽ tự biến nó thành chữ in hoa `EXIT` và báo lỗi `sh: 1: EXIT: Permission denied`.
   - **Cách thoát chuẩn**: Nhấn tổ hợp phím **`Ctrl + D`** trên bàn phím (gửi tín hiệu kết thúc EOF) để ngắt hoàn toàn kết nối SSH.
   - *(Hoặc bấm phím `Enter` rồi gõ `~.` để ép client SSH ngắt kết nối ngay lập tức).*

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 33

```text
Password bandit33: [u4P2CyPOwPGLe94RdD9Uo2FxFwvnFswM]
```
