$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, textStatus) => {
  if (textStatus === 'success') {
    for (const coun of data.results) {
        $('#list_movies').append(`<li>${coun.title}</li>`);
    }
  }
});