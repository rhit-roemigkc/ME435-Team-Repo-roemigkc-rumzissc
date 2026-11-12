async function sendMessage(username, message){
    // clear chat box
    document.querySelector("#chatBox").value = "";
    // get timestamp
    let date = new Date();
    let timestamp = date.toLocaleTimeString();
    var xml;
    xml = new XMLHttpRequest();
    // put in text box
    xml.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            document.querySelector("#replyTime").innerHTML = timestamp + " - ";
            document.querySelector("#replyUsername").innerHTML = username + ": ";
            document.querySelector("#replyText").innerHTML = message;
            xml.open("POST","http://137.112.212.209:8080/index.html",true)
        }
    }
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