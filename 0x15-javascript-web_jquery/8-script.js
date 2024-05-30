// Fetch  with ajax()

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  success: function (data) {
    $.each(data.results, function (index, movie) {
      ('#list_movies').append(`<li>${movie.title}</li>`);
    });
  }
});
