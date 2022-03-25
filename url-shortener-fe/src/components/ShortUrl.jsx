import React from "react";
import { useState } from "react";
import { Button, Form } from "semantic-ui-react";
import { getUrl, shortenUrl } from "../hooks/controllers";

export const ShortUrl = () => {
  const [url, setUrl] = useState("");
  const [url1, setUrl1] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [ogUrl, setOgUrl] = useState("");
  return (
    <div>
      <h1>Super Awesome URL Shortener</h1>
      <br />
      <br />
      <b>{shortUrl}</b>
      <br />
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
          onClick={async () => {
            const newVal = await shortenUrl(url);
            setShortUrl(newVal.short_url);
          }}
        >
          Create Shortened Url
        </Button>
      </Form>
      <br />
      <b>{ogUrl}</b>
      <br />
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
          onClick={async () => {
            const newVal = await getUrl(url1);
            setOgUrl(newVal.og_url);
          }}
        >
          Get Original Value
        </Button>
      </Form>
    </div>
  );
};
