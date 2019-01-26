import main
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_subint(self):
        rv =  self.app.get('/sub?A=2&B=5')
        self.assertEqual(b'-3 \n', rv.data)
        self.assertNotEqual(b'6.000 \n',rv.data)
    def test_subfloat(self):
        rv =  self.app.get('/sub?A=2.3&B=3.3')
        self.assertEqual(b'-1 \n', rv.data)
    def test_subfrac(self):
        rv =  self.app.get('/sub?A=2/3&B=3/3')
        self.assertEqual(b'-0.3333333333333333 \n', rv.data)
    def test_subneg(self):
        rv =  self.app.get('/sub?A=2.3&B=-3.3')
        self.assertEqual(b'5.6 \n', rv.data)

if __name__ == '__main__':
    unittest.main()
