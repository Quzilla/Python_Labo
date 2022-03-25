from socket import gethostbyname
import gevent
from gevent import socket

hosts = [
    'www.crappytaxidermy.com', 
    'www.walterpottertaxidermy.com',
    'www.antique-taxidermy.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
print(jobs)
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
    
