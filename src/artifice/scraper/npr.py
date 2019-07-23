import os
import json
import time
import requests
import datetime
from pprint import pprint
from bs4 import BeautifulSoup as BS


# print(soup.findAll(text=True))
def soup_all_visible_text(soup):
    """ soup = BS(htmldoc, 'html.parser') """
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.get_text()
    return visible_text


def get_soup_obj(url):
    """ takes in a url and return a soup object """
    try:
        r = requests.get(url)
        html_doc = r.content
        soup = BS(html_doc, 'html.parser')
        return soup
    except:
        pass


def soup_npr_get_links(soup):
    lst = []
    for link in [link.get('href') for link in soup.find_all('a')]:
        if link:
            if 'https://www.npr.org' in link:
                lst.append(link.strip())
    return list(set(lst))


def soup_npr_captions(soup):
    cap_lst = []
    for p in soup.find_all('p'):
        try:
            if 'caption' in p['class']:
                cap_lst.append(p.text)
        except:
            pass
    return cap_lst


def soup_npr_wash_article(soup):
    """ Take in the article string and strip disruptive characters """
    p_tags = [e.get_text() for e in soup.find_all('p', {})]
    article = '\n'.join(p_tags)
    washed = " ".join(article.split())
    return str(washed)

def soup_npr_get_title(soup):
    """ thin wrapper for soup.title """
    try:
        t = str(soup.title.text)
    except:
        t = ''
    return t


#######################################################################
# url = "http://www.cnn.com/politics"
# article_link = "https://www-m.cnn.com/2019/07/17/politics/trump-impeachment-house-vote/index.html?r=https%3A%2F%2Fwww.cnn.com%2Fpolitics"
# google_politics = "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFZ4ZERBU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US:en"

class Spider(object):
    def __init__(self, url):
        self.soup = get_soup_obj(url)

        self.url = url
        self.title = soup_npr_get_title(self.soup)
        self.captions = soup_npr_captions(self.soup)
        self.text = soup_npr_wash_article(self.soup)
        self.links = soup_npr_get_links(self.soup)

    def egg(self):
        return dict(
            url=self.url,
            title=self.title,
            captions=self.captions,
            text=self.text,
            links=self.links,
        )


class SpiderWeb(object):
    """ Dispatcher for Spider crawlers """
    def __init__(self, seed):
        print(f"[SEED] \t {seed}")
        self.seed = seed
        self.database = {}
        self.queue = []
        self.success = 0
        self.failed = 0

    def add_egg(self, egg):
        print(f"[ADDING EGG]")
        try:
            key = egg['url']
            val = egg
            self.database.update({key : val})
            self.queue = list(set(self.queue + egg['links']))
            self.success += 1
        except:
            self.failed += 1

    def next_in_line(self):
        next = self.queue.pop(0)
        print(f"[NEXT IN QUEUE] \t {next}")
        return next

    def capture_state(self):
        print(f"[CAPTURING STATE]")
        return dict(
            seed=self.seed,
            database=self.database,
            queue=self.queue,
            success=self.success,
            failed=self.failed,
        )

    def dump_state_to_file(self,filename):
        print(f'\nPASS: \t {self.success} \t FAIL: \t {self.failed}')
        print(f"[WRITING FILE] \t {filename}")
        data = self.capture_state()
        with open(filename, "w") as f:
            jstr = json.dumps(data, indent=4)
            f.write(jstr)


try:
    tally = 0
    seed_url = "https://www.npr.org/sections/politics"

    Web = SpiderWeb(seed_url)
    egg = Spider(Web.seed).egg()
    Web.add_egg(egg)
    while True:
        if len(Web.queue) is 0:
            break
        else:
            target = Web.next_in_line()
            print(f"[NEW SPIDER]: \t {target}")
            egg = Spider(target).egg()
            Web.add_egg(egg)
            tally += 1
            print(f"# {tally}")
except:
    pass
finally:
    print(f"\n[PAGES SCRAPED]: {tally}")
    Web.dump_state_to_file("output2.json")
print("\n DONE.")

# CRAWL_LIST = [
#     "https://www.npr.org/2019/07/17/742705054/house-holds-attorney-general-and-commerce-secretary-in-contempt-over-census-prob",
#     "https://text.npr.org/s.php?sId=742705054",
# ]

# url = CRAWL_LIST[0]
# spider = Spider(url).egg()
# print(spider)

# CRAWL_LOG = {}
# for url in CRAWL_LIST:
#
#     soup = get_soup_obj(url)
#     CRAWL_OBJ = {}
#     CRAWL_OBJ.update(url=url)
#     CRAWL_OBJ.update(captions=soup_npr_captions(soup))
#     CRAWL_OBJ.update(text=soup_npr_wash_article(soup))
#     CRAWL_OBJ.update(title=soup_npr_get_title(soup))
#     CRAWL_OBJ.update(links=soup_npr_get_links(soup))
#     CRAWL_LOG.update({url : CRAWL_OBJ})
# print(CRAWL_LOG)




"""
create a seperate parser class for each website to be crawled. the crawler should take in a home/landing page and be able to extract all headlines and links from the page, which are stored temporarily in a key-value store. for each item in the dictionary, the url should be visited and determined whether or not it is a detail view for an article. if this is the case, proceed to parse the page, extracting the story text, headline, image captions, and any other links found on the page that point to within the target website. these items are added to a second dictionary, where they are eventually compared to the primary dictionary. if the link does not exist in the primary dict, the url is added to be subsequently visited and scraped. this process proceeds until all candidate links are exhausted. once the list of links has all been visited, the scraped content is aggregated and returned to the dispatcher. the dispatcher receives the parsed material and then saves it to the raw content database. there should eventually be some sort of safeguard mechanism such that once a set number of links has been visited, the crawler subsides and returns the information that has been gathered thus far.


# check if ptags have ONLY text
pgs = soup.find_all('p')
for pg in pgs:
    if not pg.get('class'):
        if pg.get('a'):
            print(pg)
            pass
        # print(pg)
    else:
        pass


"""
