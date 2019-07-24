import unittest
from case.test_blog_login import Blog_login
from case.test_03 import Test03

if __name__ == "__main__":
    suite = unittest.TestSuite()
    # suite.addTest(Blog_login("test_blog_login_2"))
    suite.addTest(Test03("test03"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
