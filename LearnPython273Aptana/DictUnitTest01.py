import unittest

class DictUnitTest01(unittest.TestCase):
    
    def setUp(self):
        self.dict_unit_test_01 = {"A":"Adam", "B":"Barry" , "C":"Cherry", "D":"Donkey"}
        self.dict_unit_test_02 = {"A":"Adam", "B":"Barry" , "C":"Cherry", "D":"Donkey"}
        
    def test_print(self):
        print self.dict_unit_test_01
        
   # def test_dict_for(self):
   #     for letter in self.dict_unit_test_01:
   #         print letter
            
   # def test_dict_if(self):
#        if "A" in self.dict_unit_test_01:
#            print "A is in List"
            
#    def test_dict_slice(self):
#        begin = int(2)
#        end = int(3)
#        print "Slice:"
  #      print self.dict_unit_test_01[begin:end]
        
    
    def test_dict_assert_equal(self):
        #print "This Test Should Pass:"
        self.assertEqual(self.dict_unit_test_01, self.dict_unit_test_02)
        #print "This Test Should Fail:"
        #self.assertNotEqual(self.dict_unit_test_01, {"A":"Adam", "B":"Barry" , "C":"Cherry", "D":"Donkey"})
    
    def test_dict_assert_not_equal(self):
        #print "This Test Should Fail:"
        self.assertNotEqual(self.dict_unit_test_01, self.dict_unit_test_02)
        
if __name__ == "__main__":
    unittest.main()