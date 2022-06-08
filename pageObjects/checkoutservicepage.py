from utilities.conf1 import Conf1


class checkoutservice:
    userid = ""
    user_token = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJGb29kU3dpcGUiLCJzdWIiOiJKV1QiLCJ1c2VyaWQiOiJuZWxhbmdvdmFuQGRlbG9pdHRlLmNvbSIsImF1dGhvcml0aWVzIjoiQ3VzdG9tZXIiLCJpYXQiOjE2NTQ3MDc2MTksImV4cCI6MTY1NTAwNzYxOX0.09IeAgMT0Onz5hQzF13NDyXq9_-8ySw_01AxTr0CP94"

    @staticmethod
    def get_userlogin():
        payload = {
            "emailId":"nelangovan@deloitte.com",
            "password":"Nithish12@"

        }
        return payload

    @staticmethod
    def get_updatemenu():
        payload = {
            "menuId": 145,
            "quantity": 40,
            "amount": 75.0,
            "menuStatus": "In Progress"
        }
        return payload

    @staticmethod
    def get_createneworder():
        payload = {
            "userId": "nelangovan@deloitte.com",
            "finalAmount": 35,
            "orderItems": [
            {
                "menuId": 35,
                "amount": 35,
                "quantity": 1,
                "menuStatus": ""
            }
            ],
            "paymentDetails": {
                "cardNumber": "1111222233334444",
                "nameOnCard": "Bayvao Verma",
                "expMonth": "SEP",
                "expYear": "2025",
                "cvv": "115",
                "totalAmount": 35
            }
        }

        return payload