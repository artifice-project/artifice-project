
import json
from collections import OrderedDict


class Queuer:
    """ Queue is the heart of the crawler. Links are added in the form of a list.
    Links are checked for duplicates against both the queue and history. """

    def __init__(self):
        """
        queue::tasks to be dispatched from
        history::previously completed tasks
        """
        self.queue = OrderedDict()
        self.history = set()


    def _size(self):
        size = {
            "queue" : len(self.queue),
            "history" : len(self.history),
        }
        return size


    def _add(self, url_list):
        """ Add list of links to the queue, ignoring duplicates.
        arg:url_list: list of links from scraper
        returns: n/a
        """
        for url in url_list:
            if url not in self.queue.keys() and url not in self.history:
                self.queue.update( {url : None} )


    def _next(self):
        """ Pop first item from the queue.
        arg: n/a
        returns: <string> or None
        """
        try:
            # item is a tuple, not a key-value pair
            link = self.queue.popitem(last=False)
            return link[0]
        except:
            print(f"[BAD LINK]: {link}")
            raise ValueError("Links exhausted from queue.")


    def _done(self, url):
        """ Move scraped link from queue to history.
        arg:url: <string>
        returns: n/a
        """
        self.history.add(url)


    def _export(self, as_JSON=False):
        """ Returns an object to be saved.
        arg:as_JSON: <boolean> (optional)
        returns: <dict> or <JSON string>
        """
        data = {
            "Queue.queue" : {
                "items" : list(self.queue.keys()),
                "size" : self._size()["queue"],
            },
            "Queue.history" : {
                "items" : list(self.history),
                "size" : self._size()["history"],
            }
        }
        if as_JSON:
            data = json.dumps(data, indent=4)
        return data


# <!--  -->

if __name__ == '__main__':

    links = [
        "www.apple.com",
        "www.bestbuy",
        "www.cisco.com",
        "www.depot.com",
    ]
    target = "www.facebook.com"

    Q = Queuer()
    Q._add(links)
    Q._done(target)
    print(Q._next())
    print(Q._export(as_JSON=True))
    print(Q._size())
