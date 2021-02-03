# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
#------------Postfix evaluation tests------------ 
    # Test input with invalid tokens
    def test_postfix_eval_1(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    # Test inputs with too few operands
    def test_postfix_eval_2(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_3(self):
        try:
            postfix_eval("5 1 2 + / 4 ** + 3 -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")
    
    # Test inputs with too many operands
    def test_postfix_eval_4(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_postfix_eval_5(self):
        try:
            postfix_eval("5 1 2 + 4 ** 5 3 + 3 -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    # Tests that dividing by zero raises a ValueError
    def test_postfix_eval_6(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 2 0 / - 4 5 / 6 - *")
    
    # Tests the general operation of the postfix evaluation
    def test_postfix_eval_7(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
    
    def test_postfix_eval_8(self):
        self.assertAlmostEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        
    def test_postfix_eval_9(self):
        self.assertAlmostEqual(postfix_eval("3 2 1 / - 4 5 / 6 - *"), -5.2)

#------------ Prefix to postfix tests------------        
    # Tests general operation of conversion
    def test_prefix_to_postfix_1(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        
    def test_prefix_to_postfix_2(self):
        self.assertEqual(prefix_to_postfix("- + 7 ** 4 5 + 2 0"), "7 4 5 ** + 2 0 + -")
            
            
if __name__ == "__main__":
    unittest.main()
