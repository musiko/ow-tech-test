from decimal import Decimal

import pytest

from app.api.services.credit_calculator_service import (
    LONG_WORD_COST,
    MEDIUM_WORD_COST,
    SHORT_WORD_COST,
    calculate_message_credits,
    count_third_vowels,
    get_word_length_credits,
    get_words,
    is_palindrome,
)


@pytest.mark.parametrize(
    "text, expected",
    [("Hello world", 0), ("Programming is great", 4), ("Oaia aia a ei o iau eu", 6)],
)
def test_count_third_vowels(text, expected):
    assert count_third_vowels(text) == expected


@pytest.mark.parametrize(
    "text, expected, description",
    [
        ("Car", SHORT_WORD_COST, "1-3 characters"),
        ("Length", MEDIUM_WORD_COST, "4-7 characters"),
        ("Alphanumeric", LONG_WORD_COST, "8+ characters"),
    ],
)
def test_word_length_credits(text, expected, description):
    assert get_word_length_credits(text) == expected, description


@pytest.mark.parametrize(
    "text, expected",
    [
        ("racecar", True),
        ("Madam, I'm Adam", True),
        ("A man, a plan, a canal - Panama", True),
        ("Hello world", False),
        ("Madam, I'm Eve", False),
    ],
)
def test_palindrome(text, expected):
    assert is_palindrome(text) == expected


@pytest.mark.parametrize(
    "text, expected, description",
    [
        ("Hello world", ["Hello", "world"], "Simple message"),
        ("Madam, I'm Adam", ["Madam", "I'm", "Adam"], "Message with apostrophes"),
        ("free-for-all", ["free-for-all"], "Message with hyphens"),
    ],
)
def test_get_words(text, expected, description):
    assert get_words(text) == expected, description


@pytest.mark.parametrize(
    "text, expected, description",
    [
        ("", Decimal("1"), "Empty message"),
        ("hi", Decimal("1"), "Short message"),
        ("hello world", Decimal("1"), "Simple message"),
        ("&^% *() &^%)", Decimal("1.6"), "Special characters with no words"),
        ("a" * 101, Decimal("38.5"), "Length penalty + third vowels"),
        ("Madam, I'm Adam", Decimal("2"), "Message with punctuation"),
        ("free-for-all", Decimal("1"), "Message with hyphens"),
        ("The quick brown fox", Decimal("1.45"), "All unique words"),
    ],
)
def test_calculate_message_credits(text, expected, description):
    assert calculate_message_credits(text) == expected, description
