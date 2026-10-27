import base64

def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def b64_encode(text):
    return base64.b64encode(text.encode()).decode()

def b64_decode(text):
    return base64.b64decode(text.encode()).decode()

if __name__ == "__main__":
    print("凯撒加密 (hello, shift 3):", caesar_encrypt("hello", 3))
    print("Base64 编码 (hello):", b64_encode("hello"))
    print("Base64 解码 (aGVsbG8=):", b64_decode("aGVsbG8="))
