// This is where we do API calls

// GET request to the shortening lambda and retrieve the original value
export const getUrl = async (shortenedUrl) => {
  console.log(shortenedUrl);
  const url = "http://localhost:5000/shorten?url=" + shortenedUrl;
  console.log(url);

  const response = await fetch(url).then((result) => result.json());

  console.log("this is your url: " + response.og_url);
  return response;
};

// POST request to the shortening lambda to send a fresh url for it to encode
// @returns: shortenedUrl
export const shortenUrl = async (ogUrl) => {
  let url = "http://localhost:5000/shorten";
  console.log("ogUrl: " + ogUrl);
  let options = {
    method: "POST",
    mode: "cors",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url: ogUrl,
    }),
  };
  console.log(options);
  const response = await fetch(url, options).then((result) => result.json());

  console.log(response);
  console.log("short url: " + response.short_url);
  return response;
};
