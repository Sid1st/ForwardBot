from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28908582")
    API_HASH = environ.get("API_HASH", "0d79d297bb8f56caed2c8f08bfc17289")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "MissDaisyy_bot") 
    DATABASE_URI = "mongodb+srv://dalate8930:thk0DxiBXLS3t7lo@cluster0.gi431od.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME = environ.get("DATABASE_NAME", "ForwardBot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5052476013').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
