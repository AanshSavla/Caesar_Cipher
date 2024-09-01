s = input("Enter a plain text:")
key = int(input("Enter a key:"))
ans = ""

# Encryption
for c in s:
    if(c.islower()):
        l = ord(c) - ord("a")
        l = (l + key)%26 + 97
    elif(c.isupper()):
        l = ord(c) - ord('A')
        l = (l + key)%26 + 65
    else:
        l = ord(c)
    ans += chr(l)
print("Encrypted Text:",ans)

s = input("Enter a cipher text:")
key = int(input("Enter a key:"))
ans = ""

# Decryption
for c in s:
    if(c.islower()):
        l = ord(c) - ord("a")
        l = (l - key)%26 + 97
    elif(c.isupper()):
        l = ord(c) - ord('A')
        l = (l - key)%26 + 65
    else:
        l = ord(c)
    ans += chr(l)
print("Decrypted Text:",ans)