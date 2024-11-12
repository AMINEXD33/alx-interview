#!/usr/bin/node

const request = require("request");

function getArgPassed() {
    let arg = process.argv[2];
    try {
        const tryNum = Number(arg);
    } catch (err) {
        console.error(err);
    }
    return arg;
}

async function getRequest(url) {
    let DATA = null;
    let pr = new Promise((resolve, reject) => {
        request(url, function(error, response, body) {
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

async function getFilms(arg) {
    const Url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
    let data = await getRequest(Url);
    return data;
}

async function getCharacters(listOfCharactersUrls) {
    if (!Array.isArray(listOfCharactersUrls)) {
        throw "you need to pass in an array";
    }
    let prs = [];
    for (let x = 0; x < listOfCharactersUrls.length; x++) {
        let prss = new Promise((resolve, reject) => {
            try {
                let data = getRequest(listOfCharactersUrls[x]);
                resolve(data);
            } catch (err) {
                reject(err);
            }
        });
        prs.push(prss);
    }

    let pr = Promise.all(prs);
    return pr
        .then((data) => data)
        .catch((err) => {
            throw err;
        });
}

async function MainEntry() {
    let films = await getFilms(getArgPassed());
    let characters = await getCharacters(films["characters"]);
    for (let character of characters) {
        console.log(character["name"]);
    }
}

MainEntry();