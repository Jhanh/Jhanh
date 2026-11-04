# Level 13 -> Level 14

The password for the next level is stored in */etc/bandit_pass/bandit14 and can only be read by user bandit14*. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.
If you need help with this level: a hint file can be found in the home directory.
Make sure to read the error messages as they are informative.

Commands you may need to solve this level:
`ssh`, `telnet`, `nc`, `openssl`, `s_client`, `nmap`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 12)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit13`
- **Password**: `qQYQiHOBPR8zR61qxYqX45quvihF2uzk`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 13

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit13@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 13

- **Thử thách**: Màn này bạn không có mật khẩu dạng chữ, mà được cung cấp một file khóa riêng tư: `sshkey.private` (kèm theo một file `HINT`).
- Mật khẩu của `bandit14` nằm tại `/etc/bandit_pass/bandit14`, nhưng file này chỉ cho phép tài khoản `bandit14` đọc.
- **Quy trình thực hiện**: Bạn sẽ copy nội dung khóa `sshkey.private` về máy cá nhân của mình, sau đó đăng xuất (`exit`) khỏi `bandit13`, rồi dùng file khóa này để SSH đăng nhập trực tiếp vào `bandit14` từ máy của bạn.

- **Khái niệm Khóa SSH (SSH Private Key)**:
  - Thay vì dùng mật khẩu thông thường, người ta dùng cặp khóa bảo mật (Public/Private Key). File `sshkey.private` chính là "chìa khóa số" để mở cửa vào tài khoản `bandit14`.
  - Tham số `-i` (Identity file): Dùng để chỉ định file khóa riêng tư khi kết nối SSH.
  - Cú pháp: `ssh -i <file_khóa> bandit14@bandit.labs.overthewire.org -p 2220`

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 14

- **Bước 1**: Kiểm tra các file có trong thư mục của bandit13:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: file `HINT` và file `sshkey.private`.

- **Bước 2**: Đọc và sao chép toàn bộ nội dung của khóa SSH:
  ```bash
  cat sshkey.private
  ```
  *Hành động*: Bôi đen và copy toàn bộ nội dung khóa hiển thị trên màn hình (từ dòng `-----BEGIN OPENSSH PRIVATE KEY-----` cho đến hết dòng `-----END OPENSSH PRIVATE KEY-----`).

- **Bước 3**: Tạo file lưu khóa trên máy tính của bạn:
  Tạo một file mới tên là `bandit14.key` (ví dụ lưu ngay trong thư mục `j4f/overthewire/bandit/`) và dán toàn bộ đoạn mã vừa copy vào file này.

  > **Lưu ý xử lý lỗi quyền khóa trên Windows (Permissions too open):**
  > Trên Windows, OpenSSH bắt buộc file khóa cá nhân chỉ có một mình tài khoản của bạn được đọc. Nếu không, khi chạy SSH bạn sẽ gặp cảnh báo:
  > `WARNING: UNPROTECTED PRIVATE KEY FILE! Permissions for 'bandit14.key' are too open` và hệ thống sẽ đòi mật khẩu.
  > Để khắc phục, chỉ cần mở PowerShell tại thư mục chứa file và chạy 2 câu lệnh:
  > ```powershell
  > icacls .\bandit14.key /inheritance:r
  > icacls .\bandit14.key /grant:r "$($env:USERNAME):(R)"
  > ```

- **Bước 4**: Thoát khỏi phiên làm việc của bandit13:
  ```bash
  exit
  ```

- **Bước 5**: Dùng file khóa vừa tạo để đăng nhập vào bandit14 từ Terminal máy bạn:
  ```bash
  ssh -i bandit14.key bandit14@bandit.labs.overthewire.org -p 2220
  ```
  *(Nếu terminal đang đứng ở thư mục khác, hãy truyền đúng đường dẫn tới file `bandit14.key`).*

- **Bước 6**: Sau khi đã vào được tài khoản bandit14 (`bandit14@bandit:~$`), hãy đọc mật khẩu:
  ```bash
  cat /etc/bandit_pass/bandit14
  ```

Màn hình sẽ in ra chuỗi mật khẩu chính thức của bandit14!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 14

```text
Password bandit14: [aaWecNkG4FhxJQxz07uiwzVP6bJiYS65]
```
