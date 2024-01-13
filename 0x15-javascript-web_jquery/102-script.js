const ap = 'https://www.fourtonfish.com/hellosalut/';

function Hello (lang) {
  $.get(`${ap}?lang=${lang}`, (data, textStatus) => {
    if (textStatus === 'success' && lang) {
      $('#hello').text(data.hello);
    }
  });
}

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    Hello(lang);
  });
});