def my_func():
    return 4


def test_my_func(snapshot):
    return_value = my_func()
    #assert return_value == 2
    snapshot.assert_match(return_value, 'gpg_response')


def test_something(snapshot):
    snapshot.assert_match([1, 2, 3, 4], 'list')


def add(a, b):
    sum_of_two_numbers =  a + b
    return sum_of_two_numbers


def test_add_with_postive_values(snapshot):
    # Arrange
    a = 1
    b = 2

    # Act
    return_value = add(a, b)

    # Assert
    snapshot.assert_match(return_value, 'sum_of_positive_numbers')


def test_add_with_float_values(snapshot):
    # Arrange
    a = 1.4
    b = 2.5

    # Act
    return_value = add(a, b)

    # Assert
    snapshot.assert_match(return_value, 'sum_of_float_numbers')


def test_add_with_negative_values(snapshot):
    # Arrange
    a = -1
    b = 2

    # Act
    return_value = add(a, b)

    # Assert
    snapshot.assert_match(return_value, 'sum_of_negative_numbers')


def get_dict():
    sample_dict = {
        "id": 1,
        "name": "user"
    }
    return sample_dict

def test_sample_dict(snapshot):
    # Arrange

    # Act
    return_value = get_dict()

    # Assert
    snapshot.assert_match(return_value, 'sample_dict')