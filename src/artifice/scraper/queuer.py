import json
from collections import OrderedDict


class Queuer:
    """ Queue is the heart of the crawler. Links are added in the form of a list.
    Links are checked for duplicates against both the queue and history.
    Can be initialized either with a created list, or by loading an exported state. """

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


    def load_state_from_json(self, jsonfile):
        try:
            with open(jsonfile) as f:
                data = json.load(f)
            queue = data["Queue.queue"]["items"]
            history = data["Queue.history"]["items"]
            for url in queue:
                self.queue.update( {url : None} )
            for url in history:
                self.history.add(url)
        except:
            raise ValueError("Unable to read JSON from file.")


# <!--  -->
