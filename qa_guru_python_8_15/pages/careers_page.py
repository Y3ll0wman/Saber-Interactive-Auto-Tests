import allure

from selene import browser, have


class CareersPage:
    careers_section = browser.element('[data-id="1d714e4"]')
    def go_to_the_careers_is_possible(self):
        with allure.step('Проверить, что текст "ALL JOBS:" - отображается'):
            self.careers_section.should(have.text('ALL JOBS:'))
