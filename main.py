import subprocess
import time
from fastapi import FastAPI
from pydantic import BaseModel, Field
from TelegramApi import *
from VkApi import *
import re
import uvicorn
from threading import Thread


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
    post_id = re.search(r'-?\d+_\d+', update.message.text)
    if post_id is None:
        tg_bot.send_message(update.message.from_.id, "Не удалось найти id поста в сообщении")
        return update
    else:
        post_id = post_id.group(0)

    response = vk_bot.wall_get_by_id(post_id)
    if response['response']['items'] is []:
        tg_bot.send_message(update.message.from_.id, "Не удалось получить контент в посте")
        return update

    tg_bot.send_message(update.message.from_.id, response['response']['items'][0]['text'])
    for attachment in response['response']['items'][0]['attachments']:
        if attachment['type'] == 'photo':
            print(attachment['photo']['sizes'][-1]['url'])
            tg_bot.send_document(update.message.from_.id, attachment['photo']['sizes'][-1]['url'])
        elif attachment['type'] == 'doc':
            print(attachment['doc']['url'])
            tg_bot.send_document(update.message.from_.id, attachment['doc']['url'])
        elif attachment['type'] == 'link':
            print(attachment['link']['url'])
            tg_bot.send_message(update.message.from_.id, attachment['link']['url'])

    return update


def startup():
    path = 'E:/Users/Любичев/ngrok.exe'
    proc = subprocess.Popen([path, 'http', '8000'], stdout=subprocess.PIPE)

    time.sleep(60)
    resp = requests.get('http://localhost:4040/api/tunnels')
    callback_server = resp.json()['tunnels'][0]['public_url']

    print(callback_server)

    tg_bot.set_webhook(f"{callback_server}/tg_hook")


tg_bot = TelegramApi("7468754032:AAGn_xvms7WJoFdOXZBDbBo1M7sY27AxwDo")
vk_bot = VkApi("95797d9495797d9495797d943d96626c7d9957995797d94f3cb688c233dfd81783e9486", "5.199")

if __name__ == "__main__":
    thread = Thread(target=startup)
    thread.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
