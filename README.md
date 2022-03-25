# url-shortener

Simple Python Flask API + Small React Demo to showcase a url shortener

## URL Shortener API

Need you URL shortened? You have come to the best place this API consist of 2 main endpoints:

- GET `http://localhost:5000/shorten?url=sho.rt/ABCD1234`
- POST `http://localhost:5000/shorten`
  - POST BODY: `{"url": "https://google.com"}`

Currently everything is just for local development but this could be hosted in a AWS lambda

### How to get started

Make sure you have python 3.9 or higher.

To begin with you will need `poetry` to get started, is the preferred package manager for this project!
Run the following in your terminal:
`poetry install`
`poetry shell`

Initialize Flask
`python main.py`

Call our API with your favorite API client and start hitting those endpoints!

## URL Shortener React Side

`npm start` should launch the example app
