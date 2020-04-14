import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TutorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000")

    def test_tutor_does_not_contain_completed_text(self):
        driver = self.driver
        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"")
    def test_tutor_has_cursor(self):
        driver = self.driver
        next_char=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(next_char.text,"h")

    def test_tutor_contains_uncompleted_text(self):
        driver = self.driver
        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"ello world YHNUJM QAZWSXEDCRFVTGB")

    def test_tutor_makes_text_completed_when_typing(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions.send_keys("hel")
        actions.perform()

        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"hel")

    def test_tutor_moves_cursor_when_typing(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions.send_keys("hel")
        actions.perform()

        cursor=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(cursor.text,"l")

    def test_tutor_removes_uncompleted_text_completed_when_typing(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions.send_keys("hel")
        actions.perform()

        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"o world YHNUJM QAZWSXEDCRFVTGB")

    def test_tutor_supports_spaces(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions.send_keys("hello" + Keys.SPACE)
        actions.perform()

        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"hello ")

        cursor=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(cursor.text,"w")

        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"orld YHNUJM QAZWSXEDCRFVTGB")

    def test_tutor_supports_backspaces(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions.send_keys("hel" + Keys.BACK_SPACE)
        actions.perform()

        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"he")

        cursor=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(cursor.text,"l")

        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"lo world YHNUJM QAZWSXEDCRFVTGB")
    def test_tutor_disallows_wrong_characters(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions.send_keys("heppo")
        actions.perform()

        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"he")

        cursor=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(cursor.text,"l")

        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"lo world YHNUJM QAZWSXEDCRFVTGB")

    def test_tutor_supports_uppercase_characters(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions\
            .send_keys("hello" + Keys.SPACE + "world" + Keys.SPACE)\
            .key_down(Keys.LEFT_SHIFT)\
            .send_keys("yhnujm")\
            .key_up(Keys.LEFT_SHIFT)
        actions.perform()

        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"hello world YHNUJM")

        cursor=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(cursor.text," ")

        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"QAZWSXEDCRFVTGB")

    def test_tutor_requires_correct_shift(self):
        driver = self.driver
        actions=ActionChains(driver)
        actions\
            .send_keys("hello" + Keys.SPACE + "world" + Keys.SPACE)\
            .key_down(Keys.LEFT_SHIFT)\
            .send_keys("yhnujm"+Keys.SPACE+"qazwsxedcrfvtgb")\
            .key_up(Keys.LEFT_SHIFT)
        actions.perform()

        completed=driver.find_element_by_id("tutor-completed")
        self.assertEqual(completed.text,"hello world YHNUJM ")

        cursor=driver.find_element_by_id("tutor-cursor")
        self.assertEqual(cursor.text,"Q")

        uncompleted=driver.find_element_by_id("tutor-uncompleted")
        self.assertEqual(uncompleted.text,"AZWSXEDCRFVTGB")


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
