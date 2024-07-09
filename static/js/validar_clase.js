(() => {
  let numero = $('#id_numero')
  let tema = $('#id_encabezado')
  let cuerpo = $('#id_cuerpo')

  $('#form').submit((e) => {
    //numero
    if (numero.val().trim() == '') {
      e.preventDefault()
      $('#error-numero').show()
      numero.addClass('is-invalid')
    } else if (isNaN(numero.val().trim()) || numero.val().trim() < 0) {
      e.preventDefault()
      $('#error-numero-formato').show()
      numero.addClass('is-invalid')
    }

    //objetivo
    if (tema.val().trim() == '') {
      e.preventDefault()
      $('#error-tema').show()
      tema.addClass('is-invalid')
    } else if (tema.val().trim().length > 255) {
      e.preventDefault()
      $('#error-tema-formato').show()
      tema.addClass('is-invalid')
    }

    //orden
    if (cuerpo.val().trim() == '') {
      e.preventDefault()
      $('#error-cuerpo').show()
      cuerpo.addClass('is-invalid')
    }
  })

  numero.keyup(() => {
    numero.removeClass('is-invalid')
    $('#error-numero').hide()
    $('#error-numero-formato').hide()
  })

  cuerpo.keyup(() => {
    cuerpo.removeClass('is-invalid')
    $('#error-cuerpo').hide()
  })

  tema.keyup(() => {
    tema.removeClass('is-invalid')
    $('#error-tema').hide()
    $('#error-tema-formato').hide()
  })


})()
