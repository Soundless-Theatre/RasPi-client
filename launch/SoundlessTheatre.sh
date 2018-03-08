#!/bin/bash
#dir > /opt/SoundlessTheatre.sh
while true
do
    killall python3
    killall python
    bash /home/pi/workspace/RasPi-client/launch/launch.sh >> /home/pi/workspace/RasPi-client/launch/service.log
    sleep 1
done

