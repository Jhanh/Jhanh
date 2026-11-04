# Level 31 -> Level 32

There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo via the port 2220. The password for the user bandit31-git is the same as for the user bandit31.

From your local machine (not the OverTheWire machine!), clone the repository and find the password for the next level. This needs git installed locally on your machine.

Commands you may need to solve this level:
`git`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ LEVEL 30)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit31`
- **Password**: `82NkymblpGBYmIXG6ZQ8YldBYstHpfUf`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 31

Mở Terminal / PowerShell trên máy bạn và chạy:

```bash
ssh bandit31@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, nhập password: `82NkymblpGBYmIXG6ZQ8YldBYstHpfUf`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 31

1. **Thử thách mới - Đẩy mã nguồn lên máy chủ (Git Push)**:
   - Các bài trước ta chỉ tải mã về (`git clone`) và xem lịch sử. Bài này yêu cầu ta tạo một file mới, commit và **push** (đẩy) ngược lên kho từ xa của server.
   - Máy chủ OverTheWire được cài đặt sẵn một **Git Server Hook** (kịch bản tự động chạy khi nhận được commit mới). Hook này sẽ kiểm tra nội dung file bạn gửi lên, nếu thỏa mãn điều kiện thì hook sẽ in ra mật khẩu của `bandit32`.

2. **Vượt qua tệp loại trừ `.gitignore`**:
   - File hướng dẫn `README.md` yêu cầu tạo file `key.txt` chứa nội dung `May I come in?`.
   - Tuy nhiên, trong repo có sẵn file `.gitignore` chứa luật chặn toàn bộ file đuôi `.txt` (`*.txt`). Nếu chỉ chạy `git add key.txt` thông thường, Git sẽ chặn và từ chối thêm file.
   - **Giải pháp**: Dùng cờ `-f` (force - ép buộc) trong lệnh `git add`:
     ```bash
     git add -f key.txt
     ```

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 32

### Cách 1: Thực hiện trực tiếp trên máy tính của bạn (Khuyến nghị)
*(Thực hiện trên PowerShell tại máy của bạn)*

1. Mở PowerShell tại thư mục làm việc của bạn trên máy tính.

2. Clone kho lưu trữ git về máy:
   ```powershell
   git clone ssh://bandit31-git@bandit.labs.overthewire.org:2220/home/bandit31-git/repo
   ```
   - Xác nhận `yes` nếu được hỏi fingerprint.
   - Nhập mật khẩu của `bandit31-git` (chính là mật khẩu của `bandit31`):
     ```text
     82NkymblpGBYmIXG6ZQ8YldBYstHpfUf
     ```

3. Đi vào thư mục vừa clone và đọc yêu cầu trong `README.md`:
   ```powershell
   cd repo
   cat README.md
   ```
   *Yêu cầu:*
   - Tên file: `key.txt`
   - Nội dung: `May I come in?`
   - Nhánh: `master`

4. Tạo file `key.txt` chuẩn định dạng:
   ```powershell
   Set-Content -Path key.txt -Value "May I come in?" -Encoding ascii
   ```

5. Ép Git thêm file `key.txt` (vượt qua bộ lọc của `.gitignore`):
   ```powershell
   git add -f key.txt
   ```

6. Tạo commit lưu thay đổi:
   ```powershell
   git commit -m "Add key.txt"
   ```

7. Push commit lên máy chủ để kích hoạt hook lấy mật khẩu:
   ```powershell
   git push origin master
   ```
   - Khi được hỏi, nhập lại mật khẩu của `bandit31-git`:
     ```text
     82NkymblpGBYmIXG6ZQ8YldBYstHpfUf
     ```
   - Hệ thống phản hồi từ máy chủ các dòng `remote: ...` và in ra mật khẩu của Level 32!

8. **Dọn dẹp thư mục sau khi hoàn thành**:
   - Sau khi ghi lại mật khẩu, lùi ra ngoài và xóa thư mục `repo`:
     ```powershell
     cd ..
     Remove-Item -Recurse -Force repo
     ```

---

### Cách 2: Thực hiện từ bên trong phiên SSH của bandit31
*(Nếu bạn muốn thao tác ngay trên server game)*

1. Tạo thư mục tạm và đi vào đó:
   ```bash
   cd $(mktemp -d)
   ```

2. Clone kho lưu trữ git qua cổng 2220:
   ```bash
   git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
   cd repo
   ```
   *(Nhập mật khẩu: `82NkymblpGBYmIXG6ZQ8YldBYstHpfUf`).*

3. Tạo file, ép add, commit và push:
   ```bash
   echo "May I come in?" > key.txt
   git add -f key.txt
   git commit -m "Add key.txt"
   git push origin master
   ```
   *(Nhập lại mật khẩu: `82NkymblpGBYmIXG6ZQ8YldBYstHpfUf` để nhận mật khẩu của Level 32).*

4. Dọn dẹp và thoát:
   ```bash
   cd ..
   rm -rf repo
   exit
   ```

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 32

```text
Password bandit32: [pWuj5jBQ6IgV0NXwiH6g1pXRF8S1YvbT]
```
