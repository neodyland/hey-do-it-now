import dotenv
import requests
from os import getenv
import random


def main() -> None:
    with open("src/messages.txt", "r") as f:
        contents = f.readlines()
    content = random.choice(contents)
    dotenv.load_dotenv()
    r = requests.post(getenv("DISCORD_WEBHOOK_URI"), json={
        "content": "<@{userid}> {content}".format(userid=getenv("TARGET_ID"), content=content),
        "username": "ヒュンダイねこ"
    })
    r.raise_for_status()


if __name__ == "__main__":
    main()
