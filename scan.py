#coding: utf-8

import telnetlib
import time
import json
import configparser
from concurrent.futures import ThreadPoolExecutor
from Verification import HostTool
from IPy import IP #ip使用 https://github.com/autocracy/python-ipy

telnet_tasks = set()
port_to_servies = {}

def get_ip_port_status(ip,port,tel_timeout=3):
    server = telnetlib.Telnet()
    try:
        server.open(ip,port,tel_timeout)
        item = port_to_servies[str(port)]
        print('{0} port {1} , {2} --- {3}'.format(ip,port,item["short_desc"],item["detail_desc"]))
    except Exception as err:
        # print('{0} port {1} is not open'.format(ip, port))
        pass
    finally:
        server.close()
        task_key = ip + ":" + str(port)
        if task_key in telnet_tasks:
            telnet_tasks.remove(task_key)

def get_hosts():
    # 读取文件
    file_hosts = []
    f = open("host_list.txt","r")
    line = f.readline()
    while line:
        if len(line) > 0:
            host = line.replace("\n", "").replace(" ", "")
            if HostTool.is_valid_domain(host):
                file_hosts.append(host)
            else:
                ips = IP(host)
                nIPs = list(map(lambda x:str(x),ips))
                file_hosts += nIPs
        line = f.readline()
    f.close()
    return set(file_hosts)

def get_ports():
    # 读取文件
    ports = []
    f = open("port_list.txt","r")
    line = f.readline()
    while line:
        if len(line) > 0:
            port = HostTool.get_ports(line.replace("\n", "").replace(" ", ""))
            ports += port
        line = f.readline()
    f.close()
    return ports

def get_port_services():
    data = {}
    f = open("service_port.txt","r")
    data = json.loads(f.read())
    f.close()
    return data

if __name__ == '__main__':
    # 读取数据
    hosts = get_hosts()
    ports = get_ports()
    port_to_servies = get_port_services()

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read("config.ini")
    max_thread_count = int(config.get("Thread","max_thread_count"))
    telnet_timeout = float(config.get("Thread","telnet_timeout"))

    # 开启线程池
    telnet_pool = ThreadPoolExecutor(max_thread_count)

    for host in hosts:
        for port in ports:
            task_key = host + ":" + str(port)
            telnet_tasks.add(task_key) # 线程池会有读写问题？
            task = telnet_pool.submit(get_ip_port_status(host, port, telnet_timeout))

    while True:
        time.sleep(1)
        if len(telnet_tasks) == 0:
            print("扫描完成")
            break
