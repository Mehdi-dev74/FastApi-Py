from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session, init_db
from app.models import User, Item
from app.schemas import UserCreate, UserResponse, ItemCreate, ItemResponse
from app.crud import create_user, get_user_by_username, create_item, get_items

app = FastAPI(title="My FastAPI App", version="1.0.0")

# -------------------
# CORS CONFIG
# -------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------
# STARTUP EVENT
# -------------------
@app.on_event("startup")
async def on_startup():
    await init_db()

# -------------------
# ROOT (clean)
# -------------------
@app.get("/")
async def root():
    return {"status": "ok"}

# -------------------
# CREATE USER
# -------------------
@app.post("/users/", response_model=UserResponse, status_code=201)
async def create_new_user(
    user_data: UserCreate,
    session: AsyncSession = Depends(get_session)
):
    db_user = await get_user_by_username(user_data.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    user = User(username=user_data.username, email=user_data.email)
    created_user = await create_user(user)
    return created_user

# -------------------
# CREATE ITEM
# -------------------
@app.post("/items/", response_model=ItemResponse, status_code=201)
async def create_new_item(
    item_data: ItemCreate,
    session: AsyncSession = Depends(get_session)
):
    item = Item(**item_data.dict(), owner_id=1)  # demo only
    created_item = await create_item(item)
    return created_item

# -------------------
# GET ITEMS
# -------------------
@app.get("/items/", response_model=list[ItemResponse])
async def read_items(session: AsyncSession = Depends(get_session)):
    items = await get_items()
    return items

