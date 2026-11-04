# Level 18 -> Level 19

The password for the next level is stored in a file *readme* in the homedirectory. Unfortunately, someone has modified *.bashrc* to log you out when you log in with SSH.

Commands you may need to solve this level:
`ssh`, `ls`, `cat`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 17)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit18`
- **Password**: `OQxXZjELndr90zuhOTDYBEomI0SZITXI`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 18

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 18

- **Thử thách**: Khi bạn đăng nhập vào tài khoản `bandit18` như bình thường, vừa nhập mật khẩu xong thì màn hình lập tức in ra dòng chữ **`Byebye!`** và tự động đá văng bạn ra ngoài (ngắt kết nối SSH).
- **Nguyên nhân**: File cấu hình khởi động `.bashrc` của tài khoản này đã bị chèn thêm lệnh thoát (`exit/logout`). Mỗi khi bạn mở một phiên tương tác dòng lệnh (interactive shell), file `.bashrc` sẽ tự động chạy và lập tức đóng phiên kết nối của bạn.

- **Kỹ thuật mới - Thực thi lệnh trực tiếp qua SSH (SSH Command Execution)**:
  - Bình thường, lệnh `ssh <user>@<host>` sẽ yêu cầu mở một cửa sổ giao tiếp hoàn chỉnh.
  - Tuy nhiên, SSH cho phép bạn **truyền trực tiếp một câu lệnh muốn chạy ngay sau lệnh SSH**. Khi đó, SSH sẽ chạy đúng lệnh đó trên máy chủ từ xa, in kết quả về máy bạn rồi mới đóng lại, mà **không khởi động phiên shell tương tác (bỏ qua `.bashrc`)**!
  - Cú pháp:
    ```bash
    ssh <user>@<host> -p <port> "<câu_lệnh_muốn_chạy>"
    ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 19

Thay vì đăng nhập vào giao diện shell, bạn hãy đứng ngay trên Terminal của máy bạn và truyền trực tiếp lệnh vào đuôi câu lệnh SSH:

### Bước 1: Xem các file trong thư mục của bandit18
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
```
*(Nhập mật khẩu: `OQxXZjELndr90zuhOTDYBEomI0SZITXI`).*
*Kết quả hiển thị*: file `readme`.

### Bước 2: Đọc file readme để lấy mật khẩu
Truyền lệnh `cat readme` trực tiếp vào SSH:
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```
*(Nhập lại mật khẩu: `OQxXZjELndr90zuhOTDYBEomI0SZITXI`).*

*Kết quả*: Hệ thống sẽ đọc ngay nội dung file `readme` và in thẳng mật khẩu của `bandit19` về màn hình máy bạn!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 19

```text
Password bandit19: [KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI]
```
