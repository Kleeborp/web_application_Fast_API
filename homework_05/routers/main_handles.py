from fastapi import APIRouter, Request, status, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from schemas.cars import cars_list, Car

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse, name = "cars_list")
async def cars_details(request: Request):
    """Получить список автомобилей"""

    result = cars_list



    context = {
        "request": request,
        "cars": result,
        "title": 'Список автомобилей'
    }

    return templates.TemplateResponse("cars_list.html", context=context)

@router.get("/{car_id}", response_class=JSONResponse, name = "car_details")
async def car_detail(car_id: int):
    """Получить информацию об автомобиле"""

    car_id -=1

    if car_id < 0 or car_id >= len(cars_list):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Такого автомобиля здесь нет")

    car = cars_list[car_id]

    # context = {
    #     "request": request,
    #     "car": car,
    # }

    # return templates.TemplateResponse("car_details.html", context=context)
    return {"car №": car.id, "brand": car.brand, "model": car.model, "cost": car.cost}

@router.post("/", response_model=Car, status_code=status.HTTP_201_CREATED, name = "car_create")
async def car_add(new_car: Car):
    """Добавить автомобиль"""
    for c in cars_list:
        if c.id == new_car.id:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Car already exists")
    cars_list.append(new_car)
    return new_car