from qa_guru_python_8_15.web import map_page


def test_find_an_object_by_search():
    # GIVEN
    map_page.open()

    # WHEN
    map_page.search(query='Газпром арена')

    # THEN
    map_page.title_searched_object_should_be_displayed(text='Газпром арена')

