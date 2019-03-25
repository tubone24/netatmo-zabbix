# netatmo-zabbix

Collect your Netatmo datas, and plot by zabbix

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

## How to use

netatmo.sh needs 2 auguments, module name and sensor value name.

Like that.

```
./netatmo.sh rainfall Rain
```

A module name is that you deside netatmo admin console.

A sensor value name is below.

```
{
  "rainfall": {
    "sum_rain_24": 0,
    "rf_status": 48,
    "sum_rain_1": 0,
    "battery_vp": 6386,
    "When": "00:18:03",
    "Rain": 0
  },
  "windspeed": {
    "WindStrength": 1,
    "GustAngle": 51,
    "rf_status": 55,
    "date_max_wind_str": 1553440683,
    "max_wind_str": 2,
    "max_wind_angle": 51,
    "GustStrength": 2,
    "When": "00:18:03",
    "battery_vp": 6307,
    "WindAngle": 90
  },
  "Indoor": {
    "Noise": 44,
    "Temperature": 21.6,
    "temp_trend": "stable",
    "When": "00:18:07",
    "Humidity": 32,
    "Pressure": 1017.8,
    "CO2": 897,
    "date_max_temp": 1553439782,
    "AbsolutePressure": 1010.3,
    "pressure_trend": "up",
    "min_temp": 21.6,
    "date_min_temp": 1553440083,
    "wifi_status": 48,
    "max_temp": 21.7
  },
  "Outdoor": {
    "date_min_temp": 1553440349,
    "rf_status": 66,
    "Temperature": 9.2,
    "date_max_temp": 1553439733,
    "min_temp": 9.2,
    "temp_trend": "stable",
    "battery_vp": 5016,
    "max_temp": 9.3,
    "When": "00:17:37",
    "Humidity": 38
  }
}
```

## How to create Zabbix Screen

Use `externalscript`

### 1st: Create externalscript metrics

Setting externalscript key like below.

```
netatmo.sh["Outdoor", "Humidity"]
```


