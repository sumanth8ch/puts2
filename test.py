import main
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_addint(self):
        rv =  self.app.get('/add?A=2&B=5')
        self.assertEqual(b'7 \n', rv.data)
        self.assertNotEqual(b'6.000 \n',rv.data)
    def test_addfloat(self):
        rv =  self.app.get('/add?A=2.3&B=3.3')
        self.assertEqual(b'5.6 \n', rv.data)
    def test_addfrac(self):
        rv =  self.app.get('/add?A=2/3&B=3/3')
        self.assertEqual(b'1.6666666666666667 \n', rv.data)
    def test_addneg(self):
        rv =  self.app.get('/add?A=2.3&B=-3.3')
        self.assertEqual(b'-1 \n', rv.data)
if __name__ == '__main__':
    unittest.main()
