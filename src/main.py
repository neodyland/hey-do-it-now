import dotenv
import requests
from os import getenv
import random


def main() -> None:
    with open("./messages.txt", "r") as f:
        contents = f.readlines()
    content = random.choices(contents)
    dotenv.load_dotenv()
    r = requests.post(getenv("DISCORD_WEBHOOK_URI"), json={
        "content": "<@{userid}> {content}".format(userid=getenv("TARGET_ID"), content=content)
    })
    r.raise_for_status()


if __name__ == "__main__":
    main()
