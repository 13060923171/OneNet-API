from flask import * #flask框架一个小型的web服务器
import requests #一个爬虫库，用于爬取数据
import re #正则表达式，用于定位数据

#请求头，可以访问这个页面的参数
headers = {
    #相对于api-key更安全的写法    #由参数组构成的token
    "Authorization":"version=2018-10-31&res=products%2F345759&et=1595403419&method=md5&sign=OfjRoPfzC3l3t2wmXybYfw%3D%3D"
}
#初始化，flask框架，更好的调用
app = Flask(__name__)
#定义温度的最初数据
temperature = 0
humidity = 0
Turang = 0
LED = 0

#添加post,get请求方法
@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:id>', methods=['GET', 'POST'])
def index(id=None):
    global temperature,humidity,Turang,LED
    if request.method == 'POST':
        url = "http://api.heclouds.com/devices/602552665/datapoints?datastream_id=LED&limit=10"
        html = requests.get(url, headers=headers)
        led = html.text
        LED = re.compile('"value":(.*?)}', re.I | re.S)
        result = LED.findall(led)[0]
        LED = result
    #当页面发起一个post请求方法时，执行下面代码
    #温度
        if id == 1:
            if request.method == 'POST':
                #获取温度的URL
                url = "http://api.heclouds.com/devices/602552665/datapoints?datastream_id=temperatrue&limit=10"
                #请求这个页面
                html = requests.get(url, headers=headers)
                #获取下来的数据以文本的形式保存下来
                wendu = html.text
                #用正则表达式，定位数据
                temperature = re.compile('"value":(.*?)}', re.I | re.S)
                #获取最新的数据
                result = temperature.findall(wendu)[0]
                temperature = result
            return render_template('index.html',temperature= temperature,LED = LED)
        #湿度
        if id == 2:
            if request.method == 'POST':
                #获取湿度的URL
                url = "http://api.heclouds.com/devices/602552665/datapoints?datastream_id=humidity&limit=10"
                #请求这个页面
                html = requests.get(url, headers=headers)
                #获取下来的数据以文本的形式保存下来
                shidu = html.text
                #用正则表达式，定位数据
                humidity = re.compile('"value":(.*?)}', re.I | re.S)
                #获取最新的数据
                result = humidity.findall(shidu)[0]
                humidity = result
            return render_template('index.html',humidity = humidity,LED = LED)
        #土壤
        if id == 3:
            if request.method == 'POST':
                #获取土壤的URL
                url = "http://api.heclouds.com/devices/602552665/datapoints?datastream_id=Turang&limit=10"
                #请求这个页面
                html = requests.get(url, headers=headers)
                #获取下来的数据以文本的形式保存下来
                youjifei = html.text
                #用正则表达式，定位数据
                Turang = re.compile('"value":(.*?)}', re.I | re.S)
                #获取最新的数据
                result = Turang.findall(youjifei)[0]
                Turang = result
            return render_template('index.html',Turang= Turang,LED = LED)
    return render_template('index.html')

if __name__ == '__main__':
    #run是运行这个程序，host是可以外部可访问的服务器，debug是调试模式，port是端口的意思
    app.run(host = "0.0.0.0",port=8080,debug=True)
