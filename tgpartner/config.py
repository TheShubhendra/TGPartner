from decouple import config


ENV = config("ENV","development")
APP_ID = config("APP_ID")
API_HASH = config("API_HASH")


if ENV == "production":
    APP_NAME = config ("APP_NAME")
