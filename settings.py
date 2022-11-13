from pathlib import Path
from dotenv import load_dotenv
import os


# loading env file
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def get_value_setting(key):
    return os.getenv(key)
