import random
import unittest
from http import HTTPStatus
from jsonschema import validate
from src.services.webService import WebService
from src.utils.commonUtilities import CommonUtilities
from src.utils.propertyConfig import PropertyConfig
from src.utils.schemas import Schemas
from src.utils.stringConstants import StringConstants


class Tests_service_get_iso3(unittest.TestCase):
    # Creating object of class PropertyConfig
    _properties_ = PropertyConfig()

    @classmethod
    def setUpClass(self):
        # Call the setup method of class PropertyConfig
        # Read the hostname and endpoint from properties file and create URL
        self._properties_.setup()
        hostname = self._properties_._config_.get('dev', 'url')
        endpoint = self._properties_._config_.get('dev', 'endpoint.getall')
        endpoint_iso3 = self._properties_._config_.get('dev', 'endpoint.getiso3')
        self.url_testdata = hostname + endpoint
        self.url = hostname + endpoint_iso3
        self.service = WebService()

    def fetch_data_and_validate(self):
        """
        Method to fetch, validate and store all records for future test cases
        Return:
            (bool): return True if method is successful in fetching the test data, false otherwise
        """
        # Fetch data for all records that will be used as test data in further methods
        # Check if the JSON format of test_content is valid
        status_code, test_content = self.service.get(self.url_testdata)
        validate(instance=test_content, schema=Schemas.schema_all)
        self.test_data_list = test_content['RestResponse']['result']
        # Read the message returned in the content
        resp = test_content['RestResponse']['messages']
        if len(resp) == 1:
            resp_msg = resp[0]
        else:
            return False
        # Read the number of records returned
        self.total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        if self.total_no_of_records != -1:
            return True
        else:
            return False

    def test_get_iso3_valid(self):
        """
        Testing to query records with randomly chosen valid iso3Codes
        Expectation: Service should return valid json as per the defined schema with certain number of records
        """
        assert self.fetch_data_and_validate()
        # Selecting random records from the output of all records to be used as
        # test case for this method
        no_of_test_cases = int(int(self.total_no_of_records) / 10)
        random_choice = random.sample(self.test_data_list, no_of_test_cases)
        for item in random_choice:
            iso3code = item['alpha3_code']
            # Create URL to test with ISO3CODE
            # Fetch status code and content from get method
            url = self.url + iso3code
            status_code, content = self.service.get(url)
            assert status_code == HTTPStatus.OK

            # Check if the JSON format of test_content is valid
            validate(instance=content, schema=Schemas.schema_iso)
            # Read the message returned in the content
            resp = content['RestResponse']['messages']
            assert len(resp) == 1
            resp_msg = resp[0]

            # Check if we get Country found message and required iso3code
            assert StringConstants.country_found in resp_msg
            assert content['RestResponse']['result']['alpha3_code'] == iso3code

    # Testing the URL with invalid ISO3CODE
    def test_get_iso3_invalid(self):
        """
        Testing to query records with randomly chosen invalid iso3Codes
        Expectation: Service should return a valid json as per the defined schema with zero records
        """
        # Create invalid ISO3CODE with random number
        # Fetch the status code and content from get method
        rand = CommonUtilities.generate_random_string(5)
        url = self.url + rand
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK

        # Check if the JSON format of content is valid
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_iso_invalid)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Check if we get 'no matching' message
        assert StringConstants.no_matching in resp_msg

    def test_get_iso3_post_method(self):
        """
        Testing to query records with a random invalid iso3Code using HTTP Post
        Expectation: Service should return a HTTP Bad Request
        """
        # Create invalid ISO3CODE with random number
        # Fetch the status code and content from get method
        rand = CommonUtilities.generate_random_string(5)
        url = self.url + rand
        # Fetch the status code from POST method
        status_code, content = self.service.post(url, rand)
        assert status_code == HTTPStatus.BAD_REQUEST

    def test_get_iso3_xss(self):
        """
        Testing to query records for validation against Cross Site Scripting (XSS) attacks
        Expectation: Service should return a HTTP Bad Request
        """
        url = self.url + '<script>alert()</script>'
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.BAD_REQUEST

    def test_get_iso3_empty_string(self):
        """
        Testing to query records with empty iSO3Code
        Expectation: Service should return a HTTP Bad Request
        """
        status_code, content = self.service.get(self.url)
        assert status_code == HTTPStatus.BAD_REQUEST

    def test_get_iso3_intl(self):
        """
        Testing to query records with unicode characters in the iSO3Code
        Expectation: Service should handle the request gracefully and output no matching records
        """
        url = self.url + 'ÖöÜü'
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK
        validate(instance=content, schema=Schemas.schema_iso_invalid)
        # Read the message returned in the content
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Check if we get 'no matching' message
        assert StringConstants.no_matching in resp_msg
