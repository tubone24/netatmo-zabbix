# netatmo-zabbix

## Install

First, you install netatmo-api-python(https://github.com/philippelt/netatmo-api-python)

```
pip install lnetatmo
```

And you put 2file below for `zabbix external scripts`

```
git clone https://github.com/tubone24/netatmo-zabbix
cp netatmo-zabbix/zabbix-netatmo.sh /usr/lib/zabbix/externalscripts/
cp netatmo-zabbix/print_all_lastdata_Json.py /usr/lib/zabbix/externalscripts/
```

And also, change files permission and owner

```
sudo -i
cd /usr/lib/zabbix/externalscripts/
chown zabbix. zabbix-netatmo.sh
chown zabbix. print_all_lastdata_Json.py
chmod +x zabbix-netatmo.sh
chmod +x print_all_lastdata_Json.py
```

Enjoy
