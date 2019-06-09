import re
import uuid

class CommonUtilities():
    """ Static utility class for commonly used functions """

    def generate_random_string(length = 5):
        """
        Function to generate a random string of given length

        Args:
            length (int): desired length of random string, defaults to 5 characters
        Return:
            (str) random string of specified length
        """
        random = str(uuid.uuid4()).upper().replace("-", "")
        return random[0:length]

    def fetch_total_records(resp_msg):
        """
        Function to parse number of records from a given string

        Args:
            resp_msg (str): expected format of the string is `Abcd [num] Defg`
        Return:
            numeric value enclosed in square braces if found, -1 otherwise
        """
        try:
            num = re.search(r'\[(.*)\]', resp_msg)
            if num:
                return num.group(1)
        except:
            return -1
