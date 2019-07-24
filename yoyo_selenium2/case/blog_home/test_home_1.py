import unittest
from common.logger import Log


class Test_home_1(unittest.TestCase):
    log = Log()

    @unittest.skip(u"无条件跳过此用例")
    def test_home_1(self):
        self.log.debug("开始执行用例test_home_1")
        print("test_home_1")
        self.log.error("用例test_home_1执行时报错")

if __name__ == "__main__":
    unittest.main()


