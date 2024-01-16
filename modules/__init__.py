import requests
import requests.utils

headers = {
    'user-agent': f'mem-submit-client ({requests.utils.default_user_agent()})',
}


class Adapter:
    def fetch_user_data(self):
        username = os.getenv(f'{self.module_name}-username'.upper())
        if username is None:
            username = input(f'Please enter your {self.module_name} username: ')
        password = os.getenv(f'{self.module_name}-password'.upper())
        if password is None:
            password = input(f'Please enter your {self.module_name} password: ')
        return username, password

    def __init__(self):
        self.module_name = 'default'
        self.session = requests.Session()
        pass
