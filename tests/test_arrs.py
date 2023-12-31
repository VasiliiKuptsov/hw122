from unittest import TestCase
from utils import arrs

#def test_get():
 #   assert arrs.get([1, 2, 3], 1, "test") == 2
  #  assert arrs.get([], -11, "test") == "test"


#def test_slice():
 #   assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
  #  assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
   # assert arrs.my_slice([], 1) == []
    #assert arrs.my_slice([1, 2, 3],-5, 3) == [1, 2, 3]
    #assert arrs.my_slice([1, 2, 3],-2, 3) == [2, 3]

class ArtTestCase(TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test") , 2)
        self.assertEqual(arrs.get([], -11, "test"), "test")


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3),[2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5, 3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2, 3), [2, 3])