import asyncio
from typing import Optional

from app.models import Item


async def filter_items(data: list[Item], text: str) -> list[Item]:
    loop = asyncio.get_event_loop()
    filtered_data = await loop.run_in_executor(
        None,
        lambda: [
            item
            for item in data
            if text.lower() in item["name"].lower()
            or any(text.lower() in tag.lower() for tag in item["tags"])
        ],
    )
    return filtered_data


async def get_items(
    text: Optional[str] = None,
) -> tuple[tuple[Item], int]:
    data = await get_data()
    if text is not None:
        data = await filter_items(data, text)
    return (data, len(data))


async def get_data():
    return [
        {
            "id": "4f7dfabc-9db7-4bbe-9e03-4f3915f5aecf",
            "name": "Harry Potter",
            "date": "2023-10-01",
            "tags": ["dev", "Inception", "The Matrix"],
            "link": "https://example.com/harry-potter",
        },
        {
            "id": "77046bcb-832c-42c2-9d5d-5db3063e1108",
            "name": "Hermione Granger",
            "date": "2023-10-02",
            "tags": ["qa", "Interstellar", "The Godfather"],
            "link": "https://example.com/hermione-granger",
        },
        {
            "id": "",
            "name": "Ron Weasley",
            "date": "2023-10-03",
            "tags": ["prod", "Pulp Fiction", "Fight Club"],
            "link": "https://example.com/ron-weasley",
        },
        {
            "id": "8107db23-df87-420e-b0b0-91d56efc29c3",
            "name": "Albus Dumbledore",
            "date": "2023-10-04",
            "tags": ["dev", "Forrest Gump", "The Dark Knight"],
            "link": "https://example.com/albus-dumbledore",
        },
        {
            "id": "627c2381-8e39-44ea-9006-8c8cb2de227f",
            "name": "Severus Snape",
            "date": "2023-10-05",
            "tags": ["qa", "The Shawshank Redemption", "Gladiator"],
            "link": "https://example.com/severus-snape",
        },
        {
            "id": "",
            "name": "Rubeus Hagrid",
            "date": "2023-10-06",
            "tags": ["prod", "The Lord of the Rings", "Star Wars"],
            "link": "https://example.com/rubeus-hagrid",
        },
        {
            "id": "cd6722a6-ede3-4217-a697-65142f246be1",
            "name": "Draco Malfoy",
            "date": "2023-10-07",
            "tags": ["dev", "Jurassic Park", "Titanic"],
            "link": "https://example.com/draco-malfoy",
        },
        {
            "id": "e7254e63-fc88-4aa6-8d82-26d4822ff321",
            "name": "Minerva McGonagall",
            "date": "2023-10-08",
            "tags": ["qa", "Avatar", "The Avengers"],
            "link": "https://example.com/minerva-mcgonagall",
        },
        {
            "id": "d9364fac-32f3-4537-9ee6-d8ed60cdce99",
            "name": "Sirius Black",
            "date": "2023-10-09",
            "tags": ["prod", "The Lion King", "Toy Story"],
            "link": "https://example.com/sirius-black",
        },
        {
            "id": "672310e5-aa40-45f5-940b-84ecea0e8bbd",
            "name": "Remus Lupin",
            "date": "2023-10-10",
            "tags": ["dev", "Back to the Future", "Indiana Jones"],
            "link": "https://example.com/remus-lupin",
        },
    ]
