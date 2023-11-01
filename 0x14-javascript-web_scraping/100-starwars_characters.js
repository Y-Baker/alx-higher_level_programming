#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(apiUrl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    body = JSON.parse(body);
    characters = body.characters;
    for (const character of characters) {
      request(character, (err, res, characterBody) => {
        if (!err && res.statusCode === 200) {
          data = JSON.parse(characterBody);
          console.log(data.name);
        }
      })
    }
  }
});
