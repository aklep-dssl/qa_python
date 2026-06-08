# Sprint_4

## Реализованные тесты

| # | Тестируемый метод | Тестовый метод | Покрываемый сценарий | Комментарий  |
|---|-------------------|----------------|----------------------|--------------|
| 1 |  add_new_book     |  test_add_new_book_add_two_books| Добавление 2 книг | Пример (кривой, т.к. использует несуществующий метод) |
| 2 |  add_new_book     | test_add_new_book_incorrect_length_not_added | Книги с некорректной длиной не добавляются | Негатив |
| 3 |  add_new_book     | test_add_new_book_duplicate_not_added | Дубликат не добавляется | Негатив |
| 4 |  set_book_genre   | test_set_book_genre_set_existing_genre | Установка существующего жанра для книги проходит успешно |   |
| 5 |  set_book_genre   | test_set_book_genre_set_non_existing_genre_fail  | Несуществующий жанр не устанавливается | Негатив |
| 6 |  get_book_genre   | test_get_book_genre_returns_genre | Возвращение жанра по названию книги работает |   |
| 7 | get_books_with_specific_genre | test_get_books_with_specific_genre_existing_book_returns_book | Возвращает 1 книгу по существующему жанру |   |
| 8 | get_books_with_specific_genre | test_get_books_with_specific_genre_incorrect_genre_returns_empty_list | По несуществующему жанру не возвращаются книги | Негатив |
| 9 | get_books_genre   | test_get_books_genre_add_2_books_return_2_books | Корректно отдаёт дикт с 2 книгами с заданным жанром |   |
| 10 | get_books_genre   | test_get_books_genre_no_books_return_empty_dict | Корректно отдаёт пустой дикт, если книг не добавлено |   |
| 11 | get_books_for_children | test_get_books_for_children_add_children_books_return_children_books | Отдаёт 1 книгу с детским жанром |   |
| 12 | get_books_for_children | test_get_books_for_children_add_non_children_books_return_empty_list | Отдаёт пустой список, если добавлены только книги с ограничением по возрасту | Негатив |
| 13 | add_book_in_favorites | test_add_book_in_favorites_add_1_fav_book_return_1_fav_book | Добавляет 1 книгу в избранное, она появляется в списке избранных |   |
| 14 | delete_book_from_favorites | test_delete_book_from_favorites_add_1_delete_1_return_empty_favlist | Удаляет добавленную в избранное книгу, проверяет пустой ли список избранного |   |
| 15 | get_list_of_favorites_books | test_get_list_of_favorites_books_added_2_fav_return_2_fav | Добавляет 2 книги в избранное, отдаёт список избранного |   |

## Нереализованные тесты

| # | Тестируемый метод | Покрываемый сценарий |
|---|-------------------|----------------------|
| 1 | add_new_book      | Добавление книг (тест из примера кривой) |
| 2 | get_books_with_specific_genre | Запрос по жанрам при наличии нескольких книг с разными жанрами |
| 3 | get_books_for_children | Запрос книг для детей при наличии книг для детей и не для детей в дикте |
| 4 | add_book_in_favorites | Добавление нескольких книг в избранное |
| 5 | delete_book_from_favorites | Удаление части книг из избранного |