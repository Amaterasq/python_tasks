import simplecrypt as sc


with open("encrypted.bin", "rb") as encrypted_file:
    encrypted = encrypted_file.read()

with open("passwords.txt", "r") as passwords_file:
    passwords = [line.rstrip() for line in passwords_file]


decrypted = []
for password in passwords:
    try:
        decrypted.append(sc.decrypt(password, encrypted))
    except sc.DecryptionException:
        continue


print(*decrypted)
# [b'Alice loves Bob']