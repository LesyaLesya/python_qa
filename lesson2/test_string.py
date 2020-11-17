class TestString:
    # Тест параметризован в conftest.py
    def test_get_len_string(self, fixture_get_len_string):
        assert len(fixture_get_len_string) == 3, "Wrong length for string"
        print(f"Word '{fixture_get_len_string}' has length 3")

    def test_first_symbol_of_string(self, fixture_first_symbol_of_string):
        assert fixture_first_symbol_of_string.first_symbol_of_string("python") == "p", "Wrong first letter in word"

    def test_upper_word(self, fixture_upper_word):
        assert fixture_upper_word.upper_word("python") == "PYTHON", "Word not in upper case"

    def test_check_letter_in_sring(self, fixture_check_letter_in_sring):
        assert fixture_check_letter_in_sring.check_letter_in_string("o", "python"), "No such a letter in word"

    def test_replace_letter(self, fixture_replace_letter):
        assert fixture_replace_letter.replace_letter("d", "m", "day") == "may", "Wrong word after replace letters"

    def test_find_letter_index(self, fixture_find_letter_index):
        assert fixture_find_letter_index.find_letter_index("testing", "s") == 2, "Wrong index for letter position"

    def test_count_letter(self, fixture_count_letter):
        assert fixture_count_letter.count_letter("abbbbaaaua", "a") == 5, "Wrong count of letter"
