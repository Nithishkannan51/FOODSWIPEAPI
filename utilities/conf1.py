from pathlib import Path


class Conf1:
    LOG_PATH = "/logs/" + 'logfile.log'
    ROOT_PATH = str(Path(__file__).parent.parent)
    BASE_URL="https://may-hasherfoodswipe-backend-api-urtjok3rza-wl.a.run.app"
    Login= "https://may-hasherfoodswipe-backend-user-urtjok3rza-wl.a.run.app/v1/public/user/login-user"
    Additem="/inventory-management-service/v1/auth/inventory/createMenu"
    Availabilityitem="/inventory-management-service/v1/auth/inventory/updateMenu/1"

    fetchorderhistory="/checkout-service/v1/auth/orders/order-history/nelangovan@deloitte.com"
    fetchoneorder="/checkout-service/v1/auth/orders/order-history/nelangovan@deloitte.com/106"
    fetchallorder="/checkout-service/v1/auth/orders/all-order-history"
    updatemenu="/checkout-service/v1/auth/orders/update-order/nelangovan@deloitte.com/145"
    cancelorder="/checkout-service/v1/auth/orders/cancel-order/nelangovan@deloitte.com/107"
    createnewuser="/checkout-service/v1/auth/orders/create-order"

    status_200=200
    status_201=201
    status_400=400

    status_true=bool(True)
    status_false = bool(False)

    #Assertion inventoryservice
    menuname="Rice2"
    updatemenuname="Rice45"
