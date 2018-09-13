#! /usr/bin/env /usr/bin/python3

import os
import sys

import yaml

INPUT="/etc/nginx-redirect/config.yaml"
OUTPUT="/etc/nginx/conf.d/default.conf"

def config(y):
    yield "  server {"
    yield "    listen 80;"
    for host in y['hosts']:
        hostname = host['host']
        yield "    if ($http_host = {}) {{".format(hostname)
        for p in host['patterns']:
            yield "      rewrite {} {} permanent;".format(p['from'], p['to'])
        yield "    }"
    yield "  }"

def genconfig(instr, outstr):
    y = yaml.load(instr)
    data = "\n".join(config(y))
    print("Configuration file is")
    print(data)
    outstr.write(data)

if __name__ =='__main__':
    if os.path.exists(INPUT):
        genconfig(open(INPUT), open(OUTPUT, "w"))
        os.execlp("nginx", "nginx", "-g", "daemon off;")
    else: # for testing
        genconfig(sys.stdin, sys.stdout)
