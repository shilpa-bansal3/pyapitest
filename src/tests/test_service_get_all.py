import unittest
from http import HTTPStatus
from jsonschema import validate
from src.services.webService import WebService
from src.utils.commonUtilities import CommonUtilities
from src.utils.propertyConfig import PropertyConfig
from src.utils.schemas import Schemas


class Tests_service_get_all(unittest.TestCase):
    # Creating object of class PropertyConfig
    _properties_ = PropertyConfig()

    @classmethod
    def setUpClass(self):
        # Call the setup method of class PropertyConfig
        # Read the hostname and endpoint from properties file and create URL
        self._properties_.setup()
        hostname = self._properties_._config_.get('dev', 'url')
        endpoint = self._properties_._config_.get('dev', 'endpoint.getall')
        self.url = hostname + endpoint
        self.service = WebService()

    def test_get_all_valid(self):
        """
        Testing the webservice for a valid request
        Expectation: Webservice should return HTTP Status 200 OK and a valid json with all records in the content
        """
        status_code, content = self.service.get(self.url)
        assert status_code == HTTPStatus.OK
        # Check if the JSON format is valid
        validate(instance=content, schema=Schemas.schema_all)
        # Read the message returned in the content
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Read the number of records returned
        total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        assert total_no_of_records != -1
        assert len(content['RestResponse']['result']) == int(total_no_of_records)

    def test_get_all_valid_with_query_params(self):
        """
        Testing the webservice for a valid request with additional query parameters
        Expectation: Webservice should return HTTP Status 200 OK and a valid json with all records in the content
        """
        rand = CommonUtilities.generate_random_string(5)
        url = self.url + '?' + rand + '=' + rand
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK
        # Check if the JSON format is valid
        validate(instance=content, schema=Schemas.schema_all)
        # Read the message returned in the content
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Read the number of records returned
        total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        assert total_no_of_records != -1
        assert len(content['RestResponse']['result']) == int(total_no_of_records)

    def test_get_all_invalid_request(self):
        """
        Testing the webservice for an invalid request with additional path information in the URI
        Expectation: Webservice should return HTTP BAD REQUEST
        """
        rand = CommonUtilities.generate_random_string(5)
        url = self.url + '/' + rand
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.BAD_REQUEST

    def test_get_all_post_method(self):
        """
        Testing the webservice for HTTP POST Method
        Expectation: Webservice should return HTTP BAD REQUEST
        """
        rand = CommonUtilities.generate_random_string(5)
        status_code, content = self.service.post(self.url, rand)
        assert status_code == HTTPStatus.BAD_REQUEST
