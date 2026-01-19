from unittest.mock import Mock, patch


from utils import load_json


def test_load_json():
    mock_exists = Mock(return_value = True)

    mock_json = Mock()
    mock_json.load.return_value = [{"id": 1}]

    mock_file = Mock()
    mock_open_func = Mock(return_value=mock_file)

    with patch('os.path.exists', mock_exists):
        with patch('builtins.open', mock_open_func):
            with patch('json.load', mock_json.load):
                result = load_json("test.json")

                assert result == [{"id": 1}]
                mock_exists.assert_called_once_with("test.json")
                mock_open_func.assert_called_once_with("test.json", "r", encoding="utf-8")

                print("✅ Тест пройден!")
                return result


if __name__ == "__main__":
    test_load_json()
    print("\n✅ Все тесты пройдены!")

