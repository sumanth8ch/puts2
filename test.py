import main
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

        def test_mulint(self):
            rv =  self.app.get('/mul?A=2&B=5')
            self.assertEqual(b'10 \n', rv.data)
            self.assertNotEqual(b'6.000 \n',rv.data)
        def test_mulfloat(self):
            rv =  self.app.get('/mul?A=2.3&B=3.3')
            self.assertEqual(b'7.59 \n', rv.data)
        def test_mulfrac(self):
            rv =  self.app.get('/mul?A=2/3&B=3/3')
            self.assertEqual(b'0.6666666666666666 \n', rv.data)
        def test_mulneg(self):
            rv =  self.app.get('/mul?A=2.3&B=-3.3')
            self.assertEqual(b'-7.59 \n', rv.data)

if __name__ == '__main__':
    unittest.main()
