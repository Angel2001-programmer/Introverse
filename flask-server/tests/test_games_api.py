import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig
from models.content_models import Games
from mock_data import games_list


def insert_games():
    """Insert mock game data into the database"""
    for i in range(len(games_list)):
        new_game = Games(game_id=games_list[i]["game_id"], game_name=games_list[i]["game_name"],
                         game_genre=games_list[i]["game_genre"], w_console=games_list[i]["w_console"],
                         price=games_list[i]["price"], game_script=games_list[i]["game_script"],
                         game_image=games_list[i]["game_image"])
        db.session.add(new_game)
        db.session.commit()


class TestGamesAPI(TestCase):
    """Test for game related suggestions within the content namespace, inheriting directly from
    TestCase (rather than TestAPI class) so can insert all mock data into tables within setUp function"""

    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():

            db.create_all()
            insert_games()      

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

    def test_get_game_by_genre(self):
        """Test get list of games by a genre that exists"""
        genre = "simulation"
        get_response = self.client.get(f"/content/games/genre/{genre}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 4)

    def test_get_game_by_genre_case_different(self):
        """Test get list of books by a genre that exists, mixed case"""
        genre = "SimuLATION"
        get_response = self.client.get(f"/content/games/genre/{genre}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 4)
    
    def test_get_game_by_genre_doesnt_exist(self):
        """Test get game by a genre that doesn't exist, results list empty"""
        genre = "Testing"
        get_response = self.client.get(f"/content/games/genre/{genre}")
        status_code = get_response.status_code
        expected = []
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)
        self.assertEqual(expected, result)

    def test_get_game_by_title_exact(self):
        """Test get list of games by title, search exact title"""
        title = "God of War"
        get_response = self.client.get(f"/content/games/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_game_by_title_partial(self):
        """Test get list of games by title, partial search of title"""
        title = "of"
        get_response = self.client.get(f"/content/games/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 2)

    def test_get_game_by_title_no_results(self):
        """Test get list of books by title, no match"""
        title = "The Legend of Testing"
        get_response = self.client.get(f"/content/games/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)

    def test_get_game_by_console_exact_only(self):
        """Test get list of games by console, search exact combination of consoles"""
        console = "PC, NINTENDO SWITCH, XBOX, PLAYSTATION"
        get_response = self.client.get(f"/content/games/console/{console}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 2)

    def test_get_game_by_console_partial(self):
        """Test get list of games by console, partial search, returns any that contain that console"""
        console = "switch"
        get_response = self.client.get(f"/content/games/console/{console}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 6)

    def test_get_game_by_console_no_results(self):
        """Test get list of games by console, no match"""
        console = "SNES"
        get_response = self.client.get(f"/content/games/console/{console}")
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
