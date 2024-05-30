// Fetching hello from api

$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  success: function (data) {
    const hello = data.hello;
    $.ajax({
      url: `https://translation.googleapis.com/language/translate/v2?key=YOUR_API_KEY&q=${hello}&source=fr&target=en`,
      method: 'GET',
      success: function (response) {
        const translatedHello = response.data.translations[0].translatedText;
        $('#hello').text(translatedHello);
      }
    });
  }
});
