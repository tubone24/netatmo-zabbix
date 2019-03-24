# /bin/bash 

MODULE=$1
SENSOR=$2

/bin/python /usr/lib/zabbix/externalscripts/netatmo-api-python/printAllLastDataJson | jq .$MODULE.$SENSOR
