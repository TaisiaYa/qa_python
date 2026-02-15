class TestBooksCollector:

    def test_add_new_book_add_two_books(self, books_collector):
        books_collector.add_new_book('Гордость и предубеждение и зомби')
        books_collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_genre()) == 2

    # Тест метода set_book_genre
    def test_set_book_genre(self, books_collector):
        books_collector.add_new_book('Книга1')
        books_collector.set_book_genre('Книга1', 'Фантастика')
        assert books_collector.get_book_genre('Книга1') == 'Фантастика'

    # Тест метода get_book_genre
    def test_get_book_genre_no_genre(self, books_collector):
        books_collector.add_new_book('Вишневый сад')
        result = books_collector.get_book_genre('Вишневый сад')
        assert result is None or result == ''

    # Тест метода get_books_with_specific_genre
    def test_get_books_with_specific_genre(self, books_collector):
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        books_collector.add_new_book('Марсианин')
        books_collector.set_book_genre('Марсианин', 'Фантастика')
        books_collector.add_new_book('Пикник на обочине')
        books_collector.set_book_genre('Пикник на обочине', 'Фантастика')
        result = books_collector.get_books_with_specific_genre("Фантастика")
        assert result == ['Марсианин', 'Пикник на обочине']

    # Тест метода get_books_for_children
    def test_get_books_for_children_exclude_adult_books(self, books_collector):
        books_collector.add_new_book('Психо')
        books_collector.set_book_genre('Психо', 'Ужасы')
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        books_collector.add_new_book('Ну, погоди!')
        books_collector.set_book_genre('Ну, погоди!', 'Мультфильмы')
        result = books_collector.get_books_for_children()
        assert 'Ну, погоди!' in result
        assert 'Психо' not in result
        assert 'Оно' not in result

    # Тест метода add_book_in_favorites
    def test_add_book_in_favorites_success(self, books_collector):
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        books_collector.add_book_in_favorites('Оно')
        assert 'Оно' in books_collector.get_list_of_favorites_books()

    # Тест метода delete_book_from_favorites
    def test_delete_book_from_favorites_success(self, books_collector):
        books_collector.add_new_book('Оно')
        books_collector.set_book_genre('Оно', 'Ужасы')
        books_collector.add_book_in_favorites('Оно')
        books_collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in books_collector.get_list_of_favorites_books()

    # Тест метода get_list_of_favorites_books
    def test_get_list_of_favorites_empty(self, books_collector):
        result = books_collector.get_list_of_favorites_books()
        assert result == []

    # Тест метода get_books_genre
    def test_get_books_genre_empty(self, books_collector):
        result = books_collector.get_books_genre()
        assert result == {}