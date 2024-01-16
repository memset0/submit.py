from . import Adapter


class QojAdapter(Adapter):
    def login(self):
        username, password = self.fetch_user_data()
        login_page = session.get(f'{self.baseurl}/login')
        print(login_page)

    def __init__(self):
        self.module_name = 'qoj'
        self.baseurl = 'https://qoj.ac'
        self.languages = {
            'cpp': '',
            'py': '',
        }


if __name__ == '__main__':
    adapter = QojAdapter()
    adapter.login()
