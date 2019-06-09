from http import HTTPStatus
from src.services.webService import WebService

class Test_Webservice():
    """
    Class to unit test webservice module

    Attributes:
        webservice : Instance of the WebService class
        TEST_URL : a static url for json based HTTP request/response
    """
    webservice = WebService()
    TEST_URL = 'https://reqres.in/api/users?page=2'

    def test_get(self):
        status_code, content = self.webservice.get(self.TEST_URL)
        assert status_code == HTTPStatus.OK

    def test_get_invalid_url_error(self):
        status_code, content = self.webservice.get('INVALID_URL')
        assert status_code == HTTPStatus.BAD_REQUEST

    def test_get_non_json_response(self):
        status_code, content = self.webservice.get('http://google.com')
        assert status_code == HTTPStatus.BAD_REQUEST

    def test_post(self):
        status_code, content = self.webservice.post(self.TEST_URL, "randomdata")
        assert status_code == HTTPStatus.CREATED

    def test_post_invalid_url(self):
        status_code, content = self.webservice.post('INVALIDURL', "randomdata")
        assert status_code == HTTPStatus.BAD_REQUEST
