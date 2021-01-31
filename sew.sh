#!bin/bash

gnome-terminal -x "python sensors/anemo_sensor.py"
gnome-terminal -x "python sensors/hum_sensor.py"
gnome-terminal -x "python sensors/temp_ext_sensor.py"
gnome-terminal -x "python sensors/indice_uv_sensor.py"

cd dashboard-web

gnome-terminal -e "google-chrome http://localhost:8000"

cargo run

