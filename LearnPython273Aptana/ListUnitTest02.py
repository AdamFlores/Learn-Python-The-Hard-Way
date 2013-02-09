import unittest

class ListUnitTest02(unittest.TestCase):
	
	def setUp(self):
		self.list_unit_test_01 = ["A", "B" , "C", "D"]

	def test_print(self):
		print self.list_unit_test_01
		
	def test_list_for(self):
		for letter in self.list_unit_test_01:
			print letter
			
	def test_list_if(self):
		if "A" in self.list_unit_test_01:
			print "A is in List"
			
	def test_list_slice(self):
		begin = int(2)
		end = int(3)
		print "Slice:"
		print self.list_unit_test_01[begin:end]
		
	
	def test_list_assert(self):
		self.assertEqual(self.list_unit_test_01, ["A","B","C","D"])
		self.assertNotEqual(self.list_unit_test_01, ["A","B","C","C"])

if __name__ == "__main__":
	unittest.main()