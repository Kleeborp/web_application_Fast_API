from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def index():
    return {"massage": "Главная страница сайта"}

@router.get("/about/")
async def about():
    return {"massage": "Информация о сайте и разработчике"}

