// render chat templates to the DOM 
// clear the list of chats (when the room changes)
let image_url = document.querySelector('.chatsection').getAttribute('data-image')
// const username_1 = document.querySelector(".chatsection").getAttribute("data-user")
class ChatUI {
    constructor(list) {
        this.list = list;
    }

    clear(){
        this.list.innerHTML = '';
    }

    render(data){
        const when = dateFns.distanceInWordsToNow(
            data.created_at.toDate(),
            { addSuffix: true }
        )
        let div = document.createElement('div')
        div.setAttribute('class', 'chat')
        if(username == data.username){
            div.classList.add('right')   
        }
        else{
            div.classList.add('left')
        }
        div.innerHTML = `
            <div class="user-dets">
                <img src="https://img.icons8.com/cotton/64/000000/user-male--v4.png"/>
                <p>${data.username}</p>
                
            </div>
            <p>${data.msg}</p>
            <p class="time">${when}</p>
        `
        
        this.list.prepend(div) 
    }
}