# Level 29 -> Level 30

There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo via the port 2220. The password for the user bandit29-git is the same as for the user bandit29.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

Commands you may need to solve this level:
`git`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ LEVEL 28)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit29`
- **Password**: `Em7eGtqaMySwNFjCpwzzHhLhospOcdt0`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 29

Mở Terminal / PowerShell trên máy bạn và chạy:

```bash
ssh bandit29@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, nhập password: `Em7eGtqaMySwNFjCpwzzHhLhospOcdt0`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 29

1. **Khái niệm Phân nhánh trong Git (Git Branching)**:
   - Trong Git, nhánh (branch) cho phép phân tách luồng phát triển ra khỏi nhánh chính (`master` hoặc `main`) để thử nghiệm, phát triển tính năng mới mà không làm ảnh hưởng đến mã nguồn chính thức (production).
   - Khi chạy `git clone`, Git mặc định chỉ tải về và kích hoạt nhánh chính. Tuy nhiên, trên kho lưu trữ từ xa (remote) có thể tồn tại nhiều nhánh phát triển khác (ví dụ: `dev`, `feature`, `staging`).

2. **Thử thách của bài 29**:
   - Khi đọc file `README.md` ở nhánh mặc định `master`, bạn sẽ thấy dòng thông báo kiểu: *"no passwords in production!"* (không lưu mật khẩu trên môi trường chính thức).
   - Mật khẩu thực sự đã được cất giấu trong một nhánh phát triển khác (nhánh `dev`).

3. **Các lệnh Git quan trọng khi làm việc với nhánh**:
   - `git branch -a`: Liệt kê tất cả các nhánh, bao gồm cả nhánh trên máy (`local`) và các nhánh trên máy chủ từ xa (`remote`, có tiền tố `remotes/origin/...`).
   - `git checkout <tên_nhánh>` hoặc `git switch <tên_nhánh>`: Chuyển đổi mã nguồn hiện tại sang một nhánh khác.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 30

### Cách 1: Thực hiện trực tiếp trên máy tính của bạn (Khuyến nghị)
*(Thực hiện trên PowerShell tại máy của bạn)*

1. Mở PowerShell tại thư mục làm việc của bạn trên máy tính.

2. Clone kho lưu trữ git về máy:
   ```powershell
   git clone ssh://bandit29-git@bandit.labs.overthewire.org:2220/home/bandit29-git/repo
   ```
   - Xác nhận `yes` nếu được hỏi fingerprint.
   - Nhập mật khẩu của `bandit29-git` (chính là mật khẩu của `bandit29`):
     ```text
     Em7eGtqaMySwNFjCpwzzHhLhospOcdt0
     ```

3. Đi vào thư mục vừa clone và kiểm tra file ban đầu:
   ```powershell
   cd repo
   cat README.md
   ```
   *Bạn sẽ thấy thông báo đại ý "no passwords in production!".*

4. Kiểm tra danh sách tất cả các nhánh trong kho:
   ```powershell
   git branch -a
   ```
   *Màn hình sẽ hiển thị các nhánh, bạn sẽ thấy có nhánh từ xa dạng: `remotes/origin/dev`.*

5. Chuyển sang nhánh `dev`:
   ```powershell
   git checkout dev
   ```
   *(Hoặc gõ `git switch dev`).*

6. Đọc nội dung file trên nhánh `dev`:
   ```powershell
   cat README.md
   ```
   *Màn hình sẽ in ra mật khẩu chính thức của Level 30!*

7. **Dọn dẹp thư mục sau khi hoàn thành**:
   - Sau khi ghi lại mật khẩu, lùi ra ngoài và xóa thư mục `repo`:
     ```powershell
     cd ..
     Remove-Item -Recurse -Force repo
     ```

---

### Cách 2: Thực hiện từ bên trong phiên SSH của bandit29
*(Nếu bạn muốn thao tác ngay trên server game)*

1. Tạo thư mục tạm và đi vào đó:
   ```bash
   cd $(mktemp -d)
   ```

2. Clone kho lưu trữ git qua cổng 2220:
   ```bash
   git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo
   ```
   *(Nhập mật khẩu: `Em7eGtqaMySwNFjCpwzzHhLhospOcdt0`).*

3. Đi vào thư mục, kiểm tra và chuyển nhánh:
   ```bash
   cd repo
   git branch -a
   git checkout dev
   cat README.md
   ```

4. Dọn dẹp và thoát:
   ```bash
   cd ..
   rm -rf repo
   exit
   ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 30

```text
Password bandit30: [jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX]
```
