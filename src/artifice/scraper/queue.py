import json
from collections import OrderedDict


class Queue:
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
            return self.queue.popitem(last=False)[0]
        except:
            return None


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


links = [
    "www.apple.com",
    "www.bestbuy",
    "www.cisco.com",
    "www.depot.com",
]
target = "www.facebook.com"

Queue = Queue()
Queue._add(links)
Queue._done(target)
print(Queue._next())
print(Queue._export(as_JSON=True))
print(Queue._size())
