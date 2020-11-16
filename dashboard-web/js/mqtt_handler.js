var mqtt;
var reconnectTimeout = 2000;
var host = "54.38.32.137";
var port = 9001;

console.log("connecting to " + host + " " + port);
mqtt = new Paho.MQTT.Client(host, port, "clientjs");

var options = {
    timeout: 3,
    onSuccess: onConnect,
};

mqtt.onMessageArrived = onMessageArrived;
mqtt.connect(options);

function onMessageArrived(message) {
    console.log("onMessageArrived:" + message.payloadString);
    
    const div = document.createElement('div');
    div.className = 'row';

    div.innerHTML = `
    <div class="row">
        <div class="col-sm">
            ${message.payloadString}
        </div>
    </div>
    `;

    document.getElementById('inputs_table').appendChild(div);
}

function onConnect() {
    mqtt.subscribe("rasp/sensors/temperature");
    console.log("Connected");
    // message = new Paho.MQTT.Message("Hello my dudes");
    // message.destinationName = "sensor1";
    // mqtt.send(message);
}