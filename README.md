# se_dashboard dev branch
Sensors EveryWhere project

# Run the Rust web server

## Dependencies 

- Make sure you have Rust installed in nightly:

`curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh` or download the Windows installer.

 `rustup default nightly`

  - Mosquitto (Broker MQTT) : 
    ```sudo apt-get install mosquitto```
    
    ```pip3 install paho-mqtt```

Run the server:

`cd dashboard-web`

`cargo run`

# To run a sensor 

Make sure you have node js installed (to send image in json format)

Install nodejs packages
Install : pip3 install geocoder

Simply run the python script "python <name of the sensor>.py"

