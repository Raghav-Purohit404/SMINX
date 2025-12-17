from app.utils.hashing import hash_password, verify_password

password = "secure123"

hashed, salt = hash_password(password)

print("Hashed password:", hashed)
print("Salt:", salt)

print("Correct password check:",
      verify_password("secure123", hashed, salt))

print("Wrong password check:",
      verify_password("wrongpass", hashed, salt))
