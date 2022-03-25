from flask import Flask, request
from controllers import get_url, url_shortener

app = Flask(__name__)

# Simple ping to see if App is up
@app.route("/")
def ping():
    return "<h1>URL Shortener API is up and running </h1>"
  
  
# Shortens the given url and returns it
# body: {"url": "https://google.com"}
# response: {"short_url": "sho.rt/ABCD1234"}
@app.route("/shorten", methods=["POST"])
def shorten_url():
  x = request.json
  url = x.get("url")
  
  if not url:
    return "Missing field url", 400
  
  result = url_shortener(url)
  return result

# Gets the original URL based on the shortened url
# param: url: "sho.rt/ABCD1234"
# response: {"og_url": "https://google.com"}
@app.route("/shorten", methods=["GET"])
def get_shortened_url():
  x = request.args
  url = x.get("url")
  
  if not url:
    return "Missing param url", 400
  
  result = get_url(url)
  return result

if __name__ == "__main__":
    app.run(debug=True)