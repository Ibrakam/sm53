from fastapi import APIRouter
from database.userservice import *
from pydantic import BaseModel
from api import result_message

user_router = APIRouter(prefix="/user", tags=["Users API"])


class User(BaseModel):
    name: str
    phone_number: str
    email: str
    password: str
    birthday: str
    user_city: str


@user_router.post("/register_user")
async def register_user_api(user_data: User):
    user_db = dict(user_data)
    result = register_user_db(**user_db)
    result_message(result)


@user_router.post("/login_user")
async def login_user_api(login: str, password: str):
    result = login_user_db(login, password)
    result_message(result)

@user_router.get("/get_profile_info")
@user_router.get("/change_profile")
@user_router.get("/delete_profile")

