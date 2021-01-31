// Make sure to include the javascript library in your html:
// <script src="https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.min.js" type="text/javascript"></script>

var mqtt;
var host = "54.38.32.137";
var port = 9001;
var topics = {}

function openMQTTConnection(topics) {
    console.log("Connecting to the brooker");
    topics = topics;
    mqtt = new Paho.MQTT.Client(host, port, "clientjs");

    var options = {
        timeout: 3,
        onSuccess: onConnect,
    };

    mqtt.connect(options);
    mqtt.onMessageArrived = onMessageArrived;
}

function onConnect() {
    console.log("Connected");
    for (topic of Object.keys(topics)) {
        mqtt.subscribe(topic);
    }
}

function onMessageArrived(message) {
    var element = document.getElementById(topics[message.destinationName]);
    var values = JSON.parse(message.payloadString);

    console.log(values);

    if (values["type"] == "degre") {
        element.innerText = (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " °C";
    } else if (values["type"] == "km/h") {
        element.innerText = (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " km/h";
    } else if (values["type"] == "percentage") {
        element.innerText = (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " %";
    } else {
        element.innerText = Math.round((values["value"] + Number.EPSILON) * 100) / 100;
    }
}
