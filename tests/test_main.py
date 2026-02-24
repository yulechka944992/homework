from unittest.mock import patch

from main import main


def test_main(capsys):
    """Тест с базовыми ответами пользователя"""
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['1', 'EXECUTED', 'нет', 'нет', 'нет']

        main()

    captured = capsys.readouterr()
    assert "Программа: Распечатываю итоговый список транзакций..." in captured.out
    assert "Всего банковских операций в выборке:" in captured.out


def test_main_empty(capsys):
    """Тест на обработку пустой выборки"""
    with patch('builtins.input') as mock_input:
        mock_input.side_effect = ['1', 'PENDING', 'нет', 'да', 'нет']

        main()

    captured = capsys.readouterr()
    assert "Программа: Распечатываю итоговый список транзакций..." in captured.out
    assert "Всего банковских операций в выборке: 0" in captured.out
