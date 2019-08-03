# nsd1903_python1_day04

python官方手册页：https://docs.python.org/zh-cn/3/ -> 标准库参考

## shutil模块

主要实现复制、移动等操作

```python
import shutil

# 拷贝文件对象的方式，了解
f1 = open('/etc/passwd', 'rb')
f2 = open('/tmp/mima', 'wb')

shutil.copyfileobj(f1, f2)
f1.close()
f2.close()

# 直接拷贝文件 
>>> shutil.copyfile('/etc/shadow', '/tmp/sd')
'/tmp/sd'

# 将文件拷贝到目标目录，或指定目标位置及名字，常用
>>> shutil.copy('/etc/hosts', '/tmp/')
'/tmp/hosts'
>>> shutil.copy('/etc/hosts', '/tmp/zhuji.txt')
'/tmp/zhuji.txt'

# copy2相当于是cp -p  ， 常用
>>> shutil.copy2('/etc/hosts', '/tmp/zhj')
'/tmp/zhj'

# cp -r /etc/security /tmp/anquan， 常用
>>> shutil.copytree('/etc/security', '/tmp/anquan')
'/tmp/anquan'

# mv /tmp/anquan /var/tmp/anquan
>>> shutil.move('/tmp/anquan', '/var/tmp/anquan')
'/var/tmp/anquan'

# chown
>>> shutil.chown('/tmp/mima', user='bob', group='bob')

# rm -rf 
>>> shutil.rmtree('/var/tmp/anquan')
```

## subprocess模块

用于执行系统命令。

```python
# 在shell环境中执行命令ls ~
>>> subprocess.run('ls ~', shell=True)

>>> result = subprocess.run('ls abcd', shell=True)
ls: 无法访问abcd: 没有那个文件或目录
>>> result.returncode   # returncode就是$?
2

# 将输出保存到stdout中，将错误保存到stderr中
>>> result = subprocess.run('id root; id john', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> result.stdout
b'uid=0(root) gid=0(root) \xe7\xbb\x84=0(root)\n'
>>> result.stderr
b'id: john: no such user\n'

```










