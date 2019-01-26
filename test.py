import main
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

        def test_divint(self):
            rv =  self.app.get('/div?A=2&B=5')
            self.assertEqual(b'0.4 \n', rv.data)
            self.assertNotEqual(b'6.000 \n',rv.data)
        def test_divfloat(self):
            rv =  self.app.get('/div?A=2.3&B=3.3')
            self.assertEqual(b'0.696969696969697 \n', rv.data)
        def test_divfrac(self):
            rv =  self.app.get('/div?A=2/3&B=3/3')
            self.assertEqual(b'0.6666666666666666 \n', rv.data)
        def test_divneg(self):
            rv =  self.app.get('/div?A=2.3&B=-3.3')
            self.assertEqual(b'-0.696969696969697 \n', rv.data)

if __name__ == '__main__':
    unittest.main()
