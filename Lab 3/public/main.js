async function sendCommand(command){
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    
    console.log(replyText)
    document.querySelector("#replyText").innerHTML = replyText;
    return replyText
}

function main() {
    console.log("Hello JavaScript!");
    document.querySelector('#reset').onclick = () => {
        console.log("You pressed the button!");
        sendCommand("RESET");
    };
    //X-AXIS
    document.querySelector('#x1').onclick = () => {
        sendCommand("X-AXIS 1");
    };
    document.querySelector('#x2').onclick = () => {
        sendCommand("X-AXIS 2");
    };
    document.querySelector('#x3').onclick = () => {
        sendCommand("X-AXIS 3");
    };
    document.querySelector('#x4').onclick = () => {
        sendCommand("X-AXIS 4");
    };
    document.querySelector('#x5').onclick = () => {
        sendCommand("X-AXIS 5");
    };
    //Z-AXIS
    document.querySelector('#ext').onclick = () => {
        sendCommand("Z-AXIS EXTEND");
    };
    document.querySelector('#ret').onclick = () => {
        sendCommand("Z-AXIS RETRACT");
    };
    //GRIPPER
    document.querySelector('#open').onclick = () => {
        sendCommand("GRIPPER OPEN");
    };
    document.querySelector('#close').onclick = () => {
        sendCommand("GRIPPER CLOSE");
    };
    document.querySelector('#status').onclick = () => {
        sendCommand("LOADER_STATUS");
    };

    document.querySelector('#move').onclick = () => {
        let startPos = document.querySelector("#moveFrom").value;
        let endPos = document.querySelector("#moveTo").value;
        console.log("You MOVED!");
        sendCommand(`MOVE ${startPos} ${endPos}`);
    };

}


main();