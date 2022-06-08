import pytest
import requests

#from pageObjects.task import task
#from pageObjects.user import user
from pageObjects.inventoryservicepage import inventoryservice
from pageObjects.checkoutservicepage import checkoutservice
from utilities.Base import Base
from utilities.Data import Data
from utilities.conf1 import Conf1


class Test_checkoutservice(Base):

    def test_loginuser(self):
        log = self.getLogger()
        log.info("Login user API response received")
        req = requests.post(Conf1.Login, json=checkoutservice.get_userlogin())

        # log.info(req.json())

        log.info("Login admin API response received ")

        assert req.status_code == Conf1.status_200

    def test_orderhistory(self):
        log = self.getLogger()
        log.info("Fetch order history by user id testing")
        headers_dict = {"Authorization": "Bearer " + checkoutservice.user_token}
        req = requests.get(Conf1.BASE_URL + Conf1.fetchorderhistory,headers=headers_dict)

        # log.info(req.json())

        log.info("Fetch order history API response received ")

        assert req.status_code == Conf1.status_200

    def test_fetchoneorder(self):
        log = self.getLogger()
        log.info("Fetch one order by order id testing")
        headers_dict = {"Authorization": "Bearer " + checkoutservice.user_token}
        req = requests.get(Conf1.BASE_URL + Conf1.fetchoneorder,headers=headers_dict)

        response_json=req.json()

        log.info("Fetch one order API response received ")

        assert req.status_code == Conf1.status_200
        assert response_json["orderId"]==106
        assert response_json["userId"]=="nelangovan@deloitte.com"

    def test_fetchallorder(self):
        log = self.getLogger()
        log.info("Fetch all order for all users testing")
        headers_dict = {"Authorization": "Bearer " + checkoutservice.user_token}
        req = requests.get(Conf1.BASE_URL + Conf1.fetchallorder,headers=headers_dict)

        response_json=req.json()

        log.info("Fetch all order for all users API response received ")

        assert req.status_code == Conf1.status_200

    def test_updatemenu(self):
        log = self.getLogger()
        log.info("update menu testing")
        headers_dict = {"Authorization": "Bearer " + checkoutservice.user_token}
        req = requests.put(Conf1.BASE_URL + Conf1.updatemenu,json=checkoutservice.get_updatemenu(),headers=headers_dict)

        response_json=req.json()
        log.info(response_json)
        log.info("updatemenu API response received ")

        assert req.status_code == Conf1.status_200
        assert response_json==True

    def test_cancelorder(self):
        log = self.getLogger()
        log.info("cancelorder testing")
        headers_dict = {"Authorization": "Bearer " + checkoutservice.user_token}
        req = requests.put(Conf1.BASE_URL + Conf1.cancelorder,headers=headers_dict)

        response_json=req.json()
        log.info("cancelorder API response received ")

        assert req.status_code == Conf1.status_200
        assert response_json==True

    def test_createneworder(self):
        log = self.getLogger()
        log.info("create new order testing")
        headers_dict = {"Authorization": "Bearer " + checkoutservice.user_token}
        req = requests.post(Conf1.BASE_URL + Conf1.createnewuser,json=checkoutservice.get_createneworder(),headers=headers_dict)

        #response_json=req.json()
        log.info("create new order API response received ")

        assert req.status_code == Conf1.status_200






