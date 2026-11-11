async function sendMessage(username, message){
    // clear chat box
    document.querySelector("#chatBox").value = "";
    // get timestamp
    let date = new Date()
    let timestamp = date.toLocaleTimeString();
    
    // put in text box

    document.querySelector("#replyTime").innerHTML = timestamp + " - ";
    document.querySelector("#replyUsername").innerHTML = username + ": ";
    document.querySelector("#replyText").innerHTML = message;
}


function main() {
    console.log("Hello JavaScript!");
    document.querySelector('#send').onclick = () => {
        //console.log("Message Sent");
        let username = document.querySelector("#username").value;
        let message = document.querySelector("#chatBox").value;
        sendMessage(username, message);   
    };
}


main();