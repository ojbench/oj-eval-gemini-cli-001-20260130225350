import subprocess
import unittest

class TestAPlusB(unittest.TestCase):
    def test_sample(self):
        # The sample input from README
        input_str = "1 1\n"
        expected_output = "2\n"
        
        # Run the compiled executable
        process = subprocess.Popen(
            ['./code'], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_str)
        
        self.assertEqual(process.returncode, 0)
        self.assertEqual(stdout, expected_output)

if __name__ == '__main__':
    unittest.main()

