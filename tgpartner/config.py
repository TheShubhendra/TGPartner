from decouple import config


ENV = config("ENV", "development")
APP_ID = config("APP_ID")
API_HASH = config("API_HASH")


#Production variables
APP_NAME = config("APP_NAME", None)
STRING_SESSION = config("STRING_SESSION", None)
