import json
import requests
import sys
from http import HTTPStatus


class WebService():

    def get(self, URL):
        """
        Executes HTTP GET request at the specified URL with an expectation of a json response

        Args:
             URL (str): to send the request to
        Return:
             status (int): HTTP status code of the request
             json_content (str): HTTP content of the request or exception stack trace
        """
        try:
            response = requests.get(url=URL)
        except:
            # In case of an exception, return bad request code and the exception class
            return HTTPStatus.BAD_REQUEST, sys.exc_info()
        status = response.status_code

        try:
            json_content = json.loads(response.content)
        except:
            # In case the format is not JSON,return bad request code and the exception class
            return HTTPStatus.BAD_REQUEST, sys.exc_info()
        return status, json_content

    def post(self, URL, post_data):
        """
        Executes HTTP POST request at the specified URL with an expectation of a json response

        Args:
            URL (str): to send the request to
            post_data (str): HTTP post data
        Return:
            status (int): HTTP status code of the request
            json_content (str): HTTP content of the request or exception stack trace
        """
        try:
            response = requests.post(URL, post_data)
        except:
            # In case of invalid URL, return bad request code and the exception class
            return HTTPStatus.BAD_REQUEST, sys.exc_info()
        status = response.status_code

        try:
            json_content = json.loads(response.content)
        except:
            # In case the format is not JSON, return bad request code and the exception class
            return HTTPStatus.BAD_REQUEST, sys.exc_info()
        return status, json_content

    # Implement HTTP PUT functionality
    def put(self):
        pass

    # Implement HTTP DELETE functionality
    def delete(self):
        pass
