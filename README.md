# BSilenceScan

BSlienceScan是一款基于Telnet进行端口扫描的工具，相对Nmap产生的动静会少很多，而且扫描速度极快，配置简单，并且采用线程池降低多线程实现复杂度，便于二次开发。

## 安装 & 运行

使用前先安装python3库`IPy`，运行前配置好`host_list.txt`和`port_list.txt`，然后运行`scan.py`即可。

## 使用

配置文件是`config.ini`, `max_thread_count`为默认配置的3线程，`telnet_timeout`为telnet连接超时时间。

扫描目标配置文件是`host_list.txt`，支持多IP配置

```
192.168.1.0/24
192.168.3.0/24
1.2.3.4
```
扫描目标端口配置文件是`port_list.txt`，支持多段端口配置

```
21-80
3389
4000-5000
```
扫描完成显示结果，基于[Services Name](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?&page=1)显示端口服务：

```
192.168.1.2 port 88 , kerberos --- Kerberos
192.168.1.2 port 445 , microsoft-ds --- Microsoft-DS
192.168.1.2 port 548 , afpovertcp --- AFP over TCP
扫描完成
```


