from pathlib import Path


class Conf:
    LOG_PATH = "/logs/" + 'logfile.log'
    ROOT_PATH = str(Path(__file__).parent.parent)
    BASE_URL="https://api-nodejs-todolist.herokuapp.com"
    REGISTER_USER="/user/register"
    LOGIN_USER="/user/login"
    UPDATE_USER="/user/me"
    ADD_TASK="/task"
    GET_ALL_TASK="/task"
    DELETE_USER="/user/me"
    status_200=200
    status_201=201
    status_400=400
    input_datafile_location="/resources/input_data.xlsx"
    backup_data_file_location="/resources/backup.xlsx"
    status_true=bool(True)
    status_false = bool(False)
    duplicate_user_error = "duplicate key"
    invalid_login_message="Unable to login"
    invalid_update_message="Please authenticate."
    user_name = "Kumar"
    user_email = "kumar@gmail.com"
    user_email_invalid = "kumar123@gmail.com"

    user_password = "12345678"
    user_age = 20
    user_updated_age=25
    task_pagination_count=10
    task_skip_count=0
    limit_list=[2,5,10]
