var mqtt;
var host = "54.38.32.137";
var port = 9001;
var topics = {}

function openAlertsConnection(topics) {
    console.log("Connecting to the brooker");
    topics = topics;
    mqtt = new Paho.MQTT.Client(host, port, "js-" + Math.random());

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
    console.log(message.payloadString);
    var values = JSON.parse(message.payloadString);
    sensor = topics[message.destinationName];
    topic = message.destinationName;

    if (values["type"] == "degree") {
        if (values["value"] > 100) {
            addAlert("danger", "Sensor: " + sensor + " Topic: " + topic + " " + (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " °C");
        } else if (values["value"] > 80) {
            addAlert("warning", "Sensor: " + sensor + " Topic: " + topic + " " + (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " °C");
        }
    } else if (values["type"] == "km/h") {
        if (values["value"] > 150) {
            addAlert("danger", "Sensor: " + sensor + " Topic: " + topic + " " + (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " km/h");
        } else if (values["value"] > 100) {
            addAlert("warning", "Sensor: " + sensor + " Topic: " + topic + " " + (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " km/h");
        }
    } else if (values["type"] == "percentage") {
        if (values["value"] > 70) {
            addAlert("danger", "Sensor: " + sensor + " Topic: " + topic + " " + (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " %");
        } else if (values["value"] > 85) {
            addAlert("warning", "Sensor: " + sensor + " Topic: " + topic + " " + (Math.round((values["value"] + Number.EPSILON) * 100) / 100).toString() + " %");
        }
    }
}

function addAlert(type, message) {
    var alerts = document.getElementById("alerts");
    let newAlert = document.createElement("div");
    newAlert.setAttribute("role", "alert");

    if (type == "danger") {
        newAlert.setAttribute("class", "alert alert-danger");
        newAlert.innerText = "[Danger] " + message;
    } else if (type == "warning") {
        newAlert.setAttribute("class", "alert alert-warning");
        newAlert.innerText = "[Warning] " + message;
    }

    alerts.appendChild(newAlert);
}