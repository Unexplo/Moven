from fastapi import APIRouter

router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.post("/")
async def create_session():
    return {"message": "session created"}


@router.get("/")
async def list_sessions():
    return {"message": "list sessions"}


@router.get("/{session_id}")
async def get_session(session_id: str):
    return {"message": f"session {session_id}"}
