# Level 28 -> Level 29

There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo via the port 2220. The password for the user bandit28-git is the same as for the user bandit28.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

Commands you may need to solve this level:
`git`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ LEVEL 27)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit28`
- **Password**: `y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 28

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit28@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 28

1. **Lỗ hổng lộ lọt thông tin trong lịch sử Git (Git Commit History Leak)**:
   - Trong quá trình phát triển phần mềm, lập trình viên thường vô tình commit mã bí mật (mật khẩu, API key, token) rồi sau đó nhận ra và sửa lại bằng cách xóa hoặc thay bằng `xxxxxxxxx`.
   - Tuy nhiên, **Git lưu giữ toàn bộ lịch sử thay đổi**. Kể cả khi bạn đã xóa hoặc che giấu thông tin ở commit mới nhất, phiên bản cũ chứa mật khẩu vẫn còn nguyên vẹn trong lịch sử commit.

2. **Các lệnh Git quan trọng để truy vết lịch sử**:
   - `git log`: Hiển thị danh sách các lần commit (mã băm commit hash, tác giả, ngày giờ, thông điệp commit).
   - `git log -p`: Hiển thị lịch sử commit kèm theo sự thay đổi chi tiết từng dòng (diff: dòng màu xanh thêm vào `+`, dòng màu đỏ bị xóa `-`).
   - `git show <commit-hash>`: Xem chi tiết nội dung thay đổi của một commit cụ thể.
   - `git checkout <commit-hash>`: Quay ngược trạng thái của toàn bộ thư mục về thời điểm của commit đó.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 29

### Cách 1: Thực hiện trực tiếp trên máy tính của bạn (Khuyến nghị)
*(Thực hiện trên PowerShell tại máy của bạn)*

1. Mở PowerShell tại thư mục làm việc của bạn trên máy tính.

2. Clone kho lưu trữ git về máy:
   ```powershell
   git clone ssh://bandit28-git@bandit.labs.overthewire.org:2220/home/bandit28-git/repo
   ```
   - Xác nhận `yes` nếu được hỏi fingerprint.
   - Nhập mật khẩu của `bandit28-git` (chính là mật khẩu của `bandit28`):
     ```text
     y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ
     ```

3. Đi vào thư mục vừa clone và kiểm tra file:
   ```powershell
   cd repo
   cat README.md
   ```
   *Bạn sẽ thấy mật khẩu đã bị che mất bằng các ký tự `xxxxxxxxx`.*

4. Kiểm tra lịch sử commit để tìm mật khẩu:
   ```powershell
   git log
   ```
   *Bạn sẽ thấy các commit trong quá khứ, ví dụ một commit có nội dung "fix info leak" (sửa lỗi lộ thông tin) và commit trước đó.*
   *(Mẹo: Khi màn hình hiển thị danh sách commit dài và dừng lại ở dấu `:` hoặc `(END)`, hãy nhấn phím **`q`** trên bàn phím để thoát trở về dòng lệnh).*

5. Xem chi tiết nội dung bị lộ:
   - Cách nhanh nhất là xem diff trực tiếp:
     ```powershell
     git log -p
     ```
     *(Nhấn phím **`q`** để thoát khỏi màn hình xem diff sau khi đã đọc xong).*
   - Hoặc xem commit trước thời điểm bị sửa:
     ```powershell
     git show <mã_hash_của_commit_trước_đó>
     ```
   *Màn hình sẽ hiển thị dòng chữ chứa mật khẩu thực sự của bandit29 (thường hiển thị ở dòng màu đỏ bị xóa `-`).*

6. **Dọn dẹp thư mục sau khi hoàn thành**:
   - Sau khi ghi lại mật khẩu, lùi ra ngoài và xóa thư mục `repo`:
     ```powershell
     cd ..
     Remove-Item -Recurse -Force repo
     ```

---

### Cách 2: Thực hiện từ bên trong phiên SSH của bandit28
*(Nếu bạn muốn thao tác ngay trên server game)*

1. Tạo thư mục tạm và đi vào đó:
   ```bash
   cd $(mktemp -d)
   ```

2. Clone kho lưu trữ git qua cổng 2220:
   ```bash
   git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
   ```
   *(Nhập mật khẩu: `y8Yd2ssKcpHpud7UvOSOxwamRMzIGIeQ`).*

3. Đi vào thư mục và truy vết lịch sử:
   ```bash
   cd repo
   git log -p
   ```
   *(Nhấn phím `q` để thoát khỏi màn hình xem log).*

4. Dọn dẹp và thoát:
   ```bash
   cd ..
   rm -rf repo
   exit
   ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 29

```text
Password bandit29: [Em7eGtqaMySwNFjCpwzzHhLhospOcdt0]
```
