from fastapi import FastAPI
from app.core.config import settings
from app.routers import auth, sessions, reports, users

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(sessions.router)
app.include_router(reports.router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
