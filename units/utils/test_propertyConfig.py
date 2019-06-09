from src.utils.propertyConfig import PropertyConfig

class Test_PropertyConfig():
    """ Class to unit test property configuration fetch"""

    def test_setup(self):
        property_config = PropertyConfig()
        property_config.setup()
        # If the config is read properly, valid sections would exist
        assert len(property_config._config_.sections()) > 0
