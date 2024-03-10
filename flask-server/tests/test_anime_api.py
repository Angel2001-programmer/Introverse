import unittest
from unittest import TestCase
import sys
sys.path.append("..")
from app import create_app, db
from config import TestConfig
from models.content_models import Anime
from mock_data import anime_list


def insert_anime():
    """Insert mock anime data into the database"""
    for i in range(len(anime_list)):
        new_anime = Anime(anime_id=anime_list[i]["anime_id"], anime_name=anime_list[i]["anime_name"],
                          anime_genre=anime_list[i]["anime_genre"], where_tw=anime_list[i]["where_tw"],
                          anime_script=anime_list[i]["anime_script"], anime_image=anime_list[i]["anime_image"])
        db.session.add(new_anime)
        db.session.commit()


class TestAnimeAPI(TestCase):
    """Test for anime related suggestions within the content namespace, inheriting directly from
    TestCase (rather than TestAPI class) so can insert all mock data into tables within setUp function"""

    def setUp(self):
        """Set up our test database and work within the context of our application"""
        self.app = create_app(TestConfig)

        self.client = self.app.test_client(self)

        with self.app.app_context():

            db.create_all()
            insert_anime()     
         
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

    def test_get_anime_by_genre(self):
        """Test get list of anime by a genre that exists"""
        genre = "Seinen"
        get_response = self.client.get(f"/content/anime/genre/{genre}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 4)

    def test_get_anime_by_genre_case_different(self):
        """Test get list of anime by a genre that exists, mixed case"""
        genre = "SEiNen"
        get_response = self.client.get(f"/content/anime/genre/{genre}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 4)
    
    def test_get_anime_by_genre_doesnt_exist(self):
        """Test get anime by a genre that doesn't exist, results list empty"""
        genre = "Testing"
        get_response = self.client.get(f"/content/anime/genre/{genre}")
        status_code = get_response.status_code
        expected = []
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)
        self.assertEqual(expected, result)

    def test_get_anime_by_title_exact(self):
        """Test get list of books by title, search exact title"""
        title = "Death Note"
        get_response = self.client.get(f"/content/anime/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_anime_by_title_partial(self):
        """Test get list of anime by title, partial search of title"""
        title = "on"
        get_response = self.client.get(f"/content/anime/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 2)

    def test_get_anime_by_title_no_results(self):
        """Test get list of anime by title, no match"""
        title = "Sword Art Online"
        get_response = self.client.get(f"/content/anime/title/{title}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 0)

    def test_get_anime_by_where_to_watch_exact_only(self):
        """Test get list of anime by where to watch, search that exact platform"""
        stream = "Crunchyroll"
        get_response = self.client.get(f"/content/anime/stream/{stream}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)
        print(list_length)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 10)

    def test_get_anime_by_where_to_watch_partial(self):
        """Test get list of anime by where to watch, returns any that contain that streaming platform"""
        stream = "ix"
        get_response = self.client.get(f"/content/anime/stream/{stream}")
        status_code = get_response.status_code
        result = get_response.json
        list_length = len(result)

        self.assertEqual(status_code, 200)
        self.assertEqual(list_length, 1)

    def test_get_anime_by_where_to_watch_no_results(self):
        """Test get list of anime by streaming platform, no match"""
        stream = "Prime"
        get_response = self.client.get(f"/content/anime/stream/{stream}")
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
