const loginContainer = document.querySelector('.login-container')
const signupContainer = document.querySelector('.signup-container')
const loginBtn = document.querySelector('.login')
const signupBtn = document.querySelector('.register')
const closeBtnLogin = document.querySelector('.close-login')
const closeBtnSignup = document.querySelector('.close-signup')
const outerContainerLogin = document.querySelector('.container')
const outerContainerSignup = document.querySelector('.container_')

const toSignupBtn = document.querySelector('#signup__')
const toLoginBtn = document.querySelector('#login__')


const signupForm = document.querySelector('.signup-form')

const passPattern = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,}$/

const feedback = document.querySelector('.feedback')


const close = (innercontainer, outercontainer) => {
    innercontainer.classList.remove('open')
    innercontainer.classList.add('close')
    outercontainer.style.display = 'none'
}

const open = (innercontainer, outercontainer) => {
    if (innercontainer.classList.contains('close')) {
        innercontainer.classList.remove('close')
        innercontainer.classList.add('open')
    } else {
        innercontainer.classList.add('open')
    }
    outercontainer.style.display = 'flex'
}

loginBtn.addEventListener('click', () => {
    open(loginContainer, outerContainerLogin)
})
signupBtn.addEventListener('click', () => {
    open(signupContainer, outerContainerSignup)
})

closeBtnLogin.addEventListener('click', () => {
    close(loginContainer, outerContainerLogin)
})

closeBtnSignup.addEventListener('click', () => {
    close(signupContainer, outerContainerSignup)
})

toSignupBtn.addEventListener('click', () => {
    close(loginContainer, outerContainerLogin)
    open(signupContainer, outerContainerSignup)
    
})

toLoginBtn.addEventListener('click', () => {
    close(signupContainer, outerContainerSignup)
    open(loginContainer, outerContainerLogin)
})

signupForm.password.addEventListener('keyup', e => {
    const password = signupForm.password.value
    if(passPattern.test(password)){
        document.getElementById('password').className = 'success'
        feedback.innerHTML = ``;

    } else{
        feedback.innerHTML = `
            <ul>
                <li> Min 5 characters </li>
                <li> Atleast one small letter </li>
                <li> Atleast one capital leter </li>
                <li> Atleast one number </li>
            </ul>
        `;
        document.getElementById('password').className = 'error'

    }
})

signupForm.confirmPassword.addEventListener('keyup', e => {
    const password = signupForm.password.value
    const confirmPassword = signupForm.confirmPassword.value
    if(password === confirmPassword && passPattern.test(confirmPassword)){
        document.getElementById('confirm').className = 'success'
        document.querySelector('#signup').classList.remove('disabled')
        document.querySelector('#signup').removeAttribute('disabled')
    }
    else{
        
        document.getElementById('confirm').className = 'error'
        document.querySelector('#signup').classList.add('disabled')
        document.querySelector('#signup').setAttribute('disabled')

    }
})