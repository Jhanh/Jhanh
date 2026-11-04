# Level 3 -> Level 4

The password for the next level is stored in a hidden file in the *inhere* directory

Commands you may need to solve this level:
`ls`, `cd`, `cat`, `file`, `du`, `find`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 2)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit3`
- **Password**: `7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 3

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 3

- **Thử thách**: Mật khẩu nằm trong một "file ẩn" (hidden file) đặt bên trong thư mục có tên là "inhere".

- **Kiến thức mới**:
  1. **Lệnh di chuyển thư mục - `cd` (Change Directory)**:
     - Dùng để đi vào trong một thư mục con.
     - Cú pháp: `cd <tên_thư_mục>` (Ví dụ: `cd inhere`)

  2. **Khái niệm File ẩn trong Linux**:
     - Trong Linux, bất kỳ tập tin hoặc thư mục nào có tên bắt đầu bằng dấu chấm `.` (ví dụ: `.hidden`, `.bashrc`) đều được hệ thống mặc định là "tập tin ẩn".
     - Nếu bạn chỉ gõ lệnh `ls` thông thường, Linux sẽ KHÔNG hiển thị file ẩn (bạn sẽ thấy thư mục trống trơn).

  3. **Cách xem tất cả các file bao gồm cả file ẩn**:
     - Dùng tham số `-a` (viết tắt của "all"):
       ```bash
       ls -a
       ```
     - Hoặc xem chi tiết quyền/kích thước bằng:
       ```bash
       ls -la
       ```
       *(với `l` = long listing, `a` = all)*

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 4

- **Bước 1**: Liệt kê các mục trong thư mục hiện tại:
  ```bash
  ls
  ```
  *Kết quả hiển thị thư mục*: `inhere`

- **Bước 2**: Di chuyển vào trong thư mục inhere:
  ```bash
  cd inhere
  ```

- **Bước 3**: Liệt kê tất cả các file (kể cả file ẩn):
  ```bash
  ls -a
  ```
  *Kết quả hiển thị*: `.  ..  ...Hiding-From-You`

  *(Giải thích thêm:*
  - *Ký hiệu `.` là thư mục hiện tại.*
  - *Ký hiệu `..` là thư mục cha phía trên.*
  - *`...Hiding-From-You` chính là file ẩn chứa mật khẩu!)*

- **Bước 4**: Đọc nội dung file ẩn:
  ```bash
  cat ...Hiding-From-You
  ```
  *(hoặc gõ: `cat ...` rồi nhấn phím **TAB** để terminal tự động điền)*

  Màn hình sẽ in ra chuỗi mật khẩu tiếp theo, đó chính là mật khẩu của bandit4!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 4

```text
Password bandit4: [xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq]
```
