from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тест метода set_book_genre
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_book_genre('Книга1') == 'Фантастика'

    # Тест метода get_book_genre
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Вишневый сад')
        collector.set_book_genre('Вишневый сад', 'Комедия')
        result = collector.get_book_genre('Вишневый сад')
        assert result == 'Комедия'

    # Тест метода get_books_with_specific_genre
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        result = collector.get_books_with_specific_genre("Фантастика")
        assert result == ['Марсианин', 'Пикник на обочине']

    # Тест метода get_books_for_children
    def test_get_books_for_children_exclude_adult_books(self):
        collector = BooksCollector()
        collector.add_new_book('Психо')
        collector.set_book_genre('Психо', 'Ужасы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Ну, погоди!')
        collector.set_book_genre('Ну, погоди!', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Ну, погоди!' in result
        assert 'Психо' not in result
        assert 'Оно' not in result

    # Тест метода add_book_in_favorites
    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_book_in_favorites('Оно')
        assert 'Оно' in collector.get_list_of_favorites_books()

    #Тест метода delete_book_from_favorites
    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()

    #Тест метода get_list_of_favorites_books
    def test_get_list_of_favorites_empty(self):
        collector = BooksCollector()
        result = collector.get_list_of_favorites_books()
        assert result == []

    #Тест метода get_books_genre
    def test_get_books_genre_empty(self):
        collector = BooksCollector()
        result = collector.get_books_genre()
        assert result == {}
    