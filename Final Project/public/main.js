import mqtt from 'https://cdn.jsdelivr.net/npm/mqtt@5.10.1/+esm';

const URL = "ws://broker.hivemq.com";
const TOPIC = "me435/roemigkc/final";


let client = null;
let username = null;

// const $ = (sel) => document.querySelector(sel);

// Helper function to add a line to the chat log
function addChatLine(text){
    const p = document.createElement("p");
    p.textContent = text;
    document.querySelector("#chatLog").appendChild(p);
    document.querySelector("#chatLog").scrollTop = document.querySelector("#chatLog").scrollHeight;
}


async function sendMessage(username, message){
    
    if (!client || !client.connected) {
        addChatLine("Not connected. Log in first.");
    return;
    }
    if (!message.trim()) return;

    const payload = JSON.stringify({username, message});
    await client.publishAsync(TOPIC, payload, { qos: 0});

    document.querySelector("#chatBox").value = ""; //clear only after success
}

function logIn(){
    username = document.querySelector("#username").value.trim();
    if (!username) return addChatLine("Enter user first.");
    if (client) client.end(true);

    let options = {
        clientId: 'mqtt_js_client_' + Math.random().toString(16),
        clean: true, // Clean session
        connectTimeout: 4000, // 4 seconds
        username: '', // Optional
        password: '', // Optional
        reconnectPeriod: 1000 // Auto reconnect every 1s
    };

    client = mqtt.connect(URL, options);

    client.on("connect", () => {
        addChatLine(`connected as ${username}`);
         client.subscribe(TOPIC, { qos: 0 }, (err) => {
            if (err) console.error("Subscription error", err);
            else console.log(`Subscribed to ${TOPIC}`);
        });
    });

    client.on("message", (topic, received) => {
        let data;
        try {
        data = JSON.parse(received.toString());   // Buffer -> string -> object
        } catch {
        return console.warn("Ignoring non-JSON message:", received.toString());
        }
        const time = new Date().toLocaleTimeString();
        addChatLine(`${time} - ${data.username}: ${data.message}`);
    });

    client.on("error", (e) => addChatLine("Error: " + e.message));
    client.on("close", () => console.log("Connection closed"));

}

function main() {
    document.querySelector("#logIn").onclick = logIn;
    document.querySelector("#send").onclick = () => sendMessage(document.querySelector("#username").value,document.querySelector("#chatBox").value);

    // Bonus: send on Enter
    document.querySelector("#chatBox").addEventListener("keydown", (e) => {
    if (e.key === "Enter") sendMessage(document.querySelector("#chatBox").value);
  });
}

main();