#!/usr/bin/node

const request = require('request');

function getArgPassed () {
  const arg = process.argv[2];
  try {
    Number(arg);
  } catch (err) {
    console.error(err);
  }
  return arg;
}

async function getRequest (url) {
  let DATA = null;
  const pr = new Promise((resolve, reject) => {
    request(url, function (error, response, body) {
      if (error) {
        reject(error);
      }
      if (response && response.statusCode) {
        DATA = JSON.parse(body);
        resolve(DATA);
      }
    });
  });
  return pr
    .then((data) => data)
    .catch((err) => {
      throw err;
    });
}

async function getFilms (arg) {
  const Url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
  const data = await getRequest(Url);
  return data;
}

async function getCharacters (listOfCharactersUrls) {
  if (!Array.isArray(listOfCharactersUrls)) {
    throw new Error('you need to pass in an array');
  }
  const prs = [];
  for (let x = 0; x < listOfCharactersUrls.length; x++) {
    const prss = new Promise((resolve, reject) => {
      try {
        const data = getRequest(listOfCharactersUrls[x]);
        resolve(data);
      } catch (err) {
        reject(err);
      }
    });
    prs.push(prss);
  }

  const pr = Promise.all(prs);
  return pr
    .then((data) => data)
    .catch((err) => {
      throw err;
    });
}

async function MainEntry () {
  const films = await getFilms(getArgPassed());
  const characters = await getCharacters(films.characters);
  for (const character of characters) {
    console.log(character.name);
  }
}

MainEntry();
