//wait for DOM to be fully loaded
$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    //fetch json data from the api
    $.getJSON(url, function(data) {
        data.results.forEach(function(movie) {
            $('#list_movies').append('<li>' + movie.title + '</li>');
        });
    });
});
