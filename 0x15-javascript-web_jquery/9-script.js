$(document).ready(function () {
    $.ajax({
        type: "GET",
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        success: function (response) {
            $('div#hello').text(response.hello);
        }
    });
});
