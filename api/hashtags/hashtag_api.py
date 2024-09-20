from fastapi import APIRouter
from database.postservice import *
from api import result_message

hashtag_router = APIRouter(prefix="/hashtags", tags=["Hashtag API"])


@hashtag_router.post("/add_hashtag")
async def add_hashtag_api(hashtag_name: str):
    result = add_hashtag_db(hashtag_name)
    return result_message(result)


@hashtag_router.get("/get_post_by_hashtag")
async def get_post_by_hashtag_api(size: int, hashtag_name: str):
    result = get_post_by_hashtag_db(size, hashtag_name)
    return result_message(result)


@hashtag_router.get("/get_hashtags_by_name")
async def get_hashtags_by_name_api(hashtag_name: str):
    result = get_hashtag_db(hashtag_name)
    return result_message(result)
