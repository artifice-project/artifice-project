import requests
from pprint import pprint
from functools import wraps
from bs4 import BeautifulSoup as BS4


class Spider(object):
    """ die-on-term crawler agent.

    target = "https://www.npr.org/sections/politics"
    spider = Spider(target)
    spider.lay()
    egg = spider.egg()

    """

    def __init__(self, url):
        self.only_follow_explicit_links = True
        self.url = url
        self.url_root = self.isolate_url_root(url)
        soup, success = self.pour_soup(url)
        self.soup = soup
        self.success = success
        # Spiderbot.lay() =>
        self.title = ""
        self.captions = []
        self.texts = []
        self.links = []


    @staticmethod
    def isolate_url_root(url):
        from urllib.parse import urlparse
        root = "https://" + urlparse(url).netloc
        return root


    @staticmethod
    def pour_soup(url):
        try:
            r = requests.get(url)
            soup = BS4(r.content, 'html.parser') if r.status_code is 200 else None
            success = 1
        except:
            soup, success = None, 0
        return soup, success


    @staticmethod
    def _strain_links(links, root):
        keep = []
        for link in links:
            if not link:
                pass
            elif (link[0] is "#") or (len(link) < 2):
                pass
            elif (root not in link):
                # keep.append(root + link.strip())
                pass
            else:
                keep.append(link.strip())
        return keep


    def get_title(self):
        if self.soup.title:
            self.title = str(self.soup.title.text)


    def get_captions(self):
        caption_list = []
        for p in self.soup.find_all('p'):
            try:
                if 'caption' in p['class']:
                    caption_list.append(p.text)
            except:
                pass
        self.captions = caption_list


    def get_texts(self):
        """ Take in the article string and strip disruptive characters """
        p_tags = [e.get_text() for e in self.soup.find_all('p', {})]
        article = '\n'.join(p_tags)
        washed = " ".join(article.split())
        self.texts = str(washed)


    def get_links(self):
        lst = [str(link.get('href')) for link in self.soup.find_all('a')]
        washed = list(set(lst))
        # ship off to another function to handle url blueprints
        self.links = self._strain_links(washed, self.url_root)


    def lay(self):
        if self.success is 1:
            self.get_title()
            self.get_captions()
            self.get_texts()
            self.get_links()


    def egg(self):
        return dict(
            success=self.success,
            url=self.url,
            title=self.title,
            captions=self.captions,
            texts=self.texts,
            links=self.links,
        )


if __name__ == '__main__':

    target = "https://www.npr.org/sections/politics"
    spider = Spider(target)
    spider.lay()
    egg = spider.egg()
    del spider
    pprint(egg)




"""

def fail_silently(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            pass
    return wrap

"""
