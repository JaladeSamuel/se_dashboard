#!/bin/bash
python3 sensors/anemo_sensor.py toulouse &
python3 sensors/hum_sensor.py toulouse &
python3 sensors/temp_ext_sensor.py toulouse &
python3 sensors/indice_uv_sensor.py toulouse &

python3 sensors/anemo_sensor.py london &
python3 sensors/hum_sensor.py london &
python3 sensors/temp_ext_sensor.py london &
python3 sensors/indice_uv_sensor.py london &

python3 sensors/anemo_sensor.py newyork &
python3 sensors/hum_sensor.py newyork &
python3 sensors/temp_ext_sensor.py newyork &
python3 sensors/indice_uv_sensor.py newyork &

python3 sensors/anemo_sensor.py moscou &
python3 sensors/hum_sensor.py moscou &
python3 sensors/temp_ext_sensor.py moscou &
python3 sensors/indice_uv_sensor.py moscou &

python3 sensors/anemo_sensor.py rio &
python3 sensors/hum_sensor.py rio &
python3 sensors/temp_ext_sensor.py rio &
python3 sensors/indice_uv_sensor.py rio &