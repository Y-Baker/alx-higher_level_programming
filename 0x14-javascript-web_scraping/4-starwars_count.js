#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const character = { id: 18, name: 'Wedge Antilles' };
const characterApi = `https://swapi-api.alx-tools.com/api/people/${character.id}/`;

request(apiUrl, (err, res, body) => {
  if (!err && res.statusCode === 200) {
    body = JSON.parse(body);
    let count = 0;
    for (const film of body.results) {
      if (film.characters.includes(characterApi)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
