from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.core.security import verify_password
from app.models.user import User


def create_user(
    db: Session,
    full_name: str,
    email: str,
    password: str,
) -> User:
    user = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    db: Session,
    email: str,
    password: str,
):
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    print("\n========== LOGIN DEBUG ==========")
    print(f"Email received: {repr(email)}")
    print(f"Password received: {repr(password)}")

    if not user:
        print("User not found.")
        print("=================================\n")
        return None

    print(f"Database email: {user.email}")
    print(f"Stored hash: {user.password_hash}")

    result = verify_password(
        password,
        user.password_hash,
    )

    print(f"Password verified: {result}")
    print("=================================\n")

    if not result:
        return None

    return user