# dispatcher

components:  
- queue
- history  
- task.delay - fetch

interface:  
- view queue size  
- view history size  
- toggle active state


```
$ celery worker -A tasks -l debug
$ python3 app.py

sqlite> .show tables
sqlite> .schema table

sqlite> .mode list
sqlite> select * from table;

```

The backend and results are being handled by celery and stored with a sqlite database. next up, we need to figure out how to link the databases such that the results are accessible from Flask. also, we need to convert the process flow in such a way that the process is not cyclic, but rather controlled in discrete intervals.




if the flag is set to true, we feed the process as a task to celery. when the result is returned, we check pop the item into history.

incoming request => parser => dispatcher => celery => {{ result }} => database
