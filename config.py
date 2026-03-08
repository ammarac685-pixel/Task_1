import os
from dotenv import load_dotenv

load_dotenv()


def _require(key):
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"Missing required config: '{key}' not found in .env")
    return value


PASS_MARK = int(_require("PASS_MARK"))
LATE_FINE_PER_DAY = int(_require("LATE_FINE_PER_DAY"))
