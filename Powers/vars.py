from os import getcwd
from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])

class Config:
    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default=123))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1344569458))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP"))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="").split()]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="").split()]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="").split()]
    GENIUS_API_TOKEN = config("GENIUS_API", default=None)
    AuDD_API = config("AuDD_API", default=None)
    RMBG_API = config("RMBG_API", default=None)
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="gojo_satarou")
    BDB_URI = config("BDB_URI", default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="gojo_bots_network")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="gojo_bots_network")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE", default="Asia/Kolkata")

class Development:
    LOGGER = True
    BOT_TOKEN = "YOUR_BOT_TOKEN"
    API_ID = 12345
    API_HASH = "YOUR_API_HASH"
    OWNER_ID = 1344569458
    MESSAGE_DUMP = -100845454887
    DEV_USERS = []
    SUDO_USERS = []
    WHITELIST_USERS = []
    DB_URI = "YOUR_MONGO_DB_URI"
    DB_NAME = "YOUR_DB_NAME"
    GENIUS_API_TOKEN = "YOUR_GENIUS_API_TOKEN"
    RMBG_API = "YOUR_RMBG_API"
    PREFIX_HANDLER = ["!", "/", "$"]
    SUPPORT_GROUP = "YOUR_SUPPORT_GROUP"
    SUPPORT_CHANNEL = "YOUR_SUPPORT_CHANNEL"
    VERSION = "YOUR_VERSION"
    TIME_ZONE = "Asia/Kolkata"
    BDB_URI = ""
    WORKERS = 8
    
