# Level 27 -> Level 28

There is a git repository at *ssh://bandit27-git@localhost/home/bandit27-git/repo* via the port *2220*. The password for the user bandit27-git is the same as for the user bandit27.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

Commands you may need to solve this level:
`git`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ LEVEL 26)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit27`
- **Password**: `STJLJBRRphMxKB392CT4iOr5CbzPU9ER`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 27

Mở Terminal / PowerShell trên máy bạn và chạy:

```bash
ssh bandit27@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 27

1. **Yêu cầu quan trọng của OverTheWire**:
   - Đề bài ghi rõ: *"From your local machine (not the OverTheWire machine!), clone the repository..."*.
   - Giống như lỗi ở bài 25, máy chủ OverTheWire chặn các kết nối loopback tới `localhost:2220` từ bên trong server. Vì vậy, ta sẽ thực hiện clone trực tiếp từ **máy tính cá nhân (PowerShell)** của bạn về máy.

2. **Khái niệm về Git over SSH**:
   - Git là hệ thống quản lý mã nguồn phân tán (Version Control System).
   - Khi clone qua giao thức SSH, cú pháp URL có dạng:
     `ssh://<username>@<host>:<port><đường_dẫn_repo>`
   - Khi clone từ máy tính cá nhân của bạn, địa chỉ host phải trỏ về server game:
     `ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo`
   - Đề bài gợi ý: Mật khẩu của tài khoản `bandit27-git` giống y hệt mật khẩu của `bandit27` (`STJLJBRRphMxKB392CT4iOr5CbzPU9ER`).

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 28

### Cách 1: Thực hiện trực tiếp trên máy tính của bạn (Khuyến nghị theo đề bài)
*(Thực hiện trên PowerShell tại máy của bạn)*

1. Mở PowerShell tại thư mục bạn muốn.

2. Chạy lệnh clone kho lưu trữ git về máy:
   ```powershell
   git clone ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo
   ```
   - Khi hệ thống hỏi xác nhận fingerprint: gõ `yes` rồi nhấn **Enter**.
   - Khi được hỏi mật khẩu của `bandit27-git`, dán mật khẩu:
     ```text
     STJLJBRRphMxKB392CT4iOr5CbzPU9ER
     ```
     rồi nhấn **Enter**.

3. Đi vào thư mục vừa clone và xem nội dung:
   ```powershell
   cd repo
   ls
   Get-Content README
   ```
   *(Hoặc `cat README` trên PowerShell).*

4. Màn hình sẽ hiển thị mật khẩu của Level 28!

---

### Cách 2: Thực hiện từ bên trong phiên SSH của bandit27
*(Nếu bạn muốn thao tác ngay trên server game)*

1. Tạo thư mục tạm và đi vào đó:
   ```bash
   cd $(mktemp -d)
   ```
2. Clone repo qua địa chỉ:
   ```bash
   git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
   ```
   *(Nhập mật khẩu: `STJLJBRRphMxKB392CT4iOr5CbzPU9ER`).*
3. Đọc file `README`:
   ```bash
   cd repo
   cat README
   ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 28

```text
Password bandit28: [y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ]
```
