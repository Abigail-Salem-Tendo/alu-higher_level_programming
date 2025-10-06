// wait for DOM to be fully loaded
$(document).ready(function() {
    //add event handler to the div
    $('#update_header').click(function() {
        $('header').text('New Header!!!');
    });
});