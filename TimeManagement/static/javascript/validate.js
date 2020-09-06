document.querySelector('html').style.setProperty('--full-height',window.innerHeight+'px');
document.querySelector('html').style.setProperty('--full-width',window.innerWidth+'px');
document.querySelector('html').style.setProperty('--log-box-width',window.innerWidth*0.24+'px');
document.querySelector('html').style.setProperty('--log-box-height',window.innerHeight*0.20+'px');
document.querySelector('html').style.setProperty('--reg-box-width',window.innerWidth*0.50+'px');
document.querySelector('html').style.setProperty('--reg-box-height',window.innerHeight*0.30+'px');

const username=document.getElementById('username');
    const password=document.getElementById('password1');
    const conf_password=document.getElementById('password2');
    const reg_form=document.getElementById('reg_form');
    const errorElement = document.getElementById('error');

    reg_form.addEventListener('submit',(e) => {
    let errors = [];
    let save_doc='0';
    if (username.value.length < 4 ) {
        errors.push('Username must be more than 4 characters');
    }
    if (password.value.length < 6) {
        errors.push('Password must be more than 6 characters');
    }
    if (password.value !== conf_password.value) {
        errors.push('Confirmation password is not equal to password');
    }
    if (password.value === username.value) {
        errors.push('Password and username must be different')
    }
    if (errors.length > 0) {
        e.preventDefault();
        document.querySelector('.errors').style.setProperty('display','block');
        errorElement.innerText = errors.join(', ');
        save_doc='0';
    }
    else {
        save_doc='1';
    }
    });


