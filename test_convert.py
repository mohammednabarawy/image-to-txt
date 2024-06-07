import unittest
import os
from img2otxt import convert_image_to_text


class TestImageToText(unittest.TestCase):
    def test_convert(self):
        image_path = 'New.png'
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        convert_image_to_text(image_path, output_dir)
        # Check if output.txt is created
        self.assertTrue(os.path.exists(os.path.join(output_dir, 'output.txt')))


if __name__ == '__main__':
    unittest.main()
