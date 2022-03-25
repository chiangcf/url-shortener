from flask import Flask, request
from controllers import get_url, url_shortener

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
  
  
# Gets the original URL based on the shortened url
@app.route("/shorten", methods=["GET"])
def get_shortened_url():
  x = request.args
  url = x.get("url")
  result = get_url(url)
  
  return f"{result}"

if __name__ == "__main__":
    app.run(debug=True)
    
# Shortens the given url
@app.route("/shorten", methods=["POST"])
def shorten_url():
  x = request.json # gets its as a JSON
  url = x.get("url")
  result = url_shortener(url)
  
  return f"{result}"

