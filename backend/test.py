from typing import Optional, List, Tuple
import asyncio


class Item:
    def __init__(self, name: str, date: str, tags: List[str], link: str):
        self.name = name
        self.date = date
        self.tags = tags
        self.link = link


async def filter_items(data: List[Item], text: str) -> List[Item]:
    loop = asyncio.get_event_loop()
    filtered_data = await loop.run_in_executor(
        None,
        lambda: [
            item
            for item in data
            if text.lower() in item.name.lower()
            or any(text.lower() in tag.lower() for tag in item.tags)
        ],
    )
    return filtered_data


async def get_items(text: Optional[str] = None) -> Tuple[List[Item], int]:
    data = await get_data()
    if text is not None:
        data = await filter_items(data, text)
    return (data, len(data))


async def get_data() -> List[Item]:
    return [
        Item(
            name="Harry Potter",
            date="2023-10-01",
            tags=["dev", "Inception", "The Matrix"],
            link="https://example.com/harry-potter",
        ),
        Item(
            name="Hermione Granger",
            date="2023-10-02",
            tags=["qa", "Interstellar", "The Godfather"],
            link="https://example.com/hermione-granger",
        ),
        Item(
            name="Ron Weasley",
            date="2023-10-03",
            tags=["prod", "Pulp Fiction", "Fight Club"],
            link="https://example.com/ron-weasley",
        ),
        # Add more items as needed
    ]


# Example usage
async def main():
    items, count = await get_items("Harry")
    for item in items:
        print(item.name, item.date, item.tags, item.link)
    print(f"Total items: {count}")


# Run the example
asyncio.run(main())