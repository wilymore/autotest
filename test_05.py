import requests
import unittest


class Test(unittest.TestCase):
    '''获取城市ID'''
    def test05(self):
        url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=31117'
        res = requests.get(url=url)
        # f = open('result.txt', 'rb')
        # data = f.readlines()
        # f.close()
        # print(data)
        self.assertEqual(res.status_code, 200, 'Error')
        # print(res.text)
        # self.assertEqual(res.text, data, u'城市ID获取错误')


if __name__ == '__main__':
    unittest.main()
