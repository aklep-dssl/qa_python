import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    @pytest.mark.parametrize(
        'book_name', [
            '',
            'Заветы предательства. (сборник рассказов)'
        ],
        ids=['len < 1', 'len > 40']
    )
    def test_add_new_book_incorrect_length_not_added(self,book_name, collector):
        collector.add_new_book(book_name)

        assert not collector.get_books_genre()

    @pytest.mark.parametrize(
        'book_name',
        [
            '1',
            '1234567890123456789012345678901234567890'
        ],
        ids=['length = 1','length = 40']
    )
    def test_add_new_book_correct_length_added(self, book_name, collector):
        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()


    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Возвышение Хоруса')
        collector.add_new_book('Возвышение Хоруса')

        assert len(collector.get_books_genre()) == 1


    @pytest.mark.parametrize(
        'book_name,book_genre',
        [('Лживые Боги', 'Комедии'), ('Полёт Эйзенштейна', 'Мультфильмы')],
        ids=['False Gods + Comedy','The Flight of the Eisenstein + Animation']
    )
    def test_set_book_genre_set_existing_genre(self, book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre


    def test_set_book_genre_set_non_existing_genre_fail(self, collector):
        collector.add_new_book('Лживые Боги')
        collector.set_book_genre('Лживые Боги', 'Сборник рецептов')

        assert collector.get_book_genre('Лживые Боги') == ''


    @pytest.mark.parametrize(
        'book_name,book_genre',
        [('Лживые Боги', 'Комедии'), ('Полёт Эйзенштейна', 'Мультфильмы')],
        ids=['False Gods + Comedy','The Flight of the Eisenstein + Animation']
    )
    def test_get_book_genre_returns_genre(self,book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        returned_genre = collector.get_book_genre(book_name)

        assert returned_genre == book_genre


    @pytest.mark.parametrize(
        'book_name,book_genre',
        [('Лживые Боги', 'Комедии'), ('Полёт Эйзенштейна', 'Мультфильмы')],
        ids=['False Gods + Comedy','The Flight of the Eisenstein + Animation']
    )
    def test_get_books_with_specific_genre_existing_book_returns_book(
            self, book_name, book_genre, collector
    ):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        books_by_genre = collector.get_books_with_specific_genre(book_genre)

        assert books_by_genre == [book_name]


    @pytest.mark.parametrize(
        'book_name, book_genre',
        [('Лживые Боги', 'Гримдарк'), ('Полёт Эйзенштейна', 'Эпос')],
        ids=['False Gods + Grimdark','The Flight of the Eisenstein + Epic Poetry']
    )
    def test_get_books_with_specific_genre_incorrect_genre_returns_empty_list(self, book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        books_by_genre = collector.get_books_with_specific_genre(book_genre)

        assert books_by_genre == []


    @pytest.mark.parametrize(
        'bookngenre',
        [
            (
                    {'Лживые Боги': 'Комедии',
                     'Полёт Эйзенштейна': 'Мультфильмы'}
            )
        ]
    )
    def test_get_books_genre_add_2_books_return_2_books(self, bookngenre, collector):
        for k, v in bookngenre.items():
            collector.add_new_book(k)
            collector.set_book_genre(k, v)
        books_by_genre = collector.get_books_genre()

        assert books_by_genre == bookngenre


    def test_get_books_genre_no_books_return_empty_dict(self, collector):
        books_by_genre = collector.get_books_genre()

        assert books_by_genre == {}


    @pytest.mark.parametrize(
        'book_name,book_genre',
        [('Лживые Боги', 'Комедии'), ('Полёт Эйзенштейна', 'Мультфильмы')],
        ids=['Comedy','Animation']
    )
    def test_get_books_for_children_add_children_books_return_children_books(self, book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        children_books = collector.get_books_for_children()

        assert children_books == [book_name]


    @pytest.mark.parametrize(
        'book_name,book_genre',
        [('Где Уолли?', 'Детективы'), ('Дом на Пуховой опушке', 'Ужасы')],
        ids=['Detective', 'Horror']
    )
    def test_get_books_for_children_add_non_children_books_return_empty_list(self, book_name, book_genre, collector):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        children_books = collector.get_books_for_children()

        assert children_books == []


    def test_add_book_in_favorites_add_1_fav_book_return_1_fav_book(self, collector):
        book_name = 'Сожжение Просперо'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert collector.favorites == [book_name]


    def test_delete_book_from_favorites_add_1_delete_1_return_empty_favlist(self, collector):
        book_name = 'Сожжение Просперо'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert collector.favorites == []


    def test_get_list_of_favorites_books_added_2_fav_return_2_fav(self, collector):
        book1_name = 'Сожжение Просперо'
        book2_name = 'Фулгрим'
        collector.add_new_book(book1_name)
        collector.add_book_in_favorites(book1_name)
        collector.add_new_book(book2_name)
        collector.add_book_in_favorites(book2_name)

        assert collector.get_list_of_favorites_books() == [book1_name, book2_name]