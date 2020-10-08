import pytest


@pytest.fixture(autouse=True)
def setup_fixture():
    print("\nStart test.... ")
    yield
    print("\nStop test....")


# Методы string
class TestClassString:
    def first_symbol_of_string(self, word):
        return word[0]

    def upper_word(self, word):
        return word.upper()

    def check_letter_in_string(self, letter, word):
        if letter in word:
            return True

    def replace_letter(self, letter1, letter2, word):
        return word.replace(letter1, letter2)

    def find_letter_index(self, word, letter):
        return word.find(letter)

    def count_letter(self, word, letter):
        return word.count(letter)


# Фикстуры для string
@pytest.fixture(params=["cat", "dog", "air", "bye", "day"])
def fixture_get_len_string(request):
    return request.param


@pytest.fixture
def fixture_first_symbol_of_string():
    return TestClassString()


@pytest.fixture
def fixture_upper_word():
    return TestClassString()


@pytest.fixture
def fixture_check_letter_in_sring():
    return TestClassString()


@pytest.fixture
def fixture_replace_letter():
    return TestClassString()


@pytest.fixture
def fixture_find_letter_index():
    return TestClassString()


@pytest.fixture
def fixture_count_letter():
    return TestClassString()


# Методы list
class TestClassList:
    def get_len_list(self, lst):
        return len(lst)

    def change_first_el_in_lst(self, lst, value):
        lst[0] = value
        return lst

    def append_value_to_list(self, lst, value):
        lst.append(value)
        return lst

    def concat_lists(self, lst1, lst2):
        return lst1 + lst2

# Фикстуры для list
@pytest.fixture
def fixture_get_len_list():
    return TestClassList()


@pytest.fixture
def fixture_change_first_el_in_lst():
    return TestClassList()


@pytest.fixture
def fixture_append_value_to_list():
    return TestClassList()


@pytest.fixture
def fixture_concat_lists():
    return TestClassList()


# Методы set
class TestClassSet:
    def add_value_to_set(self, set1, value):
        set1.add(value)
        return set1

    def get_len_set(self, set1):
        return len(set1)

    def clear_set(self, set1):
        set1.clear()
        return set1

    def join_sets(self, set1, set2):
        set3 = set1.union(set2)
        return set3


# Фикстуры для set
@pytest.fixture
def fixture_add_value_to_set():
    return TestClassSet()


@pytest.fixture
def fixture_get_len_set():
    return TestClassSet()


@pytest.fixture
def fixture_clear_set():
    return TestClassSet()


@pytest.fixture
def fixture_join_sets():
    return TestClassSet()


# Методы dict
class TestClassDict:
    def get_value(self, diction, key):
        return diction.get(key)

    def add_key_to_dict(self, diction, key, value):
        diction[key] = value
        return diction

    def del_key_from_dict(self, diction, key):
        diction.pop(key)
        return diction

    def copy_dict(self, diction):
        d = diction.copy()
        return d


# Фикстуры для dict
@pytest.fixture
def fixture_get_value():
    return TestClassDict()


@pytest.fixture
def fixture_add_key_to_dict():
    return TestClassDict()


@pytest.fixture
def fixture_del_key_from_dict():
    return TestClassDict()


@pytest.fixture
def fixture_copy_dict():
    return TestClassDict()


@pytest.fixture(params=[{"a": 89, "d": 67}, {"e": 0, "y": 5}, {"q": 65, "h": 90}, {"v": 7, "n": 61}])
def fixture_get_len_dicts(request):
    return request.param