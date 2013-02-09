import unittest

class DictUnitTest02(unittest.TestCase):
    
    def setUp(self):
        self.dict_unit_test_01 = ["A":"Adam", "B":"Barry" , "C":"Cherry", "D":"Donkey"]

    def test_print(self):
        print self.dict_unit_test_01
        
    def test_list_for(self):
        for letter in self.dict_unit_test_01:
            print letter
            
    def test_list_if(self):
        if "A" in self.dict_unit_test_01:
            print "A is in List"
            
    def test_list_slice(self):
        begin = int(2)
        end = int(3)
        print "Slice:"
        print self.dict_unit_test_01[begin:end]
        
    
    def test_list_assert(self):
        print "This Test Should Pass:"
        self.assertEqual(self.dict_unit_test_01, ["A":"Adam", "B":"Barry" , "C":"Cherry", "D":"Donkey"])
        print "This Test Should Fail:"
        self.assertNotEqual(self.dict_unit_test_01, ["A":"Adam", "B":"Barry" , "C":"Cherry", "D":"Donkey"])

if __name__ == "__main__":
    unittest.main()