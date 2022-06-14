from sidorov5 import *
import pytest
import datetime


class TestHomework:
    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        print(f'\nTEST START : {datetime.datetime.now()}')
        yield
        print(f'\nTEST END : {datetime.datetime.now()}')
        print('*' * 150)

    @pytest.mark.check_name
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "name, result",
        [
            ("", "Error: empty name!"),
            ("Jack If Kusto", "Error: name can't contain more than one space!"),
            (" ", "Error: the name must contain at least 3 characters!")

        ]
    )
    def test_name_positive(self, name, result):
        assert validate_name(name) == result

    @pytest.mark.check_name
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "name, result",
        [
            ("Aliaksei", "Hello, Aliaksei."),
            ("123123123", "Hello, 123123123."),
            ("Jack If", "Hello, Jack If.")

        ]
    )
    def test_name_negative(self, name, result):
        assert validate_name(name) != result

    @pytest.mark.check_age
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "age, result",
        [
            (-2, "Error: enter the correct age!"),
            (5, "Error: you need to grow up to 14 years old!"),
            (20, "")
        ]
    )
    def test_age_positive(self, age, result):
        assert validate_age(age) == result

    @pytest.mark.check_age
    @pytest.mark.negative
    @pytest.mark.parametrize(
        'age, result',
        [
            (2, ""),
            (15, "You are 15 years old."),
            (25, "You are 25 years old.")
        ]
    )
    def test_age_negative(self, age, result):
        assert validate_age(age) != result

    @pytest.mark.clean
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name, expected',
        [
            ("alex         ", "alex"),
            ("         alex", "alex"),
            ("   alex    ", "alex")
        ]
    )
    def test_clean_positive(self, name, expected):
        assert clean(name) == expected

    @pytest.mark.clean
    @pytest.mark.negative
    @pytest.mark.parametrize(
        'name, expected',
        [
            ("  alex", "  alex"),
            ("alex   ", "alex   "),
            ("  alex  ", "  alex  ")

        ]
    )
    def test_clean_negative(self, name, expected):
        assert clean(name) != expected

    @pytest.mark.main
    @pytest.mark.positive
    @pytest.mark.parametrize(
        'name,age,expected',
        [
            ('Alex', 27, "Hello, Alex. You are 27 years old. "),
            ('Aliaksei', 25,
             "Hello, Aliaksei. You are 25 years old. Don't forget to replace your passport after 25 years."),
            ('Jack If', 15, "Hello, Jack If. You are 15 years old. ")
        ]
    )
    def test_main_positive(self, name, age, expected):
        assert main(name, age) == expected

    @pytest.mark.main
    @pytest.mark.negative
    @pytest.mark.parametrize(
        'name,age,expected',
        [
            ("al", 30, "Hello, al. You are 30 years old. "),
            ("alex", 10, "Hello, alex. You are 10 years old. "),
            ("Jack If Kusto", -5, "Hello, Jack if Kusto. You are -5 years old. ")
        ]
    )
    def test_main_negative(self, name, age, expected):
        assert main(name, age) != expected
