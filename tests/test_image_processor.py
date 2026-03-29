'''
https://docs.python.org/3/library/unittest.html

class ...(unittest.TestCase): 
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_something(self):
        self.assertEqual(True, False)
'''

import unittest
import os
import sys
from PIL import Image

sys.path.append('./src')

from src.image_processor import precess_file, add_text_elements

class TestImageProcessor(unittest.TestCase):
    
    def setUp(self):
        self.test_img = Image.new('RGB', (100, 100), color='red')
        self.test_img_path = './tests/test_image.jpg'
        self.test_img.save(self.test_img_path)
    

    def tearDown(self):

        if os.path.exists(self.test_img_path):
            os.remove(self.test_img_path)

        # ./polaroid_test_image.jpg after tests
        for file in os.listdir('./'):
            if file.startswith('test_') and file.endswith('_polaroid.jpg'):
                os.remove(f'./{file}')


    def test___process_file(self):

        result_path = precess_file(self.test_img_path)
        
        self.assertTrue(os.path.exists(result_path))

    
    def test___add_text_elements(self):

        canvas = Image.new('RGB', (400, 500), 'white')
        add_text_elements(canvas, geo="Paris, France", hashtags="vacation,travel", caption="Amazing trip!")
        
        self.assertIsNotNone(canvas)


if __name__ == '__main__':
    unittest.main()