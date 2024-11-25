from typing import Any

from fastapi import APIRouter

from app.crud import get_items

router = APIRouter()


@router.get("/")
async def read_items(
    text: str | None = None,
) -> Any:
    return await get_items(
        text=text,
    )
