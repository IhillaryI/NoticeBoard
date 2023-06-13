console.log("Now you see me")

const register = document.getElementById('register');
const login = document.getElementById('login');
const guest = document.getElementById('guest');
const email = document.getElementById('email');
const pass = document.getElementById('pass');
const form = document.getElementById('form');

login.addEventListener('click', function (e) {
    form.action = '/login';
})

register.addEventListener('click', function (e) {
   form.action = '/register'
})


guest.addEventListener('click', (e) => {
    email.value = "Guest@guest.com"
    pass.value = "Guest"
    form.action = '/guest'
})
