#coding: utf-8
import re

class HostTool:

    def is_valid_domain(value):
        """
        Return whether or not given value is a valid domain.
        If the value is valid domain name this function returns ``True``, otherwise False
        :param value: domain string to validate
        """
        pattern = re.compile(
            r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
            r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
            r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
            r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
        )

        return True if pattern.match(value) else False

    def get_ports(port_str=""):
        n_ports = []
        if port_str.find("-") >= 0:
            the_ports = port_str.split("-")
            begin = int(the_ports[0])
            end = int(the_ports[1])
            if begin > end:
                return  n_ports
            for i in range(begin,end):
                n_ports.append(i)
        else:
            n_ports.append(int(port_str))
        return n_ports