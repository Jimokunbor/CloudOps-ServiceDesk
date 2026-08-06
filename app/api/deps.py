from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db


def get_current_db(
    db: Session = Depends(get_db),
):
    return db