from functions.level_4.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration


def test_fetch_app_config_field_with_field(filepath):
    assert fetch_app_config_field(filepath, 'url') == 'asdf'

def test_fetch_app_config_field_without_field(filepath):
    assert fetch_app_config_field(filepath, 'abc') is None

def test_fetch_extra_fields_configuration_success(filepath):
    assert fetch_extra_fields_configuration(filepath) == {'1asd': 2}

def test_fetch_extra_fields_configuration_empty(filepath_without_extra):
    assert fetch_extra_fields_configuration(filepath_without_extra) == {}

