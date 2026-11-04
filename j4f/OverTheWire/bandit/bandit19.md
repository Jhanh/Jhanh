# Level 19 -> Level 20

To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

Commands you may need to solve this level:
Không có lệnh mới đặc thù (thao tác thực thi file binary).

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 18)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit19`
- **Password**: `KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 19

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit19@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 19

- **Thử thách**: Mật khẩu của Level 20 nằm tại đường dẫn quen thuộc: `/etc/bandit_pass/bandit20`. Tuy nhiên, tài khoản `bandit19` không có quyền đọc file này (nếu gõ `cat` trực tiếp sẽ bị `Permission denied`).
- Để giải quyết, đề bài cung cấp sẵn một file thực thi đặc biệt trong thư mục nhà có tên là `bandit20-do`.

- **Khái niệm then chốt trong Linux Privilege - Quyền SUID (Set User ID)**:
  - Thông thường trong Linux, khi bạn chạy một chương trình, chương trình đó sẽ chạy với quyền hạn của chính bạn.
  - Tuy nhiên, khi một file thực thi được gán quyền **SUID** (khi xem bằng lệnh `ls -l` bạn sẽ thấy chữ `s` thay vì `x`, ví dụ: `-rwsr-x---`), chương trình đó sẽ **tạm thời chạy với quyền hạn của người sở hữu file đó** (ở đây là `bandit20`), bất kể ai là người bấm chạy!
  - Trong thực tế, các lệnh như `passwd` hay `sudo` đều dùng cơ chế SUID này để mượn quyền hạn cao hơn một cách an toàn.

- **File `bandit20-do`**:
  - File này đóng vai trò như một lệnh `sudo` thu nhỏ: nó cho phép bạn truyền vào một câu lệnh bất kỳ, và nó sẽ chạy câu lệnh đó dưới tư cách của user `bandit20`.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 20

- **Bước 1**: Kiểm tra file và quyền hạn trong thư mục:
  ```bash
  ls -la
  ```
  *Kết quả hiển thị*: file `bandit20-do` thuộc quyền sở hữu của user `bandit20` và có cờ quyền `s` (SUID).

- **Bước 2**: Chạy thử file không kèm tham số để xem hướng dẫn:
  ```bash
  ./bandit20-do
  ```
  *Kết quả*: Chương trình in ra hướng dẫn:
  ```text
  Run a command as another user.
    Example: ./bandit20-do id
  ```

- **Bước 3**: Dùng `bandit20-do` để đọc file mật khẩu với quyền của bandit20:
  ```bash
  ./bandit20-do cat /etc/bandit_pass/bandit20
  ```

Màn hình sẽ in ra chuỗi mật khẩu chính thức của bandit20!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 20

```text
Password bandit20: [4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA]
```
