const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const message_body = $('#main-chat')
let wsStart = "ws://"

if(window.location.protocol === 'https:'){
    wsStart = 'wss://'
}
const socket = new WebSocket(
    wsStart
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED : ",e);
    $('#ChatForm').on('submit',function(e){
        e.preventDefault()
    let message = $('#InputMessage').val()
    socket.send(JSON.stringify({
        'message':message,
        'username':message_username
    }));
    $(this)[0].reset()
})
    
}

socket.onclose =  function(e){
    console.log("CONNECTION LOST");
}

socket.onerror = async function(e){
    console.log("ERROR OCCURED");
}

socket.onmessage =  function(e){
    console.log(e.data)
    const data = JSON.parse(e.data)
    appendMessage(data.message,data.username)

}
time = formatAMPM(new Date)

function appendMessage(message,data_user){
    if(message){
        let message_append;
        if(data_user==message_username){
        message_append = `<li class="repaly">
        <p> ${message}</p>
        <span class="time">${time}</span>
        </li>
        </ul>
        </div>`
    }
    else{
        message_append = `<li class="sender">
        <p> ${message}</p>
        <span class="time">${time}</span>
        </li>
        </ul>
        </div>`      
    }
        message_body.append(message_append)
        $('#message-container').animate({
            scrollTop: $(document).height()
        }, 100);
}
}
function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm.toUpperCase();
    return strTime;
  }

