
(() => {
  let numero = $('#id_numero')
  let objetivo = $('#id_objetivoEvaluar')
  let orden = $('#id_orden')

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
    if (objetivo.val().trim() == '') {
      e.preventDefault()
      $('#error-objetivo').show()
      objetivo.addClass('is-invalid')
    } else if (objetivo.val().trim().length > 255) {
      e.preventDefault()
      $('#error-objetivo-formato').show()
      objetivo.addClass('is-invalid')
    }

    //orden
    if (orden.val().trim() == '') {
      e.preventDefault()
      $('#error-orden').show()
      orden.addClass('is-invalid')
    }
  })

  numero.keyup(() => {
    numero.removeClass('is-invalid')
    $('#error-numero').hide()
    $('#error-numero-formato').hide()
  })

  orden.keyup(() => {
    orden.removeClass('is-invalid')
    $('#error-orden').hide()
  })

  objetivo.keyup(() => {
    objetivo.removeClass('is-invalid')
    $('#error-objetivo').hide()
    $('#error-objetivo-formato').hide()
  })


})()
