from unittest.mock import patch, Mock

import pytest

from src.external_api import amount_rub


def test_transaction_in_rub():
    """Тест: транзакция уже в рублях"""
    transaction = {"operationAmount": {"amount": "425.61", "currency": {"code": "RUB"}}}
    result = amount_rub(transaction)
    assert result == 425.61


@patch("src.external_api.requests.get")
def test_transaction_in_usd(mock_get):
    """Тест: транзакция успешно конвертируется с помощью API"""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 774.20}
    mock_get.return_value = mock_response
    result = amount_rub(transaction)
    assert result == 774.20


@patch("src.external_api.requests.get")
def test_api_error(mock_get):
    """Тест: API возвращает ошибку, функция возвращает 0.0"""
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    result = amount_rub(transaction)
    assert result == 0.0
