from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, Item

async def create_user(session: AsyncSession, user: User) -> User:
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    result = await session.exec(select(User).where(User.username == username))
    return result.first()

async def create_item(session: AsyncSession, item: Item) -> Item:
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item

async def get_items(session: AsyncSession) -> list[Item]:
    result = await session.exec(select(Item))
    return result.all()

