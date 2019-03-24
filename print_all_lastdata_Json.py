#!/bin/python
# -*- coding: utf-8 -*-

import time
import json
import lnetatmo

authorization = lnetatmo.ClientAuth()
devList = lnetatmo.DeviceList(authorization)

module_dict = {}

for module, moduleData in devList.lastData(exclude=3600).items() :
    sensor_dict = {}
    for sensor, value in moduleData.items() :
        if sensor == "When" : value = time.strftime("%H:%M:%S",time.localtime(value))
        sensor_dict.update({sensor: value})
    module_dict.update({module: sensor_dict})

print(json.dumps(module_dict))
