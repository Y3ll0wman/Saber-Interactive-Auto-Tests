from qa_guru_python_8_15.web import main_page, news_page, careers_page


def test_go_to_the_news_is_possible():
    # GIVEN
    main_page.open()

    # WHEN
    main_page.go_to_careers()

    # THEN
    careers_page.go_to_the_careers_is_possible()
