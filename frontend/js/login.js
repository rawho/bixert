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


signupForm.confirmPassword.addEventListener('keyup', e => {
    const password = signupForm.password.value
    const confirmPassword = signupForm.confirmPassword.value
    if(password === confirmPassword){
        document.getElementById('confirm').className = 'success'
    }
    else{
        
        document.getElementById('confirm').className = 'error'
    }
})