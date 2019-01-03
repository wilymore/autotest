import requests
import unittest


class Test(unittest.TestCase):
    '''AppCenter清理白名单接口测试'''
    def test04(self):
        url = 'http://appcenter-50.tclclouds.com/appcenter-api-server/v2/whitelist/config.json'
        data = {'channelName': 'AOTA',
                'deviceType': 'mobile',
                'imei': '869154026008834#c4:f0:81:10:ab:86#3c8de96354fa11b2',
                'imsi': '460009521890181',
                'language': 'zh_CN_#Hans',
                'model': 'EVA-AL10',
                'osVersionCode': '26',
                'osVersionName': '8.0.0',
                'region': 'US',
                'screenResolution': '1792#1080',
                'type': 'clean',
                'versionCode': '575051',
                'versionName': '5.7.5.051'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post(url=url, params=data, headers=headers)
        print(type(r.text))
        dic = r.json()
        first = dic.get('data')
        sec = first.get('packageNames')
        # print(type(sec))
        print(sec[0])
        self.assertEqual(sec[0], 'com.tiny.flashlight', '白名单接口错误')


if __name__ == '__main__':
    unittest.main()
