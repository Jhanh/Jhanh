# Level 6 -> Level 7

The password for the next level is stored *somewhere on the server* and has all of the following properties:
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

Commands you may need to solve this level:
`ls`, `cd`, `cat`, `file`, `du`, `find`, `grep`

---

## 1. THÔNG TIN KẾT NỐI (DÙNG PASSWORD TÌM ĐƯỢC TỪ BANDIT 5)

- **Host**: `bandit.labs.overthewire.org`
- **Port**: `2220`
- **Username**: `bandit6`
- **Password**: `pXa26xhMWaC2SvDotA4r9EgZkulOeSBW`

---

## 2. CÂU LỆNH KẾT NỐI SSH VÀO BANDIT 6

Mở Terminal / PowerShell và chạy:

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

---

## 3. KIẾN THỨC MỚI & THỬ THÁCH CỦA LEVEL 6

- **Thử thách**: File mật khẩu không nằm trong thư mục cá nhân mà nằm "ở một nơi nào đó trên toàn bộ máy chủ" (somewhere on the server). Do đó, ta phải tìm kiếm bắt đầu từ thư mục gốc `/` (root directory).
- **Các tiêu chí của file cần tìm**:
  1. Thuộc sở hữu của người dùng (user): `bandit7`.
  2. Thuộc sở hữu của nhóm (group): `bandit6`.
  3. Kích thước chính xác: **33 bytes**.

- **Các tham số lọc quyền sở hữu của lệnh `find`**:
  - `/`: Bắt đầu tìm kiếm từ thư mục gốc cao nhất của hệ điều hành.
  - `-user bandit7`: Lọc các file thuộc sở hữu của user `bandit7`.
  - `-group bandit6`: Lọc các file thuộc sở hữu của group `bandit6`.
  - `-size 33c`: File có kích thước đúng 33 bytes (`c` = bytes).

- **Khái niệm then chốt: Chuyển hướng lỗi với `2>/dev/null`**:
  - Vì quét toàn bộ hệ thống `/` bằng quyền user thường, bạn sẽ gặp hàng trăm dòng lỗi `Permission denied` (không có quyền truy cập vào các thư mục bảo mật của hệ thống), làm tràn ngập màn hình và che lấp kết quả đúng.
  - Trong Linux:
    - Luồng `1`: Dữ liệu đầu ra chuẩn (Standard Output - kết quả tìm thấy).
    - Luồng `2`: Dữ liệu lỗi chuẩn (Standard Error - thông báo lỗi).
    - `/dev/null`: "Hố đen" trong Linux, ném bất cứ thứ gì vào đây đều biến mất.
  - Cú pháp `2>/dev/null`: Bảo hệ thống ném toàn bộ lỗi (luồng 2) vào "hố đen", chỉ giữ lại kết quả hợp lệ (luồng 1) hiển thị trên màn hình.

---

## 4. CÁC BƯỚC THỰC HIỆN ĐỂ LẤY PASSWORD LEVEL 7

- **Bước 1**: Chạy lệnh tìm kiếm trên toàn hệ thống kèm lọc lỗi:
  ```bash
  find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
  ```
  *Kết quả*: Hệ thống sẽ lọc sạch mọi thông báo rác và chỉ in ra đúng 1 đường dẫn file thỏa mãn (ví dụ: `/var/lib/dpkg/info/bandit7.password`).

- **Bước 2**: Đọc file vừa tìm thấy:
  ```bash
  cat <đường_dẫn_file_tìm_được>
  ```
  *(Ví dụ: `cat /var/lib/dpkg/info/bandit7.password`)*

Màn hình sẽ in ra chuỗi mật khẩu tiếp theo, đó chính là mật khẩu của bandit7!

---

## 5. KẾT QUẢ / MẬT KHẨU LEVEL 7

```text
Password bandit7: [Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3]
```
