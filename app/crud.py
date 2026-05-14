from sqlmodel import select
from app.models import User, Item
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncAttrs

async def create_user(user: User) -> User:
    async for session in get_session():
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

async def get_user_by_username(username: str) -> User | None:
    async for session in get_session():
        result = await session.exec(select(User).where(User.username == username))
        return result.first()

async def create_item(item: Item) -> Item:
    async for session in get_session():
        session.add(item)
        await session.commit()
        await session.refresh(item)
        return item

async def get_items() -> list[Item]:
    async for session in get_session():
        result = await session.exec(select(Item))
        return result.all()
