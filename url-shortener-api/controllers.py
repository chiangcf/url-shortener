
import random
import string
from pymongo import MongoClient
import certifi

# Mongo DB connection, ask me for the password! :)
# TODO: Store password in credstash
cluster = MongoClient("mongodb+srv://chris:1234@shortdata.yyg2l.mongodb.net/test?retryWrites=true&w=majority", tlsCAFile=certifi.where())  
db = cluster["shortened"]
collection = db["test-data"]

# Gets the original URL based on the shortened url
def get_url(url): 
  # We always know its going to be sho.rt, so hard coding it for now
  url_id = url.replace("sho.rt/", "")

  # Check Mongo for that id
  result = collection.find_one({"_id": url_id})

  # If result is not in the table it will return a 404
  if result:
    return {"og_url": result["url"]}
  else:
    return "Couldn't find that URL sorry", 404
  
# Generates a random 8 character string id, not the best way to do it long term
def id_generator():
  return "".join(random.choices(string.ascii_letters, k=8))

# Shortens the given url by creating a unique id that will get stored to mongoDB
# returns the new shortened url
def url_shortener(url):
  new_id = id_generator()

  # A way to stop id coalitions
  while collection.find_one({"_id": new_id}):
    new_id = id_generator()
      
  # Insert new pair to mongo
  pair = {"_id": new_id, "url": url}
  collection.insert_one(pair)
  
  return {"short_url": f"sho.rt/{new_id}"}