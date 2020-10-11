

var recaptcha = document.querySelector('.g-recaptcha');

var signin_form = document.querySelector('.signin_form');

function recaptcha_scale() {
    if (signin_form.offsetWidth < 304) {
        var x = signin_form.offsetWidth/314;
        recaptcha.style.transform = 'scale('+x+')';
    }
}

recaptcha_scale()
// window.addEventListener('resize', recaptcha_scale)
