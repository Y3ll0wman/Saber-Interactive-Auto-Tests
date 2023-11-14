from qa_guru_python_8_15.web import main_page


def test_go_to_the_game_project_is_possible():
    # GIVEN
    main_page.open()

    # WHEN
    main_page.go_to_games_section()
    main_page.click_on_game_project_space_marine_2()

    # THEN
    main_page.go_to_the_game_project_is_possible()
