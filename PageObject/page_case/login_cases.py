import unittest
from WebUI.PageObject.page_object.login_page import LoginPage
from ddt import ddt, file_data


@ddt
class Cases(unittest.TestCase, LoginPage):

    def setUp(self) -> None:
        self.login = LoginPage()

    def tearDown(self) -> None:
        self.login.quit()

    # @data(('123456','54321'),('admin123','admin123'))
    # @unpack
    # def test_case(self,*args):
    #     self.login.login(*args)

    @file_data('../file/para.yaml')
    def test_case(self, **kwargs):
        self.login.login(kwargs.get('user'), kwargs.get('pwd'))


if __name__ == '__main__':
    unittest.main()
