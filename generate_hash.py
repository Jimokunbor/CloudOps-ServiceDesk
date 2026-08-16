from app.core.security import hash_password
from app.core.security import verify_password

password = "Password123"

generated_hash = hash_password(password)

print("\nGenerated hash:")
print(generated_hash)

print("\nGenerated hash length:")
print(len(generated_hash))

print("\nStored hash:")
stored_hash = "$2b$12$2990gvLZXe12vSE1cch2AuPKLeTYRIreTfdmygegZJ00HJSo3dtSy"
print(stored_hash)

print("\nStored hash length:")
print(len(stored_hash))

print("\nVerify generated hash:")
print(
    verify_password(
        password,
        generated_hash,
    )
)

print("\nVerify stored hash:")
print(
    verify_password(
        password,
        stored_hash,
    )
)