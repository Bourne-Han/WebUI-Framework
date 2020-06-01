import unittest
from WebUI.useUnittest.unittest_using import Run

# 创建测试套件
suite = unittest.TestSuite()
# 添加指定用例
# suite.addTest(Run('test_case1'))
# suite.addTest(Run('test_case2'))
#添加多条用例
# cases=[Run('test_case1'),Run('test_case2')]
# suite.addTests(cases)
#设置指运行条件，所有符合条件的py文件都会被执行，文件中的测试用例会按原本的顺序执行
# dir=r'./'
# discover=unittest.defaultTestLoader.discover(start_dir=dir,pattern='uni*.py')
#运行指定类对象中的测试用例
# suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Run))
#运行指定名称的类对象中的测试用例
suite.addTests(unittest.TestLoader().loadTestsFromName('unittest.Run'))
# 创建运行器，执行测试用例
run = unittest.TextTestRunner()
run.run(suite)
