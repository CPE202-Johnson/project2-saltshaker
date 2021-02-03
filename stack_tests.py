import unittest
from stack_array import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
        
    # Tests that a new stack is empty
    def test_empty1(self):
        stack = Stack(9)
        self.assertTrue(stack.is_empty())
        
    # Test that a stack is empty after all values have been popped
    def test_empty2(self):
        stack = Stack(9)
        stack.push(5)
        stack.pop()
        self.assertTrue(stack.is_empty())
        
    def test_full(self):
        stack = Stack(1)
        stack.push(2)
        self.assertTrue(stack.is_full())
        
    # Tests that pushing to a full stack raises an error
    def test_errors1(self):
        stack = Stack(2)
        stack.push(1)
        stack.push(1)
        with self.assertRaises(IndexError):
            stack.push(1)
    
    # Tests that popping an empty list raises an error
    def test_errors2(self):
        stack = Stack(3)
        with self.assertRaises(IndexError):
            stack.pop()
          
    # Tests that peeking at an empty list raises an error
    def test_errors3(self):
        stack = Stack(2)
        with self.assertRaises(IndexError):
            stack.peek()
        
    # Tests basic operation of peek
    def test_peek1(self):
        stack = Stack(5)
        stack.push(4)
        stack.push(9)
        self.assertEqual(stack.peek(), 9)
    
    # Tests that peek doesn't change the stack size
    def test_peek2(self):
        stack = Stack(5)
        stack.push(4)
        stack.push(9)
        stack.peek()
        self.assertEqual(stack.size(), 2)
    
    # Tests basic operation of pop 
    def test_pop1(self):
        stack = Stack(4)
        stack.push(6)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        
    # Tests that pop reduces the size of the stack
    def test_pop2(self):
        stack = Stack(4)
        stack.push(6)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.size(), 1)

if __name__ == '__main__': 
    unittest.main()

