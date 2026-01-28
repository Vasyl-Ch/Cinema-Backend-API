import datetime

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.db.session import get_db
from app.routes.movies import router as movies_router
from app.routes.auth import router as auth_router
from app.routes.cart import router as cart_router
from app.routes.orders import router as orders_router
from app.routes.payments import router as payments_router
from app.routes.webhook import router as webhook_router
from app.routes.users import router as users_router
from app.routes.certifications import router as certifications_router
from dotenv import load_dotenv
from app.core.logging import logger

logger.info("Starting Online Cinema API")
load_dotenv()

app = FastAPI(
    title="Online Cinema API"
)
logger.info("Starting Online Cinema API")


app.include_router(auth_router)
app.include_router(movies_router)
app.include_router(cart_router)
app.include_router(orders_router)
app.include_router(payments_router)
app.include_router(webhook_router)
app.include_router(users_router)
app.include_router(certifications_router)


@app.get("/health", tags=["health"])
async def health_check(db: AsyncSession = Depends(get_db)):
    """
    Health check endpoint for container orchestration
    """
    try:
        await db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Service unhealthy: {str(e)}"
        )
