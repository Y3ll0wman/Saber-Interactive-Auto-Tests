import allure

from selene import browser, be, have


class MainPage:
    main_menu_about = browser.element('//a[.="ABOUT"]')
    main_menu_games = browser.element('//a[.="GAMES"]')
    main_menu_studios = browser.element('//a[.="STUDIOS"]')
    main_menu_news = browser.element('//a[.="NEWS"]')
    main_menu_careers = browser.element('//a[.="CAREERS"]')
    main_menu_contact = browser.element('//a[.="CONTACT"]')
    about_section = browser.element('#about')
    game_project_space_marine_2 = browser.element('//a[@href="https://www.focus-entmt.com/en/games/warhammer-40000-space-marine-2"]')
    studio_3d_realms = browser.element('//a[@href="https://3drealms.com/"]')
    type_of_inquiry_dropdown = browser.element('#form-field-field_637c06a')
    type_of_inquiry_option = browser.element('//option[.="General"]')
    subject_input = browser.element('#form-field-field_be9cbc2')
    name_input = browser.element('#form-field-name')
    email_input = browser.element('#form-field-email')
    message_input = browser.element('#form-field-message')
    submit_button = browser.element('//button[@type="submit"]')
    success_message = browser.element('.elementor-message-success')

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
            browser.with_(timeout=3).switch_to_tab(1)
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
            browser.with_(timeout=3).switch_to_tab(1)
            title = str(browser.driver.title)
            assert title == 'Home - 3DRealms', f'Заголовок страницы: {title}'
        with allure.step('Проверить, что URL страницы: '
                         'https://3drealms.com/'):
            current_url = browser.driver.current_url
            assert current_url == 'https://3drealms.com/', f"Текущий url страницы: {current_url}"

    def go_to_news(self):
        with allure.step('Нажать на "News"'):
            self.main_menu_news.should(be.clickable).click()

    def go_to_careers(self):
        with allure.step('Перейти в раздел "Careers"'):
            self.main_menu_careers.should(be.clickable).click()

    def go_to_contacts_section(self):
        with allure.step('Перейти к форме "Contact us"'):
            self.main_menu_contact.should(be.clickable).click()

    def fill_contact_us_form(self):
        with allure.step('Указать тип обращения'):
            self.type_of_inquiry_dropdown.click()
            self.type_of_inquiry_option.click()

        with allure.step('Указать тему обращения'):
            self.subject_input.should(be.clickable).type('Test')
        with allure.step('Указать имя'):
            self.name_input.should(be.clickable).type('Tester')
        with allure.step('Указать email'):
            self.email_input.should(be.clickable).type('tester@example.com')
        with allure.step('Написать сообщение'):
            self.message_input.should(be.clickable).type('Test message')
        with allure.step('Нажать на кнопку "Send"'):
            self.submit_button.should(be.clickable).click()

    def to_send_contacts_is_possible(self):
        with allure.step('Проверить, что текст "Your submission was successful." - отображается'):
            pass
