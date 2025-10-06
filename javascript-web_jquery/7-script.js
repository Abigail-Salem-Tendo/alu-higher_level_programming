//fully load DOM
$(document).ready(function() {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    //fetch data from the api
    $.getJSON(url, function(data) {
        $('#character').text(data.name);
    });
});