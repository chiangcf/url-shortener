# url-shortener

Simple Python Flask API + Small React Demo to showcase a url shortener

## URL Shortener API

Need a URL shortened? You have come to the best place this API consist of 2 main endpoints:

- GET `http://localhost:5000/shorten?url=sho.rt/ABCD1234`
- POST `http://localhost:5000/shorten`
  - BODY: `{"url": "https://google.com"}`

Note: I added a URL validator to the post body, which requires you to an internet protocol (https:// or http://) will work

- Example `google.com` will not work but `https://google.com` will work, its just the logic implemented in the API

Currently everything is just for local development but this could be hosted in a AWS lambda

### How to get started

Make sure you have python `3.9` or higher.

To begin with you will need `poetry` to get started, is the preferred package manager for this project!
Run the following in your terminal:
`poetry install` to install the dependencies
`poetry shell` go inside the shell

On lines 10-12 in controllers.py is where we make the DB connection, you will need to pass credentials in order to get in.

Initialize Flask
`python main.py`

Call our API with your favorite API client and start hitting those endpoints!

## URL Shortener React Side

`npm install` to install the dependencies
`npm start` should launch the example app

TODO: Testing, this is a good first pass
