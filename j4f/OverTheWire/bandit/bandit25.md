# Level 25 -> Level 26

Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

NOTE: if you’re a Windows user and typically use Powershell to ssh into bandit: Powershell is known to cause issues with the intended solution to this level. You should use command prompt instead.

Commands you may need to solve this level:
`ssh`, `cat`, `more`, `vi`, `ls`, `id`, `pwd`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 24)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit25`
- **Password**: `SoHfqMOEqIX2IYKVciZxvgpR9a2Djx4P`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 25

Mở Terminal / PowerShell trên máy bạn và chạy:

```bash
ssh bandit25@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 25

- **Thử thách**: Shell đăng nhập của `bandit26` không phải là `bash` mà là `/usr/bin/showtext` (chạy lệnh `more ~/text.txt` rồi lập tức thoát `exit 0`). Nếu mở cửa sổ lớn, `more` in hết chữ rồi tự thoát, làm đóng kết nối SSH ngay lập tức.
- **Lưu ý quan trọng về localhost**: Phiên bản mới của OverTheWire chặn kết nối SSH nội bộ từ máy chủ sang `localhost:2220` (báo lỗi `no authentication methods enabled`). Do đó, ta cần lấy khóa `bandit26.sshkey` về máy tính laptop và kết nối từ bên ngoài vào `bandit.labs.overthewire.org`.
- **Cơ chế thoát khỏi `more`**: Khi cửa sổ terminal thật lùn (chiều cao chỉ 4 - 5 dòng), `more` không in hết file được nên buộc phải dừng lại chờ ở dòng `--More--(xx%)`. Từ đây, bấm phím `v` sẽ mở ra trình soạn thảo `vi` để ta xem file mật khẩu.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 26

### Bước 1: Lấy nội dung khóa SSH
Đọc và sao chép toàn bộ nội dung của khóa:
```bash
cat bandit26.sshkey
```
*(Bôi đen và copy toàn bộ đoạn mã từ `-----BEGIN...` đến `-----END...`).*

---

### Bước 2: Lưu khóa và phân quyền
1. Tạo một file mới tên là `bandit26.key` và dán nội dung khóa vừa copy vào đó.
2. Mở PowerShell tại thư mục đó và chạy 2 lệnh khóa quyền file:
   ```powershell
   icacls .\bandit26.key /inheritance:r
   icacls .\bandit26.key /grant:r "$($env:USERNAME):(R)"
   ```

---

### Bước 3: Thu nhỏ cửa sổ và kết nối vào bandit26
1. Mở cửa sổ **Command Prompt (`cmd`)** riêng biệt của Windows (không dùng VS Code).
2. Dùng chuột kéo chiều cao cửa sổ `cmd` **thu nhỏ lại thật lùn** (chỉ để chiều cao khoảng 4 đến 5 dòng chữ).
3. Chạy lệnh SSH từ máy bạn đến server:
   ```cmd
   ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
   ```
4. *Kết quả*: Vì cửa sổ cực lùn, màn hình sẽ dừng lại ở dòng:
   ```text
   --More--(xx%)
   ```

---

### Bước 4: Bấm phím `v` để vào `vi`
Ngay khi thấy dòng chữ `--More--`, bấm phím:
```text
v
```
*(Màn hình sẽ lập tức chuyển sang trình soạn thảo `vi`).*

---

### Bước 5: Đọc mật khẩu
Trong giao diện của `vi`, bạn gõ chuẩn xác lệnh sau:
```text
:e /etc/bandit_pass/bandit26
```
*(Nhớ có dấu hai chấm `:` ở đầu)* rồi nhấn **Enter**.

Màn hình sẽ hiển thị nội dung file chứa mật khẩu chính thức của bandit26!

---

### Bước 6: Cách thoát khỏi chế độ `vi`
Sau khi đã ghi nhớ/lưu mật khẩu xong, để thoát hoàn toàn khỏi trình soạn thảo `vi` (đóng tất cả các file đang mở), bạn gõ theo đúng hướng dẫn trên màn hình:
```text
:qa
```
*(Gồm dấu hai chấm `:`, chữ `qa` viết tắt của **quit all** - đóng toàn bộ các tập tin đang mở)* rồi nhấn **Enter**.

*(Mẹo thêm: Nếu lỡ tay gõ linh tinh khiến vi hỏi lưu, bạn có thể gõ `:qa!` để ép thoát mà không lưu).*

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 26

```text
Password bandit26: [jHdv2ELQhT22BkprMNDjybZDAkw1zeBJ]
```
