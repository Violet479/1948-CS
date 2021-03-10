#杜叶Violet ID20194201006 陈柱颖Freddie ID20194201020
# API doc: https://cutt.ly/api-documentation/cuttly-links-api
# API Key: https://cutt.ly/edit

# Usage: <cmd> full_long_url [short_name]
# Output: Shortened URL: https://cutt.ly/short_name

import requests  # 调用两个软件包
import sys

print("--- 命令行参数:", sys.argv) #输出你给的的参数
# print(len(sys.argv) )
if len(sys.argv) < 2: #判断语句，
    # expect 2 or 3 arguments: cmd, url, [short name]
    print(f"用法: {sys.argv[0]} full_long_url [short_name]") #提示正确的用法  启动程序的时候给它两个（或者3个参数）
    exit(1) #退出

# get the URL you want to shorten from cmd line,第二个参数，存放到url这个变量里
url = sys.argv[1]

api_key = "8905a4bfd4114cbf791e1a8dc1bc0c46787f0" #访问一台数据库服务器的API，它会要求你提供凭据。这个凭据，是一个字符串密码

# construct the API URL to call 
if len(sys.argv) >= 3: #判断参数是否大于或等于三个
    # user provided the preferred short name 
    short_name = sys.argv[2] #第二个参数放在short name里面 
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}&name={short_name}" #分别构建api_url
else:
    # user didnot provide the short name. 
    api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"#分别构建api_url

print("--- api_url: ", api_url) #api_url打印出来构建好的aqi_url

# make the request 把向服务器请求来的数据放在data变量里 
data = requests.get(api_url).json()["url"] #网页的返回类型实际上是str类型，但是他很特殊，是JSON格式的。所以，如果想直接解析返回结果得到一个字典格式的话，可以直接调用json（）方法

print ("--- data: ", data) #输出data变量

if data["status"] == 7: #判断请求的结果 
    # OK, get shortened URL
    shortened_url = data["shortLink"]
    
    print("--- Shortened URL:", shortened_url)  #若成功，输出 缩短了的url
else:
    print("[!] Error Shortening URL:", data) #不成功，提示错误信息
    #https://example.com/assets/guangxi/nannin/medical_school/my_cs2_1948/exercises/project1/qqqwwweeerrrttt1234561222978