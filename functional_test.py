import unittest
from selenium.webdriver.common import keys
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('./chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-to item'
        )
        input_box.send_keys('Buy something')
        input_box.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        row = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy something' for row in rows)
        )


if __name__ == '__main__':
    unittest.main()
