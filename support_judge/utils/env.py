import os

from dotenv import load_dotenv

from support_judge.utils.paths import PROJECT_ROOT

ENV_PATH = PROJECT_ROOT / ".env"


def load_env():
    # Load the .env file at the project root.
    load_dotenv(ENV_PATH)


def require_env(name):
    if not os.environ.get(name):
        raise RuntimeError(
            f"{name} was not found. Check your .env file: {ENV_PATH}"
        )
