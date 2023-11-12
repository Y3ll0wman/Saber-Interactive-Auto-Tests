import allure

from selene import browser, be, have, by


class MapPage:
    input_search = browser.element('[placeholder="Поиск в 2ГИС"]')

    def open(self):
        with allure.step('Открыть карту Санкт-Петербурга'):
            browser.open('/spb')

    def search(self, query):
        with allure.step(f'ввести в поиске {query} и нажать enter'):
            self.input_search.should(be.clickable).type(query).press_enter()

    def title_searched_object_should_be_displayed(self, text):
        with allure.step(f'Проверить, что текст {text} отображается в результатах поиска'):
            browser.element(by.text(text)).should(be.visible)
