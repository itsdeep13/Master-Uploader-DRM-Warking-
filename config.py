import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047785902:AAE59KTfmhRvF8sUSYIzl9wcGnm4FLXiWDk")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "24250238"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "6175650047").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers
    
    HOST = os.environ.get("HOST", "https://lnkz.tech/")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility


