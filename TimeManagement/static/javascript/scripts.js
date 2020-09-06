
document.querySelector('html').style.setProperty('--element-height',window.innerHeight+'px');
document.querySelector('html').style.setProperty('--element-width',window.innerWidth*0.21+'px');
document.querySelector('html').style.setProperty('--full-height',window.innerHeight+'px');
document.querySelector('html').style.setProperty('--full-width',window.innerWidth+'px');
document.querySelector('html').style.setProperty('--log-box-width',window.innerWidth*0.24+'px');
document.querySelector('html').style.setProperty('--log-box-height',window.innerHeight*0.20+'px');
document.querySelector('html').style.setProperty('--reg-box-width',window.innerWidth*0.50+'px');
document.querySelector('html').style.setProperty('--reg-box-height',window.innerHeight*0.30+'px');

const selectedot = document.querySelector('.otheropt');
const llist = document.querySelector('.other')
selectedot.addEventListener('click',function addactive () {
   llist.classList.toggle ('active');
});
// კვირების შეცვლა weeksl ;  weeksr
function weeksl() {
    const actweeks = document.querySelectorAll('.day_back.active');
    const inactweeks = document.querySelectorAll('.day_back.inactive');
    for (i=0; i!==actweeks.length; i++){
        if (i === 3) {
            actweeks[i].style.display = 'inline-block';
        }
        else {
            actweeks[i].style.display = 'none';
        }
    }
    for (i=0; i!==inactweeks.length; i++){
        inactweeks[i].style.display = 'inline-block';
    }
}

function weeksr() {
    const actweeks = document.querySelectorAll('.day_back.active');
    const statweeks = document.querySelector('.day_back.active');
    const statinweeks = document.querySelector('.day_back.inactive');
    const inactweeks = document.querySelectorAll('.day_back.inactive');
    for (i=0; i!==actweeks.length; i++){
        actweeks[i].style.display = 'inline-block';
    }
    for (i=0; i!==inactweeks.length; i++){
        inactweeks[i].style.display = 'none';
    }
}



