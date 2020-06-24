# 在flask框架中，外部怎么访问到你的网址

先安装ngrok对应的软件版本[下载地址](https://ngrok.com/download)

然后下载好之后，把对应的exe拉到和flask中exe的同一目录，首先先打开exe文件，运行成功之后，不要关掉

再打开ngrok输入对应的命令

1、ngrok help

2、ngrok http 5000（5000）为你电脑上的端口

然后会返回这一串东西

```bash
Session Status online
Account Grey Li (Plan: Free)
Version 2.2.8
Region United States (us)
Web Interface http://127.0.0.1:4040
Forwarding http://d15a56b1.ngrok.io -> localhost:5000
Forwarding https://d15a56b1.ngrok.io -> localhost:5000

Connections ttl opn rt1 rt5 p50 p90
0 0 0.00 0.00 0.00 0.00
```

其中http://d15a56b1.ngrok.io就是你可以通过外部访问的网址，注意因为你没有注册ngrok所以这个服务器只能开8个小时，8个小时之后又会关掉，到时候你得重新又启动一遍才行

[参考网站](https://zhuanlan.zhihu.com/p/45471645)