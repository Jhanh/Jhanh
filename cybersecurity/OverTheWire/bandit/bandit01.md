# Level 1 -> Level 2

The password for the next level is stored in a file called - located in the home directory

Commands you may need to solve this level:
`ls`, `cd`, `cat`, `file`, `du`, `find`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 0)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit1`
- **Password**: `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 1

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 1

- **Thử thách**: Khi bạn gõ lệnh `ls`, bạn sẽ thấy tên file cần đọc là dấu trừ: `-`
- **Vấn đề**:
  Nếu bạn gõ `cat -`, lệnh sẽ bị đơ/chờ đợi! Vì trong Linux, ký hiệu `-` thường quy ước là đọc từ bàn phím (Standard Input - stdin) hoặc báo hiệu một tham số tùy chọn (option flag), chứ hệ thống không hiểu đó là tên file.
- **Cách xử lý tên file đặc biệt bắt đầu bằng dấu gạch ngang**:
  - Dùng đường dẫn tương đối (Relative Path): thêm `./` ở phía trước tên file. Ký hiệu `./` có nghĩa là: "ngay tại thư mục hiện hành này".

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 2

- **Bước 1**: Liệt kê các file trong thư mục:
  ```bash
  ls
  ```
  *Kết quả hiển thị*: `-`

- **Bước 2**: Đọc file có tên là dấu gạch ngang:
  ```bash
  cat ./-
  ```
  *(Cách khác tương đương: `cat < -` hoặc `cat -- -`)*

  Màn hình sẽ in ra chuỗi mật khẩu tiếp theo, đó chính là mật khẩu của bandit2!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 2

```text
Password bandit2: [PK8fYLZg2hnHSz83plBL1iEPKdD3QToB]
```
