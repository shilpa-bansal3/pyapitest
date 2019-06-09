import jsonschema
from src.utils.schemas import Schemas

class TestSchemas():
    """ Class to unit test if the defined json schema is itself accurate or not """

    def schema_check(self, schema_name):
        """
        Function to check if the created schema for json response is valid

        Args:
            schema_name (str): name of the schema to validate
        Return:
            (bool): true if the schema is valid, false otherwise
        """
        try:
            jsonschema.Draft4Validator(schema=schema_name).check_schema(schema=schema_name)
        except:
            return False
        return True

    def test_schema_all(self):
        assert self.schema_check(Schemas.schema_all)

    def test_schema_iso(self):
        assert self.schema_check(Schemas.schema_iso)

    def test_schema_iso_invalid(self):
        assert self.schema_check(Schemas.schema_iso_invalid)

    def test_schema_search_invalid(self):
        assert self.schema_check(Schemas.schema_search_invalid)
