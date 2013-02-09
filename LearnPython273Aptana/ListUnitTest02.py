import unittest

class ListUnitTest02(unittest.TestCase):
	
	def setUp(self):
		self.list_unit_test_01 = ["A", "B" , "C", "D"]

	def test_print(self):
		print self.list_unit_test_01
	
	def test_list_assert(self):
		self.assertEqual(self.list_unit_test_01, ["A","B","C","D"])
		self.assertNotEqual(self.list_unit_test_01, ["A","B","C","C"])

if __name__ == "__main__":
	unittest.main()