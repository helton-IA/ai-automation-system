from dotenv import load_dotenv

load_dotenv()

import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./automation.db"
)

APP_NAME = os.getenv(
    "APP_NAME",
    "AI Automation System"
)

APP_VERSION = os.getenv(
    "APP_VERSION",
    "3.1.0"
)