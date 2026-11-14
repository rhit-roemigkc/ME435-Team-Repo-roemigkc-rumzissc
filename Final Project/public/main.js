const usernameInput = document.getElementById("username");
const logInButton = document.getElementById("logIn");
const chatBox = document.getElementById("chatBox");
const sendButton = document.getElementById("send");
const chatLog = document.getElementById("chatLog");
 
let username = null;
 
logInButton.onclick = () => {
    const name = usernameInput.value.trim();
    if (username == null) {
        if (!name) return;
        username = name;
        usernameInput.disabled = true;
        logInButton.disabled = true;
    }
};
 
function displayMessage({ username, text, time }) {
    const line = document.createElement("p");
    const timestamp = new Date(time).toLocaleTimeString();
    const nameSpan = document.createElement("b");
    nameSpan.textContent = username + ":";
 
    line.append(timestamp + " - ", nameSpan, " " + text);
    chatLog.appendChild(line);
    chatLog.scrollTop = chatLog.scrollHeight;
}
 
async function sendMessage() {
    const text = chatBox.value.trim();
    if (!username) {
        alert("Login first to send message");
        return;
    }
    if (!text) return;
 
    chatBox.value = "";
    try {
        await fetch("/send", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, text }),
        });
        poll(); // show it right away instead of waiting for the next tick
    } catch (err) {
        console.error("Send failed:", err);
    }
}
 
sendButton.onclick = sendMessage;
 
let lastId = 0;
let polling = false;
 
async function poll() {
    if (polling) return; // avoid overlapping requests
    polling = true;
    try {
        const res = await fetch(`/messages?after=${lastId}`);
        const newMessages = await res.json();
        for (const m of newMessages) {
            displayMessage(m);
            lastId = m.id;
        }
    } catch (err) {
        console.error("Poll failed:", err);
    } finally {
        polling = false;
    }
}
 
setInterval(poll, 1000);
poll();