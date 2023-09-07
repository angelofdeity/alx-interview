#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

function getCharactersFromMovie(movieId) {
  // Define the base URL for the Star Wars API
  const baseUrl = 'https://swapi.dev/api/';

  // Define the endpoint for films
  const filmsEndpoint = `films/${movieId}/`;

  // Send a GET request to the films endpoint
  request(baseUrl + filmsEndpoint, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      const characters = data.characters;

      // Fetch character names using the character URLs
      characters.forEach(characterUrl => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          } else {
            console.error('Error fetching character data:', charError);
          }
        });
      });
    } else {
      console.error('Error fetching film data:', error);
    }
  });
}

getCharactersFromMovie(movieId)
