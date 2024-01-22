#!/usr/bin/node
const request = require('request');

function printMovieCharacters(movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error:', error || `Status Code: ${response.statusCode}`);
      return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Fetch and print character names
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error('Error fetching character:', error || `Status Code:
            ${response.statusCode}`);
        }
      });
    });
  });
}
const argv = process.argv;
printMovieCharacters(argv);
