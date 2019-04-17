import requests
import random
from random import shuffle


class CircleApi:

    def test_offtime_api(self, days, start, end, name, id):
        self.days = days
        self.start = start
        self.end = end
        self.name = name
        self.id = id
        access_token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1NTY2NjMzOTUsInR5cGUiOiJhZG1pbiIsImNpcmNsZWlkIjoiMTEyY2I3YjAtODg1MS00OGU5LThmYTItNDJlNjY1ZDM1ODlhIiwiZGV2aWNlaWQiOiJhdXRoLXRlc3QtYWRtaW4iLCJsb2NhbC1zZWNyZXQiOiI3QkFDQ0VFODM0RjE5OUE4NDdBMUYzMTVCMURCQTIyNzk4QzNFNTUyQTkwNzU5MENGOTJDNzQzMUQxNzU2NzE4IiwiYWNjb3VudC1zdGF0dXMiOiJhY3RpdmUifQ.FSJi1l4w4klBGtOKsDZmmCdacZkA_IPRmJUkzLiwGu58nxKZrkAn7t2FCYepqTbsIy945MARDkxguBCjMioh-eDH52N3GIK-qcWGyB_FVen9a2ZskPsv-rc9xQkzDA8mzkFYDC6EJd6oRgWriD6XZHC3aJEXxDYabNLRGXXr4Xb3icudrjQfDgEvbm8BPdWnLRuIpR1XNYECGDEBbjPUb6iz7KfNjnXEweyllkQVdNYa1hDfHkhHxBl_TjoLuJ7W6eZPNawrJLipeLYmHhAGHrK2VIYXM1MANl-27KY6W_lyuh8rBWrqTNLfyisLIxH4JnFKNzbojMRQcWL2LBEC8w'
        header = {'Authorization': access_token}
        url = "https://vc02.product.demo.meetcircle-blue.co/api/ADD/users/user/flexOffTimes/offTime"
        querystring = {"clear": "true",
                       "user.pid": "0",
                       "days": self.days,
                       "start": self.start,
                       "end": self.end,
                       "name": self.name,
                       "type": 'offtime',
                       "id": self.id}
        response = requests.get(url, headers=header, params=querystring)
        return response

    @staticmethod
    def generate_random_days(ln):
        word = '1234560N'
        word = list(word)
        shuffle(word)
        days = ''.join(word)
        return days[:ln]

    @staticmethod
    def generate_random_time():
        start_time = f'{random.randint(0, 23):02}:{random.randint(0, 59):02}'
        end_time = f'{random.randint(0, 23):02}:{random.randint(0, 59):02}'
        print(start_time, end_time)
        return start_time, end_time

    @staticmethod
    def generate_random_name():
        f = open('src/words.txt', 'r')
        words = f.readlines()
        return words[random.randint(0, 25000)]

