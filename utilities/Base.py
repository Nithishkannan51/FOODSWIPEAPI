import inspect
import logging


from utilities.conf import Conf


class Base:
    baseurl=Conf.BASE_URL
    register_user_endpoint=Conf.REGISTER_USER
    login_user_endpoint=Conf.LOGIN_USER
    update_user_endpoint = Conf.UPDATE_USER
    add_task_endpoint=Conf.ADD_TASK
    get_all_task_endpoint=Conf.GET_ALL_TASK
    delete_user_endpoint=Conf.DELETE_USER

    status_code_200 = Conf.status_200
    status_code_201 = Conf.status_201
    status_code_400=Conf.status_400

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(Conf.ROOT_PATH + Conf.LOG_PATH)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
