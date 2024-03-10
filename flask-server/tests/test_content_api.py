import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig
from models.content_models import Books, Anime, Games
from mock_data import books_list, anime_list, games_list


def insert_books():
    """Insert mock book data into the database"""
    for i in range(len(books_list)):
        new_book = Books(book_id=books_list[i]["book_id"], book_name=books_list[i]["book_name"],
                         book_author=books_list[i]["book_author"], book_genre=books_list[i]["book_genre"],
                         price=books_list[i]["price"], book_script=books_list[i]["book_script"],
                         book_image=books_list[i]["book_image"])
        db.session.add(new_book)
        db.session.commit()


def insert_anime():
    """Insert mock anime data into the database"""
    for i in range(len(anime_list)):
        new_anime = Anime(anime_id=anime_list[i]["anime_id"], anime_name=anime_list[i]["anime_name"],
                          anime_genre=anime_list[i]["anime_genre"], where_tw=anime_list[i]["where_tw"],
                          anime_script=anime_list[i]["anime_script"], anime_image=anime_list[i]["anime_image"])
        db.session.add(new_anime)
        db.session.commit()


def insert_games():
    """Insert mock game data into the database"""
    for i in range(len(games_list)):
        new_game = Games(game_id=games_list[i]["game_id"], game_name=games_list[i]["game_name"],
                         game_genre=games_list[i]["game_genre"], w_console=games_list[i]["w_console"],
                         price=games_list[i]["price"], game_script=games_list[i]["game_script"],
                         game_image=games_list[i]["game_image"])
        db.session.add(new_game)
        db.session.commit()


class TestContentAPI(TestCase):
    """Test for content namespace routes, inheriting directly from TestCase (rather than TestAPI class)
    so can insert all mock data into tables within setUp function"""

    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():

            db.create_all()

            insert_books()
            insert_anime()
            insert_games()

    def test_hello_world(self):
        """Test the hello world route"""
        hello_response = self.client.get("/content/hello")
        status_code = hello_response.status_code
        result = hello_response.json
        expected = {"message": "Hello world!"}

        self.assertEqual(status_code, 200)
        self.assertEqual(expected, result)            
    
    def test_get_all_books(self):
        """Test get all books"""
        get_response = self.client.get("/content/books")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_book_by_id(self):
        """Test get book by id"""
        book_id = 1
        get_response = self.client.get(f"/content/books/id/{book_id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_book_by_diff_id(self):
        """Test get book by different id"""
        book_id = 12
        get_response = self.client.get(f"/content/books/id/{book_id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_book_by_id_doesnt_exist(self):
        """Test get book by id that doesn't exist"""
        book_id = 42
        get_response = self.client.get(f"/content/books/id/{book_id}")
        status_code = get_response.status_code
        expected = {'message': f'The requested URL was not found on the server. If you entered the URL manually please '
                               f'check your spelling and try again. You have requested this URI '
                               f'[/content/books/id/{book_id}] but did you mean /content/books/id/<int:id> or '
                               f'/content/books/title/<string:title> or /content/books ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)
         
    def test_get_all_anime(self):
        """Test get all anime"""
        get_response = self.client.get("/content/anime")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)
    
    def test_get_anime_by_id(self):
        """Test get anime by id"""
        anime_id = 1
        get_response = self.client.get(f"/content/anime/id/{anime_id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_anime_by_id_doesnt_exist(self):
        """Test get anime by id that doesn't exist"""
        anime_id = 42
        get_response = self.client.get(f"/content/anime/id/{anime_id}")
        status_code = get_response.status_code
        expected = {'message': f'The requested URL was not found on the server. If you entered the URL manually please '
                               f'check your spelling and try again. You have requested this URI '
                               f'[/content/anime/id/{anime_id}] but did you mean /content/anime/id/<int:id> or '
                               f'/content/games/id/<int:id> or /content/anime/title/<string:title> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_all_games(self):
        """Test get all games"""
        get_response = self.client.get("/content/games")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)
    
    def test_get_game_by_id(self):
        """Test get game by id"""
        game_id = 1
        get_response = self.client.get(f"/content/games/id/{game_id}")
        status_code = get_response.status_code

        self.assertEqual(status_code, 200)

    def test_get_game_by_id_doesnt_exist(self):
        """Test get game by id that doesn't exist"""
        game_id = 42
        get_response = self.client.get(f"/content/games/id/{game_id}")
        status_code = get_response.status_code
        expected = {'message': f'The requested URL was not found on the server. If you entered the URL manually please '
                               f'check your spelling and try again. You have requested this URI '
                               f'[/content/games/id/{game_id}] but did you mean /content/games/id/<int:id> or '
                               f'/content/anime/id/<int:id> or /content/games/title/<string:title> ?'}
        result = get_response.json

        self.assertEqual(status_code, 404)
        self.assertEqual(expected, result)

    def test_get_book_by_genre(self):
        """Test get list of books by a genre that exists"""
        genre = "Fantasy"
        get_response = self.client.get(f"/content/books/genre/{genre}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 4)

    def test_get_book_by_genre_case_different(self):
        """Test get list of books by a genre that exists, mixed case"""
        genre = "fanTASY"
        get_response = self.client.get(f"/content/books/genre/{genre}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 4)
    
    def test_get_book_by_genre_doesnt_exist(self):
        """Test get book by a genre that doesn't exist, results list empty"""
        genre = "Testing"
        get_response = self.client.get(f"/content/books/genre/{genre}")
        status_code = get_response.status_code
        expected = []
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)
        self.assertEqual(expected, result)

    def test_get_book_by_author_exact_name(self):
        """Test get list of books by an author, exact name search"""
        author = "J.K. Rowling"
        get_response = self.client.get(f"/content/books/author/{author}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_book_by_author_full_surname(self):
        """Test get list of books by an author, partial search full surname"""
        author = "Rowling"
        get_response = self.client.get(f"/content/books/author/{author}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_book_by_author_partial_name(self):
        """Test get list of books by an author, partial search of name"""
        author = "le"
        get_response = self.client.get(f"/content/books/author/{author}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 3)

    def test_get_book_by_author_no_results(self):
        """Test get list of books by an author, no match"""
        author = "1"
        get_response = self.client.get(f"/content/books/author/{author}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)

    def test_get_book_by_title_exact(self):
        """Test get list of books by title, search exact title"""
        title = "Unbroken: A World War II Story of Survival"
        get_response = self.client.get(f"/content/books/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_book_by_title_partial(self):
        """Test get list of books by title, partial search of title"""
        title = "The"
        get_response = self.client.get(f"/content/books/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)
        print(list_length)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 5)

    def test_get_book_by_title_no_results(self):
        """Test get list of books by title, no match"""
        title = "The Very Hungry Caterpillar"
        get_response = self.client.get(f"/content/books/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)

    def tearDown(self):
        """Destroy all the instances created for testing, remove sessions and drop tables"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
