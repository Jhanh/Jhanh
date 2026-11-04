# Level 2 -> Level 3

The password for the next level is stored in a file called *--spaces in this filename--* located in the home directory

Commands you may need to solve this level:
`ls`, `cd`, `cat`, `file`, `du`, `find`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 1)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit2`
- **Password**: `PK8fYLZg2hnHSz83plBL1iEPKdD3QToB`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 2

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 2

- **Thử thách**: Khi bạn gõ lệnh `ls`, bạn sẽ thấy tên file cần đọc là:
  `--spaces in this filename--`

- **Vấn đề**:
  Tập tin này kết hợp cả 2 đặc điểm đặc biệt:
  1. **Tên file có chứa các khoảng trắng (spaces)**: Trong Linux, khoảng trắng được dùng để phân tách các tham số, nên ta cần bọc tên file trong cặp dấu ngoặc kép `""`.
  2. **Tên file bắt đầu bằng hai dấu gạch ngang (`--`)**: Trong Linux, mọi chuỗi bắt đầu bằng dấu gạch ngang đều bị hiểu là cờ tùy chọn (option/flag). Vì vậy, nếu chỉ dùng `cat "--spaces in this filename--"`, lệnh vẫn sẽ hiểu lầm đây là một cờ tham số lạ và báo lỗi.

- **Cách xử lý tên file có cả khoảng trắng và bắt đầu bằng dấu gạch ngang**:
  - **Cách 1**: Dùng đường dẫn tương đối (Thêm `./` ở đầu tên file):
    Ký hiệu `./` có nghĩa là "tại thư mục hiện hành", giúp lệnh nhận diện chắc chắn đây là đường dẫn tập tin chứ không phải cờ tham số.
    - Cú pháp: `cat ./"--spaces in this filename--"`
  - **Cách 2**: Dùng ký hiệu kết thúc tham số (`--`):
    Ký hiệu `--` đứng độc lập thông báo cho câu lệnh biết đã hết phần tùy chọn, mọi thứ theo sau dấu này đều là tên file.
    - Cú pháp: `cat -- "--spaces in this filename--"`
  - **Mẹo dùng phím TAB**:
    Gõ: `cat ./-` rồi nhấn phím **TAB** để terminal tự động hoàn thành tên file.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 3

- **Bước 1**: Liệt kê các file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: `--spaces in this filename--`

- **Bước 2**: Đọc file bằng đường dẫn tương đối:
  ```bash
  cat ./"--spaces in this filename--"
  ```
  *(Cách khác tương đương: `cat -- "--spaces in this filename--"`)*

  Màn hình sẽ in ra chuỗi mật khẩu tiếp theo, đó chính là mật khẩu của bandit3!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 3

```text
Password bandit3: [7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME]
```
