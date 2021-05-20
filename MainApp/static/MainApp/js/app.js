// dom queries
const chatList = document.querySelector('.chats')
const newChatForm = document.querySelector('.new-chat-form')
const newNameForm = document.querySelector('.update-username')
const updateMsg = document.querySelector('.update-msg')
const channels = document.querySelector('.buttons')
let event_id = document.querySelector('.chatsection').getAttribute('data-event_id')
// add a new chat 
newChatForm.addEventListener('submit', e => {
    e.preventDefault()
    const msg = newChatForm.msg.value.trim()
    chatroom.addChat(msg)
        .then(() => newChatForm.reset())
        .catch(err => console.log(err))
})

// update username 
newNameForm.addEventListener('submit', e => {
    e.preventDefault()
    // update name via chatroom 
    const newName = newNameForm.name.value.trim()
    chatroom.updateName(newName)

    // reset the form
    newNameForm.reset()

    // show then hide the update msg 
    updateMsg.innerHTML = `
    <p> Your name was updated to ${newName} </p>
    `
    setTimeout(() => {
        updateMsg.innerHTML = ``
    }, 3000)

})


// check local storage for a name 
const username = document.querySelector(".chatsection").getAttribute("data-user")

// class instances
const chatUI = new ChatUI(chatList)
const chatroom = new Chatroom(event_id, username)

// get chats and render
chatroom.getChats(data => chatUI.render(data))

// update the channel 
chatUI.clear();
chatroom.updateChannel(event_id)
chatroom.getChats(chat => {
    chatUI.render(chat)
})