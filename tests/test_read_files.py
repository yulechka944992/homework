from unittest.mock import patch, mock_open, MagicMock
import pytest

from src.read_files import read_csv, read_excel


def test_read_csv():
    """Тест преобразования CSV файла в список словарей"""
    test_csv = """amount;currency_name;currency_code
1500.00;Ruble;RUB
2000.00;Euro;EUR"""
    with patch("builtins.open", mock_open(read_data=test_csv)):
        with patch("csv.DictReader") as mock_reader:
            mock_reader.return_value = [
                {"amount": "1500.00", "currency_name": "Ruble", "currency_code": "RUB"},
                {"amount": "2000.00", "currency_name": "Euro", "currency_code": "EUR"},
            ]
            result = read_csv("test.csv")

            assert result == mock_reader.return_value


def test_csv_not_exist():
    """Тест: если CSV файл не существует - возвращает сообщение об ошибке и None"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_csv("not_exist.csv")

        assert result is None
        assert "Файл не найден"


def test_csv_exception():
    """Тест ошибки чтения CSV файла"""
    with patch("builtins.open", side_effect=Exception):
        result = read_csv("not_read.csv")

        assert result is None
        assert "Ошибка при чтении файла: {e}"


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    """Тест преобразования Excel файла в список словарей"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"test": "data"}]
    mock_read_excel.return_value = mock_df

    result = read_excel("test.xlsx")

    assert result == [{"test": "data"}]


def test_read_excel_file_not_found():
    """Тест: если Excel файл не существует возращает None и сообщение об ошибке"""
    file_path = "not_found.xlsx"
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        with patch("builtins.print") as mock_print:
            result = read_excel(file_path)

            assert result is None
            mock_print.assert_called_once()


def test_read_excel_exception():
    """Тест ошибки чтения Excel файла"""
    file_path = "not_read.xlsx"
    with patch("pandas.read_excel", side_effect=Exception):
        with patch("builtins.print") as mock_print:
            result = read_excel(file_path)

            assert result is None
            mock_print.assert_called_once()
