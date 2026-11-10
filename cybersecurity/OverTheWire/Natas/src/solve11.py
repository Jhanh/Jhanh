import base64

# Dữ liệu thu thập từ Natas 11
default_data = b'{"showpassword":"no","bgcolor":"#ffffff"}'
cookie_b64 = "EGAgHwQ1IxYYMSQYGSZxTUksPFVHYDEQCC0/GBlgaVVIJDURDSQ1VRY="
cookie_raw = base64.b64decode(cookie_b64)

# 1. Tìm khóa XOR (Key = Plaintext XOR Ciphertext)
key = bytes([p ^ c for p, c in zip(default_data, cookie_raw)])[:4]
print(f"[+] Key tim duoc: {key.decode()}")

# 2. Tạo cookie mới với quyền hiển thị mật khẩu ("showpassword":"yes")
target_data = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
forged_bytes = bytes([target_data[i] ^ key[i % len(key)] for i in range(len(target_data))])
forged_cookie = base64.b64encode(forged_bytes).decode()
print(f"[+] Cookie gia mao: {forged_cookie}")
