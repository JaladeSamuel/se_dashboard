// Make sure to include the javascript library in your html:
// <script src="https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.min.js" type="text/javascript"></script>

var mqtt;
var host = "54.38.32.137";
var port = 9001;
var topics = {}
var agregator;

function openMQTTConnection(topics, agregatorName) {
    console.log("Connecting to the brooker");
    topics = topics;
    agregator = agregatorName;
    mqtt = new Paho.MQTT.Client(host, port, "js-" + Math.random());

    var options = {
        timeout: 3,
        onSuccess: onConnect,
    };

    mqtt.connect(options);
    mqtt.onMessageArrived = onMessageArrived;

    setCharts(agregatorName);
}

function onConnect() {
    console.log("Connected");
    for (topic of Object.keys(topics)) {
        mqtt.subscribe(topic);
    }
}

function onMessageArrived(message) {
    console.log(message.payloadString);

    var element = document.getElementById(topics[message.destinationName]);
    var values = JSON.parse(message.payloadString);

    if (values["type"] == "degree") {
        element.innerText = (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " °C";
    } else if (values["type"] == "km/h") {
        element.innerText = (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " km/h";
    } else if (values["type"] == "percentage") {
        element.innerText = (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " %";
    } else {
        element.innerText = Math.round((values["value"] + Number.EPSILON) * 100) / 100;
    }

    console.log("Updating: " + agregator + '-' + topics[message.destinationName]);
    addData(agregator + '-' + topics[message.destinationName], '', values["value"])
}
