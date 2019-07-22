import os
import json

from queuer import Queuer
from spider import Spider
from web import Web

API_ENDPOINT = "http://localhost:10000/update"
SAVE_FILE = "queue.json"
SEED_URL = "https://www.npr.org/sections/politics"
DATA_FILE = "databasev2.json"
DATABASE = []
TALLY = 0
MAX_VALUE = 10

# try:
print("[INITIALIZING]")
web = Web(API_ENDPOINT)
# print("[created WEB]")
Q = Queuer()
# print("[created QUEUER]")
Spi = Spider(SEED_URL)
# print("[planting SEED_URL]")
Spi.lay()
# print("[laying EGG]")
egg = Spi.egg()
# print("[created EGG]")
status_code = web.POST(egg)
# print("[posted EGG]")
Q._add(egg["links"])
# print("[adding LINKS]")
Q._done(SEED_URL)
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
    print(f"[ #{TALLY} ]\t[{status_code}]\t{url}")

# except:
#     print("[EXITING]")
#     pass
#
# finally:
#     datastr = json.dumps(DATABASE, indent=4)
#     jsonstr = Q._export(as_JSON=True)
#     with open(os.path.join("data", SAVE_FILE), "w") as f:
#         print(f"[SAVING] {SAVE_FILE}")
#         f.write(jsonstr)
#     with open(os.path.join("data", DATA_FILE), "w") as f:
#         print(f"[SAVING] {DATA_FILE}")
#         f.write(datastr)
#     print("\n[DONE]")
