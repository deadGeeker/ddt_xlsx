import ddt
import unittest
import baseinfo


@ddt.ddt()
class Demo(unittest.TestCase):

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    @ddt.data(*baseinfo.data)
    def test(self, testdata):
        print(testdata)


if __name__ == '__main__':
    unittest.main()
