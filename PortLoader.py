#coding: utf-8

import csv
import json

def mergeName(first,second):
    if first == second:
        return first
    return first + ", " + second

port_services = {}

with open('service-names-port-numbers.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        key = row[1]
        if key in port_services.keys():
            short_desc = mergeName(row[0], port_services[key]["short_desc"])
            detail_desc = mergeName(row[3], port_services[key]["detail_desc"])
            protocol = mergeName(row[2], port_services[key]["protocol"])
            port_services[key]["short_desc"] = short_desc
            port_services[key]["detail_desc"] = detail_desc
            port_services[key]["protocol"] = protocol
        else:
            item = {}
            item["short_desc"] = row[0]
            item["detail_desc"] = row[3]
            item["protocol"] = row[2]
            port_services[key] = item

port_services_json = json.dumps(port_services)

f = open("service_port.txt","w")
f.write(port_services_json)
f.close()