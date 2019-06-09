from src.utils.commonUtilities import CommonUtilities

class Test_CommonUtil():
    """ Class to test common utility functions """

    def test_generate_random_string_length(self):
        length = 10
        str1 = CommonUtilities.generate_random_string(length)
        assert len(str1) == length

    def test_fetch_total_records_valid(self):
        num_records = CommonUtilities.fetch_total_records("Total [4] records")
        assert int(num_records) == 4

    def test_fetch_total_records_invalid(self):
        num_records = CommonUtilities.fetch_total_records("Total records")
        assert num_records is None
