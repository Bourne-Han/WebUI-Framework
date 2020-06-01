import unittest
from WebUI.useUnittest.unittest_using import Run
import HTMLTestRunner
import os

# 创建测试套件
suite = unittest.TestSuite()
# 添加指定用例
# 一.suite.addTest(Run('test_case1'))
# suite.addTest(Run('test_case2'))
# 二.添加多条用例
# cases=[Run('test_case1'),Run('test_case2')]
# suite.addTests(cases)
# 三.设置指运行条件，所有符合条件的py文件都会被执行，文件中的测试用例会按原本的顺序执行
# dir=r'./'
# discover=unittest.defaultTestLoader.discover(start_dir=dir,pattern='uni*.py')
# 四.运行指定类对象中的测试用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Run))
# 五.运行指定名称的类对象中的测试用例
# suite.addTests(unittest.TestLoader().loadTestsFromName('unittest_using.Run'))
# 创建运行器，执行测试用例
# run = unittest.TextTestRunner()
# run.run(suite)

# 创建测试报告运行器
report_name = '商城登录添加购物车流程报告'
report_title = '测试报告'
report_desc = '商品添加购物车'
report_dir = './report/'
report_file = report_dir+'ShopReport.html'
# 判断是路径否存在，不存在则创建
if not os.path.exists(report_dir):
    os.mkdir(report_dir)
else:
    pass
# 生成测试报告
with open(report_file, 'wb') as report:
    suite.addTest(Run('test_case1'))
    suite.addTest(Run('test_case2'))
    htmlrun = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, description=report_desc)
    htmlrun.run(suite)
