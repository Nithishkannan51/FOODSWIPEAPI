from utilities.conf import Conf


class task:
    tasklist = []

    @staticmethod
    def get_add_task_payload(taskname):
        payload = {
            "description": taskname
        }
        return payload

    @staticmethod
    def get_task_by_pagination_endpoint(pagination_count, skip_count):
        return "/task?limit=" + str(pagination_count) + "&skip=" + str(skip_count)

    @staticmethod
    def get_limit_data_list():
        return [{"limit": Conf.limit_list[0]}, {"limit": Conf.limit_list[1]}, {"limit": Conf.limit_list[2]}]
