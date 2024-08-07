import subprocess


if __name__ == "__main__":
    path = 'E:/Users/Любичев/ngrok.exe'
    proc = subprocess.Popen([path, 'http', '8000'])

    print(proc.communicate(timeout=15))

    # tg_bot = TelegramApi("7468754032:AAGn_xvms7WJoFdOXZBDbBo1M7sY27AxwDo")
    # tg_bot.set_webhook(f"{callback_server}/tg_hook")

    # path = 'E:/Users/User8/Desktop/bot'
    # res = subprocess.run([path, 'fastapi', 'prod', 'telegram_webhook_server.py'], capture_output=True)

    input("press enter to terminate")
    proc.terminate()
