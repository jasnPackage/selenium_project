import unittest
from common.logger import Log

@unittest.skip(u"无条件跳过此用例")
class Test_home(unittest.TestCase):
    log = Log()
    def test_home(self):
        self.log.info("开始执行用例test_home")
        print(u"来打印啊test_home")
        self.log.info("用例test_home执行结束")


if __name__ == "__main__":
    unittest.main()




