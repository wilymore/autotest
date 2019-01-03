import requests
import unittest


class Test(unittest.TestCase):
    '''AppCenter升级接口测试'''
    def test07(self):
        '''最新版本'''
        url = 'http://appcenter-50.tclclouds.com/appcenter-api-server/api/apkupgradeservice/findNewestApk'
        data = {"$ARGS": ["com.tcl.live"],
                "$BASE_PARAM": {"birthDay": "", "channelName": "AOTA", "countryId": -1, "countryMCC": "460",
                                "deviceId": -1, "deviceType": "mobile", "distributorId": -1,
                                "fingerPrint": "HUAWEI/EVA-AL10/HWEVA:8.0.0/HUAWEIEVA-AL10/535(C00):user/release-keys",
                                "imei": "869154026008834#c4:f0:81:10:ab:86#3c8de96354fa11b2", "imsi": "460009521890181",
                                "language": "zh_CN_#Hans", "mNC": {"mnc2": "00", "mnc3": "009"}, "mNC2": "00",
                                "mNC3": "009", "model": "EVA-AL10", "network": "wifi", "openId": "",
                                "osVersionCode": 26, "osVersionName": "8.0.0", "region": "US", "regionId": -1,
                                "screenDensity": 360, "screenResolution": "1792#1080", "supportThirdDownloadUrl": True,
                                "token": "", "versionCode": 575051, "versionName": "5.7.5.051"}}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r = requests.post(url=url, json=data, headers=headers)
        print(r.text)
        self.assertEqual(r.text, 'null', u'分类接口返回错误')

    def test08(self):
        '''可升级版本'''
        url = 'http://appcenter-50.tclclouds.com/appcenter-api-server/api/apkupgradeservice/findNewestApk'
        data2 = {"$ARGS": ["com.tcl.live"],
                "$BASE_PARAM": {"birthDay": "", "channelName": "AOTA", "countryId": -1, "countryMCC": "460",
                                "deviceId": -1, "deviceType": "mobile", "distributorId": -1,
                                "fingerPrint": "HUAWEI/EVA-AL10/HWEVA:8.0.0/HUAWEIEVA-AL10/535(C00):user/release-keys",
                                "imei": "869154026008834#c4:f0:81:10:ab:86#3c8de96354fa11b2", "imsi": "460009521890181",
                                "language": "zh_CN_#Hans", "mNC": {"mnc2": "00", "mnc3": "009"}, "mNC2": "00",
                                "mNC3": "009", "model": "EVA-AL10", "network": "wifi", "openId": "",
                                "osVersionCode": 26, "osVersionName": "8.0.0", "region": "US", "regionId": -1,
                                "screenDensity": 360, "screenResolution": "1792#1080", "supportThirdDownloadUrl": True,
                                "token": "", "versionCode": 575046, "versionName": "5.7.5.046"}}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        r2 = requests.post(url=url, json=data2, headers=headers)
        print(r2.text)
        # self.assertEqual(sec, 'com.fortafygames.colorswitch', u'分类接口返回错误')


if __name__ == '__main__':
    unittest.main()
