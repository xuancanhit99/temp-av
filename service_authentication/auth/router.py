from datetime import timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .jwt import create_access_token
from auth.schemas import User

router = APIRouter(
    tags=['auth']
)

users = [
    User(
        username='ledhcg',
        password='123456789',
        email='user@ledinhcuong.com',
        role='user',
    ),
    User(
        username='ledhcg_admin',
        password='123456789',
        email='admin@ledinhcuong.com',
        role='admin',
    ),
]


@router.post('/login')
def login(
        request: OAuth2PasswordRequestForm = Depends(),
):
    user = None
    for u in users:
        if u.username == request.username:
            user = u
            break

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')

    if user.password != request.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    access_token = create_access_token(
        data={"email": user.email, "roles": user.role})

    return {"access_token": access_token, "token_type": "bearer"}
