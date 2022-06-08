import pytest
import requests

#from pageObjects.task import task
#from pageObjects.user import user
from pageObjects.inventoryservicepage import inventoryservice
from utilities.Base import Base
from utilities.Data import Data
from utilities.conf1 import Conf1


class Test_inventoryservice(Base):

    def test_admin_login(self):
        log = self.getLogger()
        log.info("Login admin API invoked")

        req = requests.post(Conf1.Login, json=inventoryservice.get_adminlogin())

        #log.info(req.json())

        log.info("Login admin API response received ")

        assert req.status_code == Conf1.status_200
        #log.info("Create user API assertion completed")

    def test_additem(self):
        log = self.getLogger()
        log.info("Add new item with item description")
        headers_dict = {"Authorization": "Bearer " + inventoryservice.user_token}
        req = requests.post(Conf1.BASE_URL + Conf1.Additem, json=inventoryservice.get_additem(),headers=headers_dict)
        response_json = req.json()
        log.info("Added new item with item description" + str(response_json))
        #assert Conf.duplicate_user_error in response_json
        assert req.status_code == Conf1.status_200
        assert response_json["menuName"]== Conf1.menuname
        assert response_json["quantity"]== 10
        assert response_json["price"] == 65.0
        log.info("Test Add item API Assertion completed")

    def test_updateitem(self):
        log = self.getLogger()
        log.info("update item with changes in item description")
        headers_dict = {"Authorization": "Bearer " + inventoryservice.user_token}
        req = requests.put(Conf1.BASE_URL + Conf1.Availabilityitem, json=inventoryservice.get_updateitem(),headers=headers_dict)
        response_json = req.json()
        log.info("updated item with changes in item description" + str(response_json))
        #assert Conf.duplicate_user_error in response_json
        assert req.status_code == Conf1.status_200
        assert response_json["menuId"] == 1
        assert response_json["menuName"]== Conf1.updatemenuname
        #assert response_json["quantity"]== 50
        assert response_json["price"] == 75.0
        log.info("Test update item API Assertion completed")

