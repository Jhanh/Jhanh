# Level 5 -> Level 6

The password for the next level is stored in a file somewhere under the *inhere* directory and has all of the following properties:
- human-readable
- 1033 bytes in size
- not executable

Commands you may need to solve this level:
`ls`, `cd`, `cat`, `file`, `du`, `find`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 4)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit5`
- **Password**: `6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 5

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 5

- **Thử thách**: Trong thư mục `inhere` có hàng chục thư mục con (`maybehere00` đến `maybehere19`) và chứa rất nhiều file rác. Việc tự mò thủ công từng thư mục là bất khả thi.
- **Các tiêu chí của file cần tìm**:
  1. Là văn bản con người đọc được (`human-readable`).
  2. Kích thước chính xác: **1033 bytes**.
  3. Không có quyền thực thi (`not executable`).

- **Lệnh mới - `find` (Công cụ tìm kiếm mạnh mẽ trong Linux)**:
  - Cú pháp cơ bản: `find <vị_trí_tìm> <các_tiêu_chí>`
  - Các bộ lọc (filter) cực hay của lệnh `find`:
    - `-type f`: Chỉ tìm tập tin thông thường (file), bỏ qua thư mục.
    - `-size 1033c`: Tìm file có kích thước chính xác 1033 bytes (ký tự `c` đại diện cho bytes).
    - `! -executable`: Ký hiệu `!` mang ý nghĩa phủ định (NOT), tức là file không thể chạy/thực thi.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 6

- **Bước 1**: Di chuyển vào thư mục `inhere`:
  ```bash
  cd inhere
  ```

- **Bước 2**: Sử dụng lệnh `find` để lọc file theo đúng tiêu chí:
  ```bash
  find . -type f -size 1033c ! -executable
  ```
  *(Hoặc lệnh rút gọn nhanh: `find . -size 1033c`)*

  *Kết quả*: Hệ thống sẽ tự động rà quét tất cả các thư mục con và in ra đường dẫn duy nhất của file cần tìm (ví dụ: `./maybehere07/.file2`).

- **Bước 3**: Đọc nội dung file vừa tìm được:
  ```bash
  cat <đường_dẫn_file_tìm_thấy>
  ```
  *(Ví dụ nếu tìm được `./maybehere07/.file2`: `cat ./maybehere07/.file2`)*

Màn hình sẽ in ra chuỗi mật khẩu tiếp theo, đó chính là mật khẩu của bandit6!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 6

```text
Password bandit6: [pXa26xhMWaC2SvDotA4r9EgZkulOeSBW]
```
