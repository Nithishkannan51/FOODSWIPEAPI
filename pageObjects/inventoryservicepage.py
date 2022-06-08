from utilities.conf1 import Conf1


class inventoryservice:
    userid = ""
    user_token = "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJGb29kU3dpcGUiLCJzdWIiOiJKV1QiLCJ1c2VyaWQiOiJuaXNodUBkZWxvaXR0ZS5jb20iLCJhdXRob3JpdGllcyI6IkFkbWluIiwiaWF0IjoxNjU0NzAxMTg0LCJleHAiOjE2NTUwMDExODR9.fs-FX_YBryk7EaozU6QlU6BeZUqpgB4lbMjdWsXMwvg"

    @staticmethod
    def get_adminlogin():
        payload = {
            "emailId":"nishu@deloitte.com",
            "password":"Foodswipe@123"

        }
        return payload

    @staticmethod
    def get_additem():
        payload = {
            "menuId": 140,
            "menuCategory": "Lunch",
            "menuName": "Rice2",
            "menuDesc": "Authentic curd rice",
            "price": 65.0,
            "quantity": 10,
            "activeFlag": "true",
            "counterName": "HiD3"
        }
        return payload

    @staticmethod
    def get_updateitem():
        payload = {
            "menuId": 1,
            "menuCategory": "Lunch",
            "menuName": "Rice45",
            "menuDesc": "Authentic curd rice",
            "price": 75.0,
            "quantity": 40,
            "activeFlag": "true",
            "counterName": "HiD3"
}
        return payload