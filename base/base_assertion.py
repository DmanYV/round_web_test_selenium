from base.base_page import BasePage


class Assertion(BasePage):

    def text_in_element(self, element_locator, expected_text):
        actual_text = self.find_element(element_locator).text
        assert expected_text == actual_text, f"Ожидался текст: '{expected_text}', отображается текс: '{actual_text}'"
