import requests



class CircleApiTestCase:
    def __init__(self, days, start, end, name, id):
        self.days = days
        self.start = start
        self.end = end
        self.name = name
        self.id = id

    def get_call(self):
        access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE1NTY2NjMzOTUsInR5cGUiOiJhZG1pbiIsImNpcmNsZWlkIjoiMTEyY2I3YjAtODg1MS00OGU5LThmYTItNDJlNjY1ZDM1ODlhIiwiZGV2aWNlaWQiOiJhdXRoLXRlc3QtYWRtaW4iLCJsb2NhbC1zZWNyZXQiOiI3QkFDQ0VFODM0RjE5OUE4NDdBMUYzMTVCMURCQTIyNzk4QzNFNTUyQTkwNzU5MENGOTJDNzQzMUQxNzU2NzE4IiwiYWNjb3VudC1zdGF0dXMiOiJhY3RpdmUifQ.FSJi1l4w4klBGtOKsDZmmCdacZkA_IPRmJUkzLiwGu58nxKZrkAn7t2FCYepqTbsIy945MARDkxguBCjMioh-eDH52N3GIK-qcWGyB_FVen9a2ZskPsv-rc9xQkzDA8mzkFYDC6EJd6oRgWriD6XZHC3aJEXxDYabNLRGXXr4Xb3icudrjQfDgEvbm8BPdWnLRuIpR1XNYECGDEBbjPUb6iz7KfNjnXEweyllkQVdNYa1hDfHkhHxBl_TjoLuJ7W6eZPNawrJLipeLYmHhAGHrK2VIYXM1MANl-27KY6W_lyuh8rBWrqTNLfyisLIxH4JnFKNzbojMRQcWL2LBEC8w'
        url = 'https://vc02.product.demo.meetcircle-blue.co/api/ADD/users/user/flexOffTimes/offTime'
        querystring = {"clear": "true",
                       "user.pid": "0",
                       "type": "offtime",
                       "days": self.days,
                       "start": self.start,
                       "end": self.end,
                       "name": self.name,
                       "id": self.id}
        header = {'Authorization': 'Bearer {}'.format(access_token)}
        response = requests.get(url, headers=header, params=querystring)
        response_json = response.json()
        return response_json

