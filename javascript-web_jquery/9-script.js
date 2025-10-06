//Ensure the DOM is fully loaded
$(document).ready(function() {

    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

    $.getJSON(url, function(data) {
        $('#hello').text(data.hello);
    });
});