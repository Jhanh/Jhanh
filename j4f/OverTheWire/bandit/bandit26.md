# Level 26 -> Level 27

Good job getting a shell! Now hurry and grab the password for bandit27!

Commands you may need to solve this level:
`ls`, `id`, `cat`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD / KHÓA TÌM ĐƯỢC TỪ LEVEL 25)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit26`
- **Password**: `jHdv2ELQhT22BkprMNDjybZDAkw1zeBJ`
- **File khóa SSH**: `bandit26.key` (đã lưu ở thư mục hiện tại)

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 26

Mở cửa sổ Command Prompt (`cmd`) đã thu nhỏ chiều cao (4 - 5 dòng chữ) và chạy:

```cmd
ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, hoặc nếu không dùng key, bạn có thể chạy `ssh bandit26@bandit.labs.overthewire.org -p 2220` rồi nhập password: `jHdv2ELQhT22BkprMNDjybZDAkw1zeBJ`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 26

1. **Vẫn bị vướng Shell đặc biệt (`/usr/bin/showtext`)**:
   - Khi kết nối SSH vào tài khoản `bandit26`, shell mặc định của user này vẫn là chương trình `showtext` (chạy `more ~/text.txt` rồi tự động ngắt kết nối).
   - Do đó, ta vẫn phải dùng cửa sổ **Command Prompt (`cmd`) có chiều cao cực nhỏ (4 - 5 dòng)** để kích hoạt `more`, sau đó bấm `v` để vào trình soạn thảo `vi`.

2. **Kỹ thuật Breakout Shell từ `vi` (Vim Escape)**:
   - Trong bài 25, ta dùng `:e /etc/bandit_pass/bandit26` ngay trong `vi` để đọc file.
   - Nhưng ở Level 26, để lấy được mật khẩu của `bandit27`, ta cần thực thi một chương trình có quyền SUID mang tên `bandit27-do`.
   - Vì vậy, ta phải biến trình soạn thảo `vi` thành một terminal `bash` đầy đủ quyền lực bằng cách cấu hình shell bên trong `vi`:
     - `:set shell=/bin/bash`
     - `:shell`
   - Lúc này, ta sẽ thoát ra được một giao diện dòng lệnh `bash` bình thường với tư cách là người dùng `bandit26`!

3. **SUID Binary (`./bandit27-do`)**:
   - Khi đã có shell `bash`, trong thư mục home của `bandit26` có sẵn file thực thi `./bandit27-do` thuộc quyền sở hữu của `bandit27`.
   - File này hoạt động tương tự như `./bandit20-do` ở bài 19: nó cho phép ta chạy bất kỳ câu lệnh nào với quyền của `bandit27`.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 27

### Bước 1: Mở Command Prompt (cmd) và thu nhỏ cửa sổ
*(Thực hiện trên máy tính của bạn)*

1. Mở cửa sổ **Command Prompt (`cmd`)** riêng biệt của Windows (không dùng PowerShell hay terminal trong VS Code).
2. Di chuyển đến thư mục chứa file `bandit26.key` trên máy tính của bạn.
3. Dùng chuột nắm mép trên/dưới của cửa sổ `cmd` kéo **thu nhỏ chiều cao lại thật lùn** (chỉ còn khoảng 4 đến 5 dòng chữ).
4. Chạy lệnh SSH kết nối bằng file khóa `bandit26.key`:
   ```cmd
   ssh -i bandit26.key bandit26@bandit.labs.overthewire.org -p 2220
   ```
5. Màn hình dừng lại ở dòng:
   ```text
   --More--(xx%)
   ```

---

### Bước 2: Nhảy vào trình soạn thảo `vi`
*(Thực hiện khi đang dừng ở `--More--`)*

Bấm phím:
```text
v
```
*(Giao diện sẽ lập tức chuyển sang trình soạn thảo `vi`).*

---

### Bước 3: Thoát khỏi `vi` để lấy Bash Shell
*(Thực hiện trong giao diện `vi`)*

Lần lượt gõ 2 lệnh sau (mỗi lệnh đều bắt đầu bằng dấu hai chấm `:` và kết thúc bằng phím **Enter**):

1. Đặt shell mặc định của vi là `bash`:
   ```text
   :set shell=/bin/bash
   ```
   *(Nhấn **Enter**)*

2. Khởi chạy shell:
   ```text
   :shell
   ```
   *(Nhấn **Enter**)*

Ngay lập tức, bạn sẽ thấy dấu nhắc lệnh quen thuộc xuất hiện:
```text
bandit26@bandit:~$
```
*(Bây giờ bạn có thể phóng to cửa sổ CMD ra bình thường để nhìn cho rõ).*

---

### Bước 4: Kiểm tra file và lấy mật khẩu `bandit27`
*(Thực hiện trên terminal SSH của `bandit26`)*

1. Kiểm tra danh sách các file trong thư mục:
   ```bash
   ls -la
   ```
   *Bạn sẽ thấy file `bandit27-do` có quyền `rwsr-xr-x` và được sở hữu bởi `bandit27`.*

2. Dùng `./bandit27-do` để đọc file mật khẩu của `bandit27`:
   ```bash
   ./bandit27-do cat /etc/bandit_pass/bandit27
   ```

3. Màn hình sẽ in ra mật khẩu của Level 27!

---

### Bước 5: Cách thoát khỏi kết nối
*(Thực hiện sau khi đã lưu mật khẩu)*

1. Thoát khỏi shell `bash` để quay lại `vi`:
   ```bash
   exit
   ```
2. Trong `vi`, gõ lệnh thoát an toàn:
   ```text
   :qa
   ```
   *(Nhấn **Enter** để ngắt kết nối SSH).*

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 27

```text
Password bandit27: [STJLJBRRphMxKB392CT4iOr5CbzPU9ER]
```
