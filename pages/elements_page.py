from locators.elements_page_locators import TextBoxPageLocators

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("PSINA")
        self.element_is_visible(self.locators.EMAIL).send_keys("Typaya@AYE.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("PADLAGRAD")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('RUSSIA')
        self.element_is_visible(self.locators.SUBMIT).click()
