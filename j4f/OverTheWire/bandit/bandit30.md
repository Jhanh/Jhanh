# Level 30 -> Level 31

There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo via the port 2220. The password for the user bandit30-git is the same as for the user bandit30.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

Commands you may need to solve this level:
`git`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ LEVEL 29)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit30`
- **Password**: `jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 30

Mở Terminal / PowerShell trên máy bạn và chạy:

```bash
ssh bandit30@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, nhập password: `jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 30

1. **Khái niệm Thẻ đánh dấu trong Git (Git Tags)**:
   - Trong Git, ngoài nhánh (`branch`) và lịch sử commit (`log`), ta còn có **Tag (thẻ)**.
   - Thẻ thường được dùng để đánh dấu các mốc quan trọng trong lịch sử dự án (ví dụ phát hành phiên bản `v1.0.0`, `v2.0.0`) hoặc đính kèm các chú thích quan trọng.
   - Có 2 loại tag:
     - *Lightweight tag*: Chỉ đơn giản là một con trỏ trỏ tới một commit cụ thể.
     - *Annotated tag*: Lưu đầy đủ thông tin người tạo, ngày giờ, thông điệp (tag message) và có thể chứa dữ liệu bí mật.

2. **Thử thách của bài 30**:
   - Khi clone repo về, bạn kiểm tra file `README.md` chỉ thấy thông báo trống rỗng ("just an empty file... muahaha").
   - Lịch sử `git log` cũng không thấy thông tin nhạy cảm nào, và `git branch -a` cũng chỉ có duy nhất một nhánh `master`.
   - Mật khẩu thực chất đã được cất giấu trong một **Git Tag** ẩn.

3. **Các lệnh Git quan trọng khi làm việc với Tag**:
   - `git tag`: Liệt kê tất cả các thẻ tag có trong repository.
   - `git show <tên_tag>`: Xem chi tiết thông điệp và nội dung đính kèm bên trong tag.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 31

### Cách 1: Thực hiện trực tiếp trên máy tính của bạn (Khuyến nghị)
*(Thực hiện trên PowerShell tại máy của bạn)*

1. Mở PowerShell tại thư mục làm việc của bạn trên máy tính.

2. Clone kho lưu trữ git về máy:
   ```powershell
   git clone ssh://bandit30-git@bandit.labs.overthewire.org:2220/home/bandit30-git/repo
   ```
   - Xác nhận `yes` nếu được hỏi fingerprint.
   - Nhập mật khẩu của `bandit30-git` (chính là mật khẩu của `bandit30`):
     ```text
     jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX
     ```

3. Đi vào thư mục vừa clone và kiểm tra các thẻ tag:
   ```powershell
   cd repo
   git tag
   ```
   *Bạn sẽ thấy xuất hiện một tag có tên là: `secret`.*

4. Xem chi tiết nội dung của tag `secret`:
   ```powershell
   git show secret
   ```
   *Màn hình sẽ hiển thị thông tin và in ra mật khẩu chính thức của Level 31!*

5. **Dọn dẹp thư mục sau khi hoàn thành**:
   - Sau khi ghi lại mật khẩu, lùi ra ngoài và xóa thư mục `repo`:
     ```powershell
     cd ..
     Remove-Item -Recurse -Force repo
     ```

---

### Cách 2: Thực hiện từ bên trong phiên SSH của bandit30
*(Nếu bạn muốn thao tác ngay trên server game)*

1. Tạo thư mục tạm và đi vào đó:
   ```bash
   cd $(mktemp -d)
   ```

2. Clone kho lưu trữ git qua cổng 2220:
   ```bash
   git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
   ```
   *(Nhập mật khẩu: `jq9Dfg2rXsfYsWMgFuKlXhphjdH7USgX`).*

3. Đi vào thư mục và kiểm tra tag:
   ```bash
   cd repo
   git tag
   git show secret
   ```

4. Dọn dẹp và thoát:
   ```bash
   cd ..
   rm -rf repo
   exit
   ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 31

```text
Password bandit31: [82NkymblpGBYmIXG6ZQ8YldBYstHpfUf]
```
