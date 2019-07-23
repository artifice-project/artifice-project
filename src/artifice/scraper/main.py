import os
import json

from web import Web
from queuer import Queuer
from spider import Spider


API_ENDPOINT = "http://localhost:10000/update"
SEED_URL = "https://www.npr.org/sections/politics"
QUEUE_FILE = os.path.join("data", "queue.json")
DATA_FILE = os.path.join("data", "database.json")
DATABASE = []
TALLY = 0
MAX_VALUE = 10000


if __name__ == '__main__':
    try:
        print("[INITIALIZING]")
        web = Web(API_ENDPOINT)
        Q = Queuer()
        try:
            Q.load_state_from_json(QUEUE_FILE)
            print("[QUEUE] using QUEUE_FILE")
        except:
            Q._add([SEED_URL])
            print("[QUEUE] using SEED_URL")
        print("[ENTERING LOOP]")
        while TALLY < MAX_VALUE:
            url = Q._next()     # raises Error on failure
            spider = Spider(url)
            spider.lay()
            egg = spider.egg()
            status_code = web.POST(egg)
            DATABASE.append(egg)
            Q._add(egg["links"])
            Q._done(url)
            TALLY += 1
            print(f"[#{TALLY}]\t[{status_code}]\t{url}")

    except:
        print("[EXITING]")
        pass

    finally:
        datastr = json.dumps(DATABASE, indent=4)
        jsonstr = Q._export(as_JSON=True)
        with open(QUEUE_FILE, "w") as f:
            print(f"[SAVING] {QUEUE_FILE}")
            f.write(jsonstr)
        with open(DATA_FILE, "w") as f:
            print(f"[SAVING] {DATA_FILE}")
            f.write(datastr)
        print("\n[DONE]")


# <!-- -->
