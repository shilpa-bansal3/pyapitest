

# TEST CASES
1. TEST API 1 : ```http://services.groupkt.com/country/get/all```. Retrieve all countries 

   1.1 Test Case: Get All Valid Responses 
   ```python 
    test_get_all_valid 
   ```
   It uses the valid URL and verifies that the HTTP status code is 200 OK, the content returned from the service has a valid JSON format and matches the total number of records displayed in the message with the length of the results list. 

   1.2 Test Case: Get Valid Response with a Query Parameter in URL
   ```python 
    test_get_all_valid_with_query_params 
   ```
   The valid URL is appended with additional query parameters like ?abc=xyz and the service is called. The test verifies that the HTTP status code is 200 OK ,the content returned from the service has valid JSON format and matches the total number of records displayed in the message with the length of the results list. In short the output should be same as that of using a valid URL without any query params. The assumption here is that the query parameter doesn't influence the output of the service.

   1.3 Test Case: Get Invalid response with additional path information in URL
   ```python 
    test_get_all_invalid_request 
   ```
   This test appends a random string at the end of the URL and verifies the output. The output should return an error HTML page albeit the status code remains HTTP 200 OK. In an ideal scenario the web service should return HTTP 404 Not Found status code.

   1.4 Test Case: Get Invalid response with HTTP POST Method
   ```python 
    test_get_all_post_method 
   ```
   This test verifies the output of the service in case HTTP POST method is used instead of HTTP GET. Typically in an ideal scenario the web service should return HTTP 405 Method Not Allowed. However in this case the service returns an error html page with status code 200 OK, so the assertion of a bad request is fired programmatically.


2. TEST API 2 : ``` http://services.groupkt.com/country/get/iso2code/{alpha2_code} ``` . Testing the webservice to get the list of countries based on ISO2 code: We use the output of the service ```http://services.groupkt.com/country/get/all``` as input to this service for some of the test cases.

     2.1 Test Case: Get valid response with randomly chosen valid ISO2 codes 
   ```python 
    test_get_iso2_valid 
   ```
   The test case takes random 1/10th of the test data to test this service. It appends the ISO2CODE from the test records to the URL and calls the service. The test verifies the status code is 200, the result is valid JSON schema, and the text 'Country found' is present in the messages. It further also verifies the ISO2CODE of the record returned with that of the test data matches the input ISO2CODE.

   2.2 Test Case: Get a valid response with a randomly chosen invalid ISO2 code
   ```python 
    test_get_iso2_invalid 
   ```
   The service is tested with an invalid ISO2CODE generated randomly. It verifies that the status code is 200 and the JSON returned is a valid schema and No matching record is found in messages.

   2.3 Test Case: Get an invalid response with HTTP POST Method
   ```python 
    test_get_iso2_post_method 
   ```
   This test verifies the output of the service in case HTTP POST method is used instead of HTTP GET. Typically in an ideal scenario the web service should return HTTP 405 Method Not Allowed. However in this case the service returns an error html page with status code 200 OK, so the assertion of a bad request is fired programmatically.

   2.4 Test Case: Validation against cross-site-scripting attacks
   ```python 
    test_get_iso2_xss 
   ```
    URL is tested for validation against cross site scripting attacks by giving ```<script>alert()</script>``` as an ISO2CODE. The test verifies that the service handles it gracefully and returns an erroneous response.
 
    2.5 Test Case: NULL Check 
   ```python 
    test_get_iso2_empty_string 
   ```
   URL is tested without any ISO2CODE. The test verifies that the service handles it gracefully and returns an erroneous response. Given the lack of requirements, I assume that this behavior is correct.

   2.6 Test Case: Test for internationalization and unicode characters as input
   ```python 
    test_get_iso2_intl 
   ```
   The URL is tested with unicode characters such as german umlauts: 'ÖöÜü' as an ISO2CODE. It verifies that the status code is 200 and the JSON returned is a valid schema and No matching record is found in messages.


3. TEST API 3 : ```http://services.groupkt.com/country/get/iso3code/{alpha3_code}``` . Testing the webservice to get the list of countries based on ISO3 code: We use the output of the service ```http://services.groupkt.com/country/get/all``` as input to this service for some of the test cases.

    3.1 Test Case: Get valid response with randomly chosen valid ISO3 codes 
   ```python 
    test_get_iso3_valid 
   ```
   The test case takes random 1/10th of the test data to test this service. It appends the ISO3CODE from the test records to the URL and calls the service. The test verifies the status code is 200, the result is valid JSON schema, and the text 'Country found' is present in the messages. It further also verifies the ISO3CODE of the record returned with that of the test data matches the input ISO3CODE.

   3.2 Test Case: Get a valid response with a randomly chosen invalid ISO3 code
   ```python 
    test_get_iso3_invalid 
   ```
   The service is tested with an invalid ISO3CODE generated randomly. It verifies that the status code is 200 and the JSON returned is a valid schema and No matching record is found in messages.

   3.3 Test Case: Get an invalid response with HTTP POST Method
   ```python 
    test_get_iso3_post_method 
   ```
   This test verifies the output of the service in case HTTP POST method is used instead of HTTP GET. Typically in an ideal scenario the web service should return HTTP 405 Method Not Allowed. However in this case the service returns an error html page with status code 200 OK, so the assertion of a bad request is fired programmatically.

   3.4 Test Case: Validation against cross-site-scripting attacks
   ```python 
    test_get_iso3_xss 
   ```
    URL is tested for validation against cross site scripting attacks by giving ```<script>alert()</script>``` as an ISO2CODE. The test verifies that the service handles it gracefully and returns an erroneous response.
 
    3.5 Test Case: NULL Check 
   ```python 
    test_get_iso3_empty_string 
   ```
   URL is tested without any ISO3CODE. The test verifies that the service handles it gracefully and returns an erroneous response. Given the lack of requirements, I assume that this behavior is correct.

   3.6 Test Case: Test for internationalization and unicode characters as input
   ```python 
    test_get_iso3_intl 
   ```
   The URL is tested with unicode characters such as german umlauts: 'ÖöÜü' as an ISO3CODE. It verifies that the status code is 200 and the JSON returned is a valid schema and No matching record is found in messages.  

4. TEST API 4 : ```http://services.groupkt.com/country/search?text={text to search}``` . Testing the webservice to get the list of countries based on the search text: We use the output of the service ```http://services.groupkt.com/country/get/all``` as input to this service for some of the test cases.

    4.1 Test Case: Get valid response with a valid ISO2 code as the search text 
   ```python 
    test_search_text_valid_iso2 
   ```
   The URL is tested by reading the first record of the test data and passing the ISO2CODE from that record as search text. The test verifies the result is a valid JSON schema, the number of records displayed in messages is same as the length of the result list and all the records of resultant list contain the ISO2CODE.

    4.2 Test Case:  Get valid response with a valid ISO3 code as the search text 
   ```python 
    test_search_text_valid_iso3 
   ```
   The URL is tested by reading the first record of the test data and passing the ISO3CODE from that record as search text. The test verifies the result is a valid JSON schema, the number of records displayed in messages is same as the length of the result list and all the records of resultant list contain the ISO3CODE.

    4.3 Test Case:  Get valid response with randomly chosen valid country name as the search text 
   ```python 
    test_search_text_valid_name 
   ```
    The URL is tested by reading the first record of the test data and passing the country name from that record as search text. The test verifies the result is valid JSON schema, the number of records displayed in messages is same as the length of the result list and all the records of resultant list contain the country name used as search text. 

   4.4 Test Case: Get a valid response with a randomly chosen invalid search text
   ```python 
    test_search_text_invalid 
   ```
   The service is tested with an invalid search text generated randomly. It verifies that the status code is 200 and the JSON returned is a valid schema and No matching record is found in messages.

    4.5 Test Case: Validation against cross-site-scripting attacks
   ```python 
    test_search_text_xss 
   ```
    URL is tested for validation against cross site scripting attacks by giving ```<script>alert()</script>``` as a search text. The test verifies that the service handles it gracefully and returns an erroneous response.
 
    4.6 Test Case: NULL Check 
   ```python 
    test_search_text_empty_string 
   ```
   URL is tested without any search text. The expected outcome is list of all countries. The test verifies that the service handles it gracefully, returns a valid json response and the number of records displayed in messages is equal to the length of the results list.

    4.7 Test Case: Test for internationalization and unicode characters as input
   ```python 
    test_search_text_intl 
   ```
   The URL is tested with unicode characters such as german umlauts: 'ÖöÜü' as a search text. It verifies that the status code is 200 and the JSON returned is a valid schema and No matching record is found in messages.  

# Testing Assumptions

* Given the lack of requirements document, I have assumed that the output of the web service in all cases is the desired output. For instance if we execute an HTTP POST on the web service, ideally it should respond with a HTTP 405 Unsupported Method, however the web service responds with a HTTP 200 OK and a erroneous HTML. I have handled and designed my assertions accordingly to expect this behavior.



