import requests
import time
import datetime


def get_stadiums_info(_token):
    header = {
        'Host': 'wechat.njupt.edu.cn',
        'xweb_xhr': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c0f)XWEB/11275',
        'token': _token,
        'content-type': 'application/json',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://servicewechat.com/wx3bb0b520a9e56a99/301/page-frame.html',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    url = f'https://wechat.njupt.edu.cn/mini_program/v4/venue/user/time/display/1?date={date}'
    r = requests.get(url, headers=header,verify=False)
    res=r.json()
    return res

def booking(_token, _id):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    body = f'date={date}'
    header = {
        'Host': 'wechat.njupt.edu.cn',
        'xweb_xhr': '1',
        'content-length': '15',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c0f)XWEB/11275',
        'token': _token,
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://servicewechat.com/wx3bb0b520a9e56a99/301/page-frame.html',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    url = f'https://wechat.njupt.edu.cn/mini_program/v4/venue/user/booking/pomelo/{_id}'
    r = requests.post(url, headers=header, data=body,verify=False)
    return r.json()

def consume(_token, _orderId):
    body = f'orderId={_orderId}'
    header = {
        'Host': 'wechat.njupt.edu.cn',
        'xweb_xhr': '1',
        'content-length': str(len(body)),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c0f)XWEB/11275',
        'token': _token,
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://servicewechat.com/wx3bb0b520a9e56a99/301/page-frame.html',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    url = 'https://wechat.njupt.edu.cn/mini_program/v4/e-card/pay/consume'
    r = requests.post(url, headers=header, data=body,verify=False)
    print(r.json())
    return r.json()


if __name__ == '__main__':
    token = ''
    if token == '':
        token = input('[+]input your token: ')
    res = get_stadiums_info(token)
    if not res['success']:
        print(res['errMsg'])
        input("Press any key to exit...")
        exit()
    stadiums = res['data'][0]['timeFields']
    print("Select stadium:")
    while True:
        for i in range(len(stadiums)):
            print(f"{i+1}:", stadiums[i]['startTime'], stadiums[i]['endTime'])
        choice = int(input('[+]: '))
        stadiumInfos = stadiums[choice-1]['stadiumInfos']
        for i in range(len(stadiumInfos)):
            print(f"{i+1}:", stadiumInfos[i]['name'])
        print('0:', 'back')
        choice = int(input('[+]: '))
        if choice != 0:
            break
    print(stadiumInfos[choice-1]['id'])
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == '12:00:00':
            break
    time.sleep(0.1) # 到点直接执行会报错未到预订时间
    res = booking(token, stadiumInfos[choice-1]['id'])
    time.sleep(0.05)  # 到点直接执行会报错未到预订时间
    res = booking(token, stadiumInfos[choice - 1]['id'])
    time.sleep(0.05)  # 到点直接执行会报错未到预订时间
    res = booking(token, stadiumInfos[choice - 1]['id'])
    time.sleep(0.05)  # 到点直接执行会报错未到预订时间
    res = booking(token, stadiumInfos[choice - 1]['id'])
    time.sleep(0.05)  # 到点直接执行会报错未到预订时间
    res = booking(token, stadiumInfos[choice - 1]['id'])
    time.sleep(0.05)  # 到点直接执行会报错未到预订时间
    res = booking(token, stadiumInfos[choice - 1]['id'])
    if not res['success']:
        print(res['errMsg'])
        input("Press any key to exit...")
    print(res)
    orderId = res['data']['orderId']
    res = consume(token, orderId)
    if not res['success']:
        print(res['errMsg'])
        input("Press any key to exit...")
    print(res)
    input("Press any key to exit...")
    if res["success"]:
        print("success")
        exit(0)