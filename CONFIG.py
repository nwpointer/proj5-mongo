"""
Configuration of 'memos' Flask app. 
Edit to fit development or deployment environment.

"""
import random 

### My local development environment
PORT=5000
DEBUG = True
# MONGO_URL = "mongodb://memo:iremember@localhost:27333/memos"  # on Gnat
MONGO_URL = "mongodb://admin:password@localhost:27017/memos"  # on Gnat


### On ix.cs.uoregon.edu (Michal Young's instance of MongoDB)
# PORT=random.randint(5000,8000)
# DEBUG = False # Because it's unsafe to run outside localhost
# MONGO_URL =  "mongodb://memo:iremember@localhost:4915/memos"  # on ix
