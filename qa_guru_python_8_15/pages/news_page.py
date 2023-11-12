import allure

from selene import browser, be, have


class NewsPage:
    teardown = browser.element('//a[@href="https://saber.games/teardowngameplayoverviewtrailer/"]')
    news_description = browser.element('[data-id="a609c9"]')

    def click_on_teardown(self):
        with allure.step('Нажать на блок "Teardown"'):
            self.teardown.should(be.clickable).click()

    def go_to_the_news_is_possible(self):
        with allure.step('Проверить, что текст "NEW TEARDOWN OVERVIEW VIDEO" - отображается'):
            self.news_description.should(have.text('NEW TEARDOWN OVERVIEW VIDEO'))
