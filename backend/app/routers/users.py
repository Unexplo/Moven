from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_current_user():
    return {"message": "current user"}


@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"message": f"user {user_id}"}
