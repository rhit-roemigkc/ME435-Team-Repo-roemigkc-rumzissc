import mqtt from './mqtt';

const url = 'mosquitto.csse.rose-hulman.edu';
const topic = 'me435/roemigkc/final';

let options = {
    clientId: 'mqtt_js_client_' + Math.random().toString(16),
    clean: true, // Clean session
    connectTimeout: 4000, // 4 seconds
    username: '', // Optional
    password: '', // Optional
    reconnectPeriod: 1000 // Auto reconnect every 1s
};

const client = mqtt.connect(url,options);
        
client.on('connect', () => {
    client.subscribe(topic, {qos:0}, (err) => {
        if (err) {
            console.log("Subscription Error");}
        else{
            console.log(`Subscribed to topic ${topic}`);
        }
    });
});

client.on('message', (topic, recived) => {
    // get timestamp
    console.log(`Recived message from ${topic}: ${recived}`);
    let date = new Date();
    let timestamp = date.toLocaleTimeString();
    let username = recived[0];
    let message = recived[1];
    // put in text box
    document.querySelector("#chatLog").innerHTML += `<p>${timestamp} - ${username}: ${message}</p>`;
    document.querySelector("#chatLog").scrollTop = document.querySelector("#chatLog").scrollHeight;
});

async function sendMessage(username, message){
    // clear chat box
    document.querySelector("#chatBox").value = "";
    let tosend = [username, message];
    client.publish(topic, `${tosend}`);
}

function main() {
    document.querySelector('#send').onclick = () => {
        //console.log("Message Sent");
        let username = document.querySelector("#username").value;
        let message = document.querySelector("#chatBox").value;
        sendMessage(username, message);   
    };
}

main();