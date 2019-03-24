# /bin/bash 

MODULE=$1
SENSOR=$2

/bin/python /usr/lib/zabbix/externalscripts/print_all_lastdata_Json.py | jq .$MODULE.$SENSOR
