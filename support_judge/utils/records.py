import datetime
import json

from support_judge.utils.paths import RESULTS_DIR


def utc_timestamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def append_jsonl(filename, record):
    # Append one JSON record per line to a file in results/.
    RESULTS_DIR.mkdir(exist_ok=True)

    with (RESULTS_DIR / filename).open("a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")
