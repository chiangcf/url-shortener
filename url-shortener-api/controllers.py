
from pymongo import MongoClient
import certifi

# Mongo DB connection, ask me for the password! :)
# TODO: Store password in credstash
cluster = MongoClient("mongodb+srv://chris:<password>@shortdata.yyg2l.mongodb.net/test?retryWrites=true&w=majority", tlsCAFile=certifi.where())  
db = cluster["shortened"]
collection = db["test-data"]

def url_shortener(url):
  return ""


# Gets the original URL based on the shortened url
def get_url(url): 
  # We always know its going to be sho.rt, so hard coding it for now
  url_id = url.replace("sho.rt/", "")

  # Check Mongo for that id
  result = collection.find_one({"_id": url_id})

  # If result is not in the table it will return a 404
  if result:
    return result["url"]
  else:
    return "Couldn't find that URL sorry", 404