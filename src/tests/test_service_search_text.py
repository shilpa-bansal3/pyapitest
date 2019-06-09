import re
import unittest
from http import HTTPStatus
from jsonschema import validate
from src.services.webService import WebService
from src.utils.commonUtilities import CommonUtilities
from src.utils.propertyConfig import PropertyConfig
from src.utils.schemas import Schemas
from src.utils.stringConstants import StringConstants


class Tests_service_search_text(unittest.TestCase):
    # Creating object of class PropertyConfig
    _properties_ = PropertyConfig()

    @classmethod
    def setUpClass(self):
        # Call the setup method of class PropertyConfig
        # Read the hostname and endpoint from properties file and create URL
        self._properties_.setup()
        hostname = self._properties_._config_.get('dev', 'url')
        endpoint = self._properties_._config_.get('dev', 'endpoint.getall')
        endpoint_searchtext = self._properties_._config_.get('dev', 'endpoint.searchtext')
        self.url_testdata = hostname + endpoint
        self.url = hostname + endpoint_searchtext
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

    def search_text(self, content, text_to_search):
        """
        Function to check if text exists in every record of the content list

        Args:
            content (list): a list of JSON records
            text_to_search (str): text to search in the elements of JSON record
        Return:
            (bool): return true if the text to search is found in any one of the elements of a json record
        """
        length = len(content)
        for i in range(0, length):
            # Verify the text to search is atleast part of 1 of the property of the result
            if not (text_to_search in content[i]['name'] or text_to_search in content[i]['alpha2_code'] \
                    or text_to_search in content[i]['alpha3_code']):
                return False
        return True

    def test_search_text_valid_iso2(self):
        """
        Testing the service for valid results with search text as any valid ISO2CODE
        """
        # Fetch test data and read the ISO2CODE from the first record of the result
        assert self.fetch_data_and_validate()
        assert len(self.test_data_list) > 0
        item = self.test_data_list[0]
        iso2code = item['alpha2_code']

        # Create URL to test with ISO2CODE
        # Fetch status code and content from get method
        url2 = self.url + iso2code
        status_code, content = self.service.get(url2)
        assert status_code == HTTPStatus.OK

        # Check if the JSON format of content is valid
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_all)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Read the number of records returned
        total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        assert total_no_of_records != -1

        # Verify if the length of results list is same as the no mentioned in messages
        # Verify if the result list contains the iso2code as text in name,iso2code or iso3code
        assert len(content['RestResponse']['result']) == int(total_no_of_records)
        assert self.search_text(content['RestResponse']['result'], iso2code)

    def test_search_text_valid_iso3(self):
        """
        Testing the service for valid results with search text as any valid ISO3CODE
        """
        # Fetch test data and read the ISO3CODE from the first record of the result
        assert self.fetch_data_and_validate()
        assert len(self.test_data_list) > 0
        item = self.test_data_list[0]
        iso3code = item['alpha3_code']

        # Create URL to test with ISO3CODE
        # Fetch status code and content from get method
        url2 = self.url + iso3code
        status_code, content = self.service.get(url2)

        # Check if the JSON format of content is valid
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_all)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Read the number of records returned
        total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        assert total_no_of_records != -1

        # Verify if the length of results list is same as the no mentioned in messages
        # Verify if the result list contains the iso3code as text in name,iso2code or iso3code
        assert len(content['RestResponse']['result']) == int(total_no_of_records)
        assert self.search_text(content['RestResponse']['result'], iso3code)

    def test_search_text_valid_name(self):
        """
        Testing the service for valid results with search text as any valid Name
        Expectation: Service should return valid results
        """
        # Fetch test data and read the name from the first record of the result
        assert self.fetch_data_and_validate()
        assert len(self.test_data_list) > 0
        item = self.test_data_list[0]
        name = item['name']

        # Create URL to test with name
        # Fetch status code and content from get method
        url = self.url + name
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK

        # Check if the JSON format of content is valid
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_all)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Read the number of records returned
        total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        assert total_no_of_records != -1

        # Verify if the length of results list is same as the no mentioned in messages
        # Verify if the result list contains the name as text in name,iso2code or iso3code
        assert len(content['RestResponse']['result']) == int(total_no_of_records)
        assert self.search_text(content['RestResponse']['result'], name)

    def test_search_text_invalid(self):
        """
        Testing the service with invalid text
        Expectation: Service should handle the request gracefully and return no matching records
        """
        # Create invalid text with random number
        # Fetch the status code and content from get method
        rand = CommonUtilities.generate_random_string()
        url = self.url + rand
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK

        # Check if the JSON format of content is valid
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_search_invalid)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Check if we get 'no matching' message and result list is empty
        assert StringConstants.no_matching in resp_msg
        assert not content['RestResponse']['result']

    def test_search_text_xss(self):
        """
        Testing to query records for validation against Cross Site Scripting (XSS) attacks
        Expectation: Service should handle the request gracefully and return a valid json response with no records
        """
        url = self.url + '<script>alert()</script>'
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK
        # In this case, the output is JSON with empty result list
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_search_invalid)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Check if we get 'no matching' message and result list is empty
        assert StringConstants.no_matching in resp_msg
        assert not content['RestResponse']['result']

    def test_search_text_empty_string(self):
        """
        Testing to query records with empty search text
        Expectation: Service should return all records
        """
        status_code, content = self.service.get(self.url)
        assert status_code == HTTPStatus.OK

        # Check if the JSON format of content is valid as it will return the full list
        # Read the message returned in the content
        validate(instance=content, schema=Schemas.schema_all)
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Read the number of records returned
        total_no_of_records = CommonUtilities.fetch_total_records(resp_msg)
        assert total_no_of_records != -1

        # Verify the total no of records matches in message and result list
        assert len(content['RestResponse']['result']) == int(total_no_of_records)

    def test_search_text_intl(self):
        """
        Testing to query records with unicode characters in the search text
        Expectation: Service should handle the request gracefully and output no matching records
        """
        url = self.url + 'ÖöÜü'
        status_code, content = self.service.get(url)
        assert status_code == HTTPStatus.OK
        validate(instance=content, schema=Schemas.schema_search_invalid)
        # Read the message returned in the content
        resp = content['RestResponse']['messages']
        assert len(resp) == 1
        resp_msg = resp[0]

        # Check if we get 'no matching' message and result list is empty
        assert StringConstants.no_matching in resp_msg
        assert not content['RestResponse']['result']
