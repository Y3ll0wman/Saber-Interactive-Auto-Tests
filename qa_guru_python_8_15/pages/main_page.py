import allure

from selene import browser, be, have, by


class MainPage:
    main_menu_about = browser.element('//a[.="ABOUT"]')
    about_section = browser.element('#about')

    def open(self):
        with allure.step('Открыть https://saber.games/'):
            browser.open('/')

    def go_to_about_section(self):
        with allure.step('Перейти в раздел "About"'):
            self.main_menu_about.should(be.clickable).click()

    def about_section_should_be_displayed(self):
        with allure.step('Проверить, что заголовок "ABOUT" отображается'):
            self.about_section.should(have.text('ABOUT'))
        with allure.step('Проверить, что описание компании отображается'):
            self.about_section.should(have.text('Saber Interactive is a U.S.-based developer '
                                                'and publisher of video games'))
