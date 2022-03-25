
import random
import string
from pymongo import MongoClient
import certifi
import validators

# Mongo DB connection, ask me for the password! :)
# TODO: Store password in credstash
user = "unitedmasters"
password = "notasafepassword123"
cluster = MongoClient(f"mongodb+srv://{user}:{password}@shortdata.yyg2l.mongodb.net/test?retryWrites=true&w=majority", tlsCAFile=certifi.where())  
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
  if not url:
    return "URL cannot be empty", 400
  
  valid=validators.url(url)
  if not valid:
      return "Invalid URL, did you forget the https:// ? ", 400
    
  new_id = id_generator()

  # A way to stop id coalitions
  while collection.find_one({"_id": new_id}):
    new_id = id_generator()
      
  # Insert new pair to mongo
  pair = {"_id": new_id, "url": url}
  collection.insert_one(pair)
  
  return {"short_url": f"sho.rt/{new_id}"}