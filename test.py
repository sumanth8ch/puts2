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
