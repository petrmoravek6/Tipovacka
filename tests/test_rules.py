from app.src.rules import Rules


def test_test_csv_correct_file():
    for i in range(1, 6):
        rules = Rules()
        assert rules.test_csv_file('tests/csv/test' + str(i) + '_t.csv') is True


def test_test_csv_wrong_file():
    for i in range(1, 30):
        rules = Rules()
        assert rules.test_csv_file('tests/csv/test' + str(i) + '_f.csv') is False
