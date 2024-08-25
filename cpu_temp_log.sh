#!/bin/bash

echo "$(date),$(vcgencmd measure_temp)" >> /home/pi/Desktop/cotoha/cotoha-weather.github.io/cpu_temp_log.txt

echo "$(date),$(vcgencmd measure_volts)" >> /home/pi/Desktop/cotoha/cotoha-weather.github.io/volt_log.txt