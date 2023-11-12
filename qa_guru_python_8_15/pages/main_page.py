import allure

from selene import browser, be, have, by


class MainPage:
    main_menu_about = browser.element('//a[.="ABOUT"]')
    main_menu_games = browser.element('//a[.="GAMES"]')
    main_menu_studios = browser.element('//a[.="STUDIOS"]')
    main_menu_news = browser.element('//a[.="NEWS"]')
    about_section = browser.element('#about')
    game_project_space_marine_2 = browser.element('//a[@href="https://www.focus-entmt.com/en/games/warhammer-40000-space-marine-2"]')
    studio_3d_realms = browser.element('//a[@href="https://3drealms.com/"]')

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

    def go_to_games_section(self):
        with allure.step('Перейти в раздел "Games"'):
            self.main_menu_games.should(be.clickable).click()

    def click_on_game_project_space_marine_2(self):
        with allure.step('Нажать на "SPACE MARINE 2"'):
            self.game_project_space_marine_2.should(be.clickable).click()

    def go_to_the_game_project_is_possible(self):
        with allure.step('Проверить, что в title указано "Space Marine 2 - Focus Entertainment"'):
            browser.switch_to_tab(1)
            title = str(browser.driver.title)
            assert title == 'Space Marine 2 - Focus Entertainment', f'Заголовок страницы: {title}'
        with allure.step('Проверить, что URL страницы: '
                         'https://www.focus-entmt.com/en/games/warhammer-40000-space-marine-2'):
            current_url = browser.driver.current_url
            assert current_url == 'https://www.focus-entmt.com/en/games/warhammer-40000-space-marine-2', f"Текущий url страницы: {current_url}"

    def go_to_studios_section(self):
        with allure.step('Перейти в раздел "Studios"'):
            self.main_menu_studios.should(be.clickable).click()

    def click_on_studio_3d_realms(self):
        with allure.step('Нажать на "3D Realms"'):
            self.studio_3d_realms.should(be.clickable).click()

    def go_to_the_studio_is_possible(self):
        with allure.step('Проверить, что в title указано "Home - 3DRealms"'):
            browser.switch_to_tab(1)
            title = str(browser.driver.title)
            assert title == 'Home - 3DRealms', f'Заголовок страницы: {title}'
        with allure.step('Проверить, что URL страницы: '
                         'https://3drealms.com/'):
            current_url = browser.driver.current_url
            assert current_url == 'https://3drealms.com/', f"Текущий url страницы: {current_url}"

    def go_to_news_section(self):
        with allure.step('Нажать на "News"'):
            self.main_menu_news.should(be.clickable).click()
