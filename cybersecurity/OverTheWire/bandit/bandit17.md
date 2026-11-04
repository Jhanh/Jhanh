# Level 17 -> Level 18

There are 2 files in the homedirectory: *passwords.old and passwords.new*. The password for the next level is in *passwords.new* and is the only line that has been changed between *passwords.old and passwords.new*

NOTE: if you have solved this level and see "Byebye!" when trying to log into bandit18, this is related to the next level, bandit18 -> bandit19

Commands you may need to solve this level:
`cat`, `grep`, `ls`, `diff`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 16)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit17`
- **Password**: `pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 17

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit17@bandit.labs.overthewire.org -p 2220
```
*(Khi được hỏi, nhập password: `pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2`. Hoặc bạn có thể dùng file khóa đã lưu: `ssh -i bandit17.key bandit17@bandit.labs.overthewire.org -p 2220`).*

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 17

- **Thử thách**: Trong thư mục có 2 file: `passwords.old` (mật khẩu cũ) và `passwords.new` (mật khẩu mới). Hai file này chứa rất nhiều dòng văn bản gần như giống nhau hoàn toàn, chỉ có **duy nhất 1 dòng bị thay đổi** trong `passwords.new`, và dòng đó chính là mật khẩu của `bandit18`.

- **Lệnh mới cốt lõi của lập trình viên - `diff` (So sánh sự khác biệt giữa hai tập tin)**:
  - `diff` (viết tắt của "difference") là công cụ chuyên dùng để so sánh hai tệp văn bản theo từng dòng một (đây chính là nền tảng cốt lõi của lệnh `git diff` trong Git).
  - Cú pháp cơ bản:
    ```bash
    diff <file_cũ> <file_mới>
    ```
  - Cách đọc kết quả của `diff`:
    - Ký hiệu `<`: Nội dung của file cũ (`passwords.old`).
    - Ký hiệu `---`: Vạch ngăn cách giữa 2 file.
    - Ký hiệu `>`: Nội dung đã được thay đổi trong file mới (`passwords.new`).
    👉 Chuỗi ký tự nằm sau dấu `>` chính là mật khẩu bạn cần tìm!

- **Mẹo nâng cao (Định dạng Unified Diff)**:
  - Bạn có thể thêm cờ `-u`:
    ```bash
    diff -u passwords.old passwords.new
    ```
  - Dòng có dấu `-` là dòng cũ bị bỏ, dòng có dấu `+` là dòng mới được thêm vào.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 18

- **Bước 1**: Liệt kê các file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: `passwords.new`  `passwords.old`

- **Bước 2**: So sánh hai file để tìm dòng bị thay đổi:
  ```bash
  diff passwords.old passwords.new
  ```
  *Kết quả*: Màn hình sẽ hiển thị sự khác biệt:
  ```text
  < <dòng_cũ_trong_passwords.old>
  ---
  > <mật_khẩu_mới_của_bandit18>
  ```

Chuỗi ký tự nằm sau dấu `>` chính là mật khẩu của bandit18!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 18

```text
Password bandit18: [OQxXZjELndr90zuhOTDYBEomI0SZITXI]
```
