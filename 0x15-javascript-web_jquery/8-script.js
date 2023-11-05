$.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",

    success: function (films) {
        $.each(films.results, function (indexInArray, film) { 
            $('ul#list_movies').append('<li>'+film.title+'</li>');
        });
    }
});
