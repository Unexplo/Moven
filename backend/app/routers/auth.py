from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register():
    return {"message": "register"}


@router.post("/login")
async def login():
    return {"message": "login"}
