import unittest
from utils.text_utils import TextUtils
from config.config import Config

class TestTextUtils(unittest.TestCase):
    def setUp(self):
        self.text_utils = TextUtils()
        self.sample_text = "Hello, this is a test! Numbers 123 and special characters @#$%"
        self.valid_product = "Credit card"
        self.invalid_product = "Mortgage"

    def test_clean_text(self):
        cleaned = self.text_utils.clean_text(self.sample_text)
        self.assertEqual(cleaned, "hello this is a test numbers 123 and special characters")
        
    def test_format_source_document(self):
        doc = {
            'text': 'Sample complaint text',
            'metadata': {
                'product': 'Credit card',
                'complaint_id': '12345'
            }
        }
        formatted = self.text_utils.format_source_document(doc)
        self.assertIn('Product: Credit card', formatted)
        self.assertIn('Complaint ID: 12345', formatted)
        
    def test_format_error_message(self):
        error = Exception("Test error")
        formatted = self.text_utils.format_error_message(error)
        self.assertIn("Error: Test error", formatted)
        
    def test_validate_product(self):
        self.assertTrue(self.text_utils.validate_product(self.valid_product))
        self.assertFalse(self.text_utils.validate_product(self.invalid_product))
        
    def test_split_text(self):
        text = " " * (Config.CHUNK_SIZE * 2)  # Create a long text
        chunks = self.text_utils.split_text(text)
        self.assertGreater(len(chunks), 1)
        self.assertLess(len(chunks[0]), Config.CHUNK_SIZE + Config.CHUNK_OVERLAP)

if __name__ == '__main__':
    unittest.main()
