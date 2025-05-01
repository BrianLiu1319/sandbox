'''
JSON ->

standardized format for structuring data
universal format for transmitting data on web

working with JSON :

standard text-based format for representing structured
data on javascript object syntax

JSON repressents structured data as a string

JSON.parse() lets you parse JSON
JSON.stringify lets you convert JSON into a string

to populate we can use this:

async function populate() {
  const requestURL =
    "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json";
  const request = new Request(requestURL);

  const response = await fetch(request);
  const superHeroes = await response.json();

  populateHeader(superHeroes);
  populateHeroes(superHeroes);
}

async for an asynchronist task and await 
to wait before the calls to any
async functions
'''