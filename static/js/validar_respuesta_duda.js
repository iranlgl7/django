
(() => {
  let mensaje = $('#id_mensaje')

  $('#form').submit((e) => {
    //mensaje
    if (mensaje.val().trim() == '') {
      e.preventDefault()
      $('#error-mensaje').show()
      mensaje.addClass('is-invalid')
    }
  })

  mensaje.keyup(() => {
    mensaje.removeClass('is-invalid')
    $('#error-mensaje').hide()
  })
})()
