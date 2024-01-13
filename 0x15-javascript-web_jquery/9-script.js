$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data, textStatus) => {
    if (textStatus === 'success') {
    $('DIV#hello').text(data.hello);
    }
});
