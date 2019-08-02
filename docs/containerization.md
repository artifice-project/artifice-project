# Container Overview

# _1_: Dispatcher
- https://stackoverflow.com/questions/37311562/set-up-a-while-loop-in-celery-task  
- https://stackoverflow.com/questions/50180980/running-python-in-flask-with-a-constant-background-task  

Queue which keeps track of the sites that have been visited, as well as those which are waiting to be. Tasks are dispatched accordingly, in a recursive, cyclic manner while engaged. Task arguments are sent as url link strings to the listening Scraper, which collects information on the page and returns it in a defined schema. Once received, the content is stored in the sister database.   There are several native mechanics required:  
- the ability to dispatch a url as tasks to workers  
- the ability to start and stop the dispatches  
- the ability to show the current size of the queue, history, and saved data--as well as view it in a live manner  
- the ability to display a graphic of queue size vs. history size  
- the ability to enable purging and exporting of the content storage table.
```python




```
---
# _2_: Scraper
Gathers data from the webpage which has been received from the Dispatcher. Once collected and parsed, data is sent back to the socket from which it originated.
```python



```
---
# _3_: Crawler DB
__table__ = history (scales linearly)  
__table__ = queue (scales exponentially)  
__table__ = content (scales linearly)  
```python



```
---
# _4_: Model Service
Supports the hosting, training, and querying of ML models. The sister database contains all of the text used in the training process, as well as a weight archive for each of the hosted models. API supports POST for upload of scraped data, GET for model querying, as well as viewing and modification of settings.   There are several native mechanics required:  
- the ability to upload either trained models or new training data for those existing  
- the ability to provide insight into the currently implemented models  
- the ability to hot-swap weights and to download/upload new sets  
- the ability to generate new stories on-demand  
- the ability to use "sentient mode" where generated stories can be tweaked by a person before uploading as content  
- the ability to schedule new story generation to happen automatically
- the ability to blacklist certain words from appearing in output
```python





```
---
# _5_: Model DB
__table__ = * *models*  
__table__ = * *weights*  
__table__ = * *config*  
```python





```
---
# _6_: Frontend
Renders the generated content as a graphic interface. Stories are generated and rendered ahead of time and retrieved from the sister database, which contains all the generated output that is received from the Model Service.  
There are several native mechanisms required:  
- the ability to view pages as an administrator
- the ability to select certain stories as banner stories, etc
- the ability to monitor site statistics such as visits, geography, etc
```python





```
---
# _7_: Story DB
__table__ = stories  
__table__ = social  
__table__ = traffic  
```python





```
---
