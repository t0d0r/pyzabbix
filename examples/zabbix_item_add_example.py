'''
Created on 01.10.2010

@author: gescheit
'''
from pyzabbix import ZabbixAPI

server="127.0.0.1"
username="api"
password="apipass"

zapi = ZabbixAPI(server=server, path="", log_level=6)
zapi.login(username, password)

host_name="test_host"

hostid=zapi.host.get(filter={"host":host_name})[0]["hostid"]
print hostid

zapi.item.create(hostid=hostid,
                 description='Used disk space on $1 in %' ,
                 key_='vfs.fs.size[/,pused]',
                 )
