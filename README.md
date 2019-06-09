# pyapitest : Cloud API Testing in Python

pyapitest is a python tool for testing cloud based RESTful APIs. It is built on the foundations of Pytest, a popular python unit testing framework.

Currently following four APIs are being tested in the tool:

* http://services.groupkt.com/country/get/all
* http://services.groupkt.com/country/get/iso2code/{alpha2_code}
* http://services.groupkt.com/country/get/iso3code/{alpha3_code}
* http://services.groupkt.com/country/search?text={texttosearch}

## Dockerization

The application is dockerized and is available on [docker hub](https://hub.docker.com/r/shilpabansal/pyapitest)  
You may install and run the docker image locally by executing the following commands

```bash
docker pull shilpabansal/pyapitest
docker run -it shilpabansal/pyapitest
```

## Installation

Requires [Python 3.7](https://www.python.org/downloads/)  
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the dependencies   
You can install these dependencies in your own virtual environment using [Anaconda](https://www.anaconda.com/distribution/)

```bash
pip install -r requirements.txt
```

## Command line usage

To run the tests and generate a report, execute following

```bash
pytest ~/src/tests --html=report.html
```

## Project Structure

```bash
pyapitest
├── Dockerfile
├── README.md
├── TESTCASES.md 
├── requirements.txt
├── resources                             # Configuration Module                    
│   └── application.properties
├── src
│   ├── services                          # Networking Module
│   │   └── webService.py
│   ├── tests                             # API Tests Module
│   │   ├── test_service_get_all.py
│   │   ├── test_service_get_iso2.py
│   │   ├── test_service_get_iso3.py
│   │   └── test_service_search_text.py
│   └── utils                             # Utilities Module
│       ├── commonUtilities.py
│       ├── propertyConfig.py
│       ├── schemas.py
│       └── stringConstants.py
└── units                                 # Unit Test Module
    ├── services
    │   └── test_webservice.py
    └── utils
        ├── test_commonUtil.py
        ├── test_propertyConfig.py
        └── test_schemas.py
```

## Value Proposition

pyapitest tool is quite beneficial for testing cloud based REST APIs. It is built on the python unit testing framework [pytest](https://docs.pytest.org/en/latest/) and derives its design from popular tools like [POSTMAN](https://www.getpostman.com/) and [JMeter](https://jmeter.apache.org/)
* The tool runs 23 positive and negative tests against four web services for a variety of valid and invalid test data. It also checks against Cross site scripting (XSS) validation and unicode based internationalized data
* The tool can be easily integrated with CI/CD pipeline for automated regression testing

## Test Cases
Details of all the test cases and assumptions can be found in a separate document [here](TESTCASES.md)

## Limitations
There are few limitations in the current tool that can be addressed in the future iterations of the product.

* The tool currently doesn't support multithreading and firing web request concurrently. Supporting multithreading would allow us to do load testing on the web services which will assist in benchmarking the performance of the service 

* While the tool supports html report generation of the executed test cases, it doesn't support a similar GUI to modify the test cases or properties of the test as per the business needs. A UI to input the properties would be useful for business teams to use the tool.

* The test data for the services can be read from a xls or json file in future. This will allow non developer teams to add/update/delete the test data whenever required

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
