from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/4cbd37388473e622dca4c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/4cbd37388473e622dca4c.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ze_in22")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ucriss")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6300938349").split()))


FAILED = "https://telegra.ph/file/4cbd37388473e622dca4c.jpg"
