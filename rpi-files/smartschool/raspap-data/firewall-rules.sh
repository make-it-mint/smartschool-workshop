#!/bin/bash
surfstick=<YOUR-SURFSTICK-OR-ETHERNET-CONNECTION> #default is eth0, the LAN-Port. but when using a Surfstick, it will have a different name
iptables -I DOCKER-USER -i src_if -o dst_if -j ACCEPT
iptables -t nat -C POSTROUTING -o $surfstick -j MASQUERADE || iptables -t nat -A POSTROUTING -o $surfstick -j MASQUERADE
iptables -C FORWARD -i $surfstick -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT || iptables -A FORWARD -i $surfstick -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -C FORWARD -i wlan0 -o $surfstick -j ACCEPT || iptables -A FORWARD -i wlan0 -o $surfstick -j ACCEPT
