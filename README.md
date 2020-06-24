# OneNet-API
怎么用python的flask框架来调用onenet平台上的API来实现数据交互，实现物联网之智能农业监测系统



首先第一步我们得获取onenet给我们提供的API才行

[onenet平台](https://open.iot.10086.cn/doc/)

![](https://s1.ax1x.com/2020/06/24/NwFi5Q.png)

注意一点获取的header的格式是这种

```python
headers = {
    #相对于api-key更安全的写法    #由参数组构成的token
    "Authorization":"version=2018-10-31&res=products%2F345759&et=1595403419&method=md5&sign=OfjRoPfzC3l3t2wmXybYfw%3D%3D"
}
```

header的值要用token来获取



那个url值是应用开发指南-API-MQTT-查询设备历史数据的案例来进行获取的

[具体例子](https://www.bilibili.com/video/BV16Z4y1x7Zx?from=search&seid=7232676395792337925)