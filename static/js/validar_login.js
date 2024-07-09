(() => {
  let user = $('#id_username')
  let password = $('#id_password')
  let regex = /^[a-z]+$/

  $('#mostrar').click(() => {
    if (password.attr('type') == 'password') {
      password.attr('type', 'text')
      $('#ojo').addClass('fa-eye-slash')
      $('#ojo').removeClass('fa-eye')
    } else {
      password.attr('type', 'password')
      $('#ojo').addClass('fa-eye')
      $('#ojo').removeClass('fa-eye-slash')
    }
  })

  $('form').submit((e) => {
    //usuario
    if (user.val().trim() == '') {
      e.preventDefault()
      $('#error-user').show()
      user.addClass('is-invalid')
    } else if (!regex.test(user.val())) {
      e.preventDefault()
      $('#error-user-formato').show()
      user.addClass('is-invalid')
    }
    //contrasenna
    if (password.val().trim() == '') {
      e.preventDefault()
      $('#error-password').show()
      password.addClass('is-invalid')
    } else if (password.val().trim().length < 8) {
      e.preventDefault()
      $('#error-password-length').show()
      password.addClass('is-invalid')
    }
  })

  user.keyup(() => {
    user.removeClass('is-invalid')
    $('#error-user').hide()
    $('#error-user-formato').hide()
  })

  password.keyup(() => {
    password.removeClass('is-invalid')
    $('#error-password').hide()
    $('#error-password-length').hide()
  })

})()
