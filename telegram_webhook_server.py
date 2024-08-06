from fastapi import FastAPI
from pydantic import BaseModel, Field


class Chat(BaseModel):
    id: int
    type: str
    title: str | None = None
    username: str | None = None
    fist_name: str | None = None
    last_name: str | None = None


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None = None
    username: str | None = None


class Message(BaseModel):
    message_id: int
    message_thread_id: int | None = None
    from_: User = Field(default=None, alias="from")
    sender_chat: Chat | None = None
    date: int
    chat: Chat
    text: str | None = None

    class Config:
        populate_by_name = True


class Update(BaseModel):
    update_id: int
    message: Message | None = None
    edited_message: Message | None = None
    channel_post: Message | None = None
    edited_channel_post: Message | None = None


app = FastAPI()


@app.post("/tg_hook")
async def tg_hook(update: Update):
    print(update.message.text)
    return update
