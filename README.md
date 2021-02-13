# Sensors EveryWhere

Sensors EveryWhere project.

![](doc/SEW.gif)

# Run the Rust web server

## Dependencies 

- Make sure you have Rust installed in nightly:

`curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh` or download the Windows installer.

 `rustup default nightly`

  - Mosquitto (Broker MQTT) : 
    `sudo apt-get install mosquitto`
    
    `pip3 install paho-mqtt`

# Run the server:

`cd dashboard-web`

`cargo run`

You can now open `localhost:8000` in your browser and you should have access to the dashboard!

# Run all sensors and agregators

Run all simulated local sensors with :
`./start_all_sensors.sh`

Run all agregators with (gnome) : 
`./start_all_agregators.sh`
You can also run the agregators one by one.

The python sensors scripts are executed in background, you can stop them with :
`sudo killall python3`
