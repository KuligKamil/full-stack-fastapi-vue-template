from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.include_router(api_router)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
)

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
