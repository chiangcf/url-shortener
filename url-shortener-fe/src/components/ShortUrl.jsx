import React from "react";
import { useState } from "react";
import { Button, Form } from "semantic-ui-react";

export const ShortUrl = () => {
  const [url, setUrl] = useState("");
  const [url1, setUrl1] = useState("");
  return (
    <div>
      <b>🐼 Super Awesome URL Shortener 🐼</b>
      <Form>
        <Form.Field>
          <input
            placeholder="https://google.com"
            value={url}
            onChange={(event) => {
              setUrl(event.target.value);
            }}
          />
        </Form.Field>
        <Button
          type="submit"
          onClick={() => {
            console.log("Looking to shorten this url: " + url);
          }}
        >
          Create Shortened Url
        </Button>
      </Form>
      <Form>
        <Form.Field>
          <input
            placeholder="sho.rt/ABCD1234"
            value={url1}
            onChange={(event) => {
              setUrl1(event.target.value);
            }}
          />
        </Form.Field>
        <Button
          type="submit"
          onClick={() => {
            console.log("Looking to decode this url: " + url1);
          }}
        >
          Get original value
        </Button>
      </Form>
    </div>
  );
};
