from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/{session_id}")
async def get_report(session_id: str):
    return {"message": f"report for session {session_id}"}


@router.post("/{session_id}/generate")
async def generate_report(session_id: str):
    return {"message": f"generating report for session {session_id}"}
