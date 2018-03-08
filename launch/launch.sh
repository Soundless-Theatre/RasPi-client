#!/bin/bash

echo "process start,start,starstart,start,startstart,start,startstart,start,startstart,start,start"

killall python3
killall create_ap
nmcli dev connect wlan0
python3 /home/pi/workspace/RasPi-client/launch/led_green.py &
python3 /home/pi/workspace/RasPi-client/recv.py &

mode="send"
send="send"

while true
do
    sleep 0.1
    if $(python3 /home/pi/workspace/RasPi-client/launch/check.py);then
        sleep 2
        python3 /home/pi/workspace/RasPi-client/launch/led_all.py &
        if $(python3 /home/pi/workspace/RasPi-client/launch/check.py);then
            echo "butonn pushed button pushed button pushed button pushed button pushed"
            if [ $mode = $send ]; then
                echo "setting mode start setting mode start setting mode start setting mode start"
                killall python3 &
                killall python3 &
                killall python3
                python3 /home/pi/workspace/RasPi-client/setting/lis.py
                nmcli device disconnect wlan0
                create_ap -n --no-virt wlan0 SoundessTheatreSetting hogepiyofuga &
                sleep 10
                cd /home/pi/workspace/RasPi-client/setting
                python3 -m http.server 80 &
                cd /home/pi/workspace/RasPi-client/launch
                python3 /home/pi/workspace/RasPi-client/setting/web_api.py &
                sleep 1
                python3 /home/pi/workspace/RasPi-client/launch/led_red.py &
                mode="set"
            else
                killall python3
                killall create_ap
                sleep 5 
                nmcli dev connect wlan0
                python3 /home/pi/workspace/RasPi-client/setting/connect.py
                echo "recv mode start recv mode start recv mode start recv mode start"
                killall python3 
                killall python3 &
                killall python3 
                python3 /home/pi/workspace/RasPi-client/launch/led_green.py &
                python3 /home/pi/workspace/RasPi-client/recv.py &
                
                mode="send"
            fi
        fi
    fi
done
