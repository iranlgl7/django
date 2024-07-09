(() => {
  let asunto = $('#id_sobre')
  let mensaje = $('#id_mensaje')

  $('#form').submit((e) => {
    //sobre
    if (asunto.val().trim() == '') {
      e.preventDefault()
      $('#error-asunto').show()
      asunto.addClass('is-invalid')
    } else if (asunto.val().trim().length > 150) {
      e.preventDefault()
      $('#error-asunto-formato').show()
      asunto.addClass('is-invalid')
    }

    //mensaje
    if (mensaje.val().trim() == '') {
      e.preventDefault()
      $('#error-mensaje').show()
      mensaje.addClass('is-invalid')
    }
  })

  asunto.keyup(() => {
    asunto.removeClass('is-invalid')
    $('#error-asunto').hide()
    $('#error-asunto-formato').hide()
  })

  mensaje.keyup(() => {
    mensaje.removeClass('is-invalid')
    $('#error-mensaje').hide()
  })
})()
