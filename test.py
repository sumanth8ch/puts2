import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_addint(self):
            rv =  self.app.get('/add?A=2&B=5')
            self.assertEqual(b'7.0', rv.data)
            self.assertNotEqual(b'6.000',rv.data)
        def test_addfloat(self):
            rv =  self.app.get('/add?A=2.3&B=3.3')
            self.assertEqual(b'5.6', rv.data)
        def test_addfrac(self):
            rv =  self.app.get('/add?A=2/3&B=3/3')
            self.assertEqual(b'1.667', rv.data)
        def test_addneg(self):
            rv =  self.app.get('/add?A=2.3&B=-3.3')
            self.assertEqual(b'-1.0', rv.data)

        def test_subint(self):
            rv =  self.app.get('/sub?A=2&B=5')
            self.assertEqual(b'-3.0', rv.data)
            self.assertNotEqual(b'6.000',rv.data)
        def test_subfloat(self):
            rv =  self.app.get('/sub?A=2.3&B=3.3')
            self.assertEqual(b'-1.0', rv.data)
        def test_subfrac(self):
            rv =  self.app.get('/sub?A=2/3&B=3/3')
            self.assertEqual(b'-0.333', rv.data)
        def test_subneg(self):
            rv =  self.app.get('/sub?A=2.3&B=-3.3')
            self.assertEqual(b'5.6', rv.data)

        def test_mulint(self):
            rv =  self.app.get('/mul?A=2&B=5')
            self.assertEqual(b'10.0', rv.data)
            self.assertNotEqual(b'6.000',rv.data)
        def test_mulfloat(self):
            rv =  self.app.get('/mul?A=2.3&B=3.3')
            self.assertEqual(b'7.59', rv.data)
        def test_mulfrac(self):
            rv =  self.app.get('/mul?A=2/3&B=3/3')
            self.assertEqual(b'0.667', rv.data)
        def test_mulneg(self):
            rv =  self.app.get('/mul?A=2.3&B=-3.3')
            self.assertEqual(b'-7.59', rv.data)

        def test_divint(self):
            rv =  self.app.get('/div?A=2&B=5')
            self.assertEqual(b'0.4', rv.data)
            self.assertNotEqual(b'0.0256',rv.data)
        def test_divfloat(self):
            rv =  self.app.get('/div?A=2.3&B=3.3')
            self.assertEqual(b'0.697', rv.data)
        def test_divfrac(self):
            rv =  self.app.get('/div?A=2/3&B=3/3')
            self.assertEqual(b'0.667', rv.data)
        def test_divneg(self):
            rv =  self.app.get('/div?A=2.3&B=-3.3')
            self.assertEqual(b'-0.697', rv.data)
        def test_zerodiv(self):
            rv = self.app.get('/div?A=1/0&B=1')
            self.assertEqual(b'None',rv.data)

if __name__ == '__main__':
    unittest.main()
