import configparser

class PropertyConfig():
    """
    Class to read all the configuration properties from the specified file

    Attributes:
        FILENAME (str): stores the name of the config file
        _config_ (dict): stores the parsed config file in a dictionary format
    """
    FILENAME = '././resources/application.properties'

    def __init__(self):
        self._config_ = configparser.RawConfigParser()


    def setup(self):
        """
        Function to read configuration file and store it in the config property
        Return:
            None
        """
        self._config_.read(self.FILENAME)
