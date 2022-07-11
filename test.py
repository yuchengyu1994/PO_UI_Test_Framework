import unittest

class testa(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('111')

    @classmethod    #针对整个测试类
    def tearDownClass(cls) -> None:
        print('222')

    def setUp(self) -> None:  #针对测试方法
        print('333')

    def tearDown(self) -> None:
        print('444')

    def test_01(self):
        print('test_01')
        self.assertTrue(True)

    def test_02(self):
        print('test_02')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()