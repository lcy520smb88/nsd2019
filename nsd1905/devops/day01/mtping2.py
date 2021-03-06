import subprocess
import threading

class Ping:
    def __call__(self, host):
        result = subprocess.run('ping -c2 %s &> /dev/null' % host, shell=True)
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ('172.40.63.%s' % i for i in range(1, 255))
    for ip in ips:
        # target是Ping的一个实例
        t = threading.Thread(target=Ping(), args=(ip,))
        # 启动线程，就是target(*args)
        t.start()
