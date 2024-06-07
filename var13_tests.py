from var13 import count_deceased_children


def test_all_ports():
    data = [
        {'Age': 5, 'Survived': '0', 'Embarked': 'C'},
        {'Age': 10, 'Survived': '0', 'Embarked': 'Q'},
        {'Age': 15, 'Survived': '0', 'Embarked': 'S'},
    ]
    result = count_deceased_children(data, 18)
    expected = {'C': 1, 'Q': 1, 'S': 1}
    assert result == expected


def test_no_deceased_children():
    data = [
        {'Age': 5, 'Survived': '1', 'Embarked': 'C'},
        {'Age': 10, 'Survived': '1', 'Embarked': 'Q'},
        {'Age': 15, 'Survived': '1', 'Embarked': 'S'},
    ]
    result = count_deceased_children(data, 18)
    expected = {'C': 0, 'Q': 0, 'S': 0}
    assert result == expected


def test_some_deceased_children():
    data = [
        {'Age': 5, 'Survived': '0', 'Embarked': 'C'},
        {'Age': 15, 'Survived': '1', 'Embarked': 'Q'},
        {'Age': 25, 'Survived': '0', 'Embarked': 'S'},
    ]
    result = count_deceased_children(data, 18)
    expected = {'C': 1, 'Q': 0, 'S': 0}
    assert result == expected
