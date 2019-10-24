# nsd1906_review_day02

网络架构

- 接入层：负责将主机接入网络，主要设备是二层交换机
- 汇聚层：负责VLAN间通信
- 核心层：将局域网流量转发到互联网

所用到的技术：

- VLAN：每间教室是一个VLAN，每个办公区也是一个VLAN。
  - 一教室：VLAN1、192.168.1.0/24
  - 二教室：VLAN2、192.168.2.0/24
  - n教室：VLANn、192.168.n.0/24
  - 办公区：VLAN101
- TRUNK：
- 三层交换：
- 默认路由
- 静态路由：
- ACL：
- VRRP：
- NAT：
- STP：





回答问题的方式：nW1H

- What
- Why
- When
- Where
- How

什么是VLAN？

答：VLAN是虚拟局域网。它最主要的作用是实现广播控制。使用时，首先创建VLAN，再将交换机的端口加入到相关的VLAN。为了实现不同交换机上相同的VLAN通信，需要在交换机之间的端口上创建TRUNK中继。为了实现不同VLAN间通信，需要配置三层交换。


