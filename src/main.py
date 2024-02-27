import dotenv
import requests
from os import getenv
import random


def main() -> None:
    dotenv.load_dotenv()
    r = requests.post(getenv("DISCORD_WEBHOOK_URI"), json={
        "content": "<@{userid}> さっさと働け！".format(userid=getenv("TARGET_ID"))
    })
    r.raise_for_status()


if __name__ == "__main__":
    main()
