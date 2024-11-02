from decimal import Decimal

# Credit calculation constants
BASE_COST = Decimal("1.0")
CHAR_COST = Decimal("0.05")

SHORT_WORD_COST = Decimal("0.1")
MEDIUM_WORD_COST = Decimal("0.2")
LONG_WORD_COST = Decimal("0.3")

THIRD_VOWEL_COST = Decimal("0.3")
LENGTH_PENALTY = Decimal("5.0")
UNIQUE_WORD_BONUS = Decimal("2.0")
PALINDROME_MULTIPLIER = Decimal("2.0")


def char_count_credits(char_count):
    """Calculate the character count credit of a given text."""
    return Decimal(char_count) * CHAR_COST


def is_third_char_vowel(text, index):
    vowels = set("aeiouAEIOU")
    """Check if the character at the given index is a vowel and is at a third position."""
    return (index + 1) % 3 == 0 and text[index] in vowels


def count_third_vowels(text):
    """Count vowels at third positions"""
    return sum(1 for i in range(len(text)) if is_third_char_vowel(text, i))


def get_word_length_credits(word):
    """Calculate credits based on word length."""
    length = len(word)
    if length <= 3:
        return SHORT_WORD_COST
    elif length <= 7:
        return MEDIUM_WORD_COST
    else:
        return LONG_WORD_COST


def is_palindrome(text):
    """
    Check if text is a palindrome after converting to lowercase
    and removing non-alphanumeric characters.
    """
    if not text:
        return False
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    if len(cleaned) == 0:
        return False
    return cleaned == cleaned[::-1]


def get_words(text):
    """
    Extract words from text. A word is defined as any continual sequence of letters,
    plus apostrophes and hyphens.
    """
    current_word = []
    words = []

    for char in text:
        if char.isalpha() or char in "'-":
            current_word.append(char)
        else:
            if current_word:
                words.append("".join(current_word))
                current_word = []

    # Add the last word if exists
    if current_word:
        words.append("".join(current_word))

    return words


def are_unique_words(words):
    """Check if all words in a list are unique."""
    return len(words) == len(set(words)) and len(words) > 0


def calculate_message_credits(text):
    """
    Calculate the total credits for a message based on the given rules.
    Returns a Decimal object rounded to 2 decimal places.
    """

    # Initialize with base cost
    total_credits = BASE_COST

    char_count = len(text)

    # Character count
    total_credits += char_count_credits(char_count)

    # Get words and calculate word length multipliers
    words = get_words(text)
    word_credits = sum(get_word_length_credits(word) for word in words)
    total_credits += Decimal(str(word_credits))

    # Third vowels
    third_vowels_count = count_third_vowels(text)
    total_credits += Decimal(third_vowels_count) * THIRD_VOWEL_COST

    # Length penalty
    if char_count > 100:
        total_credits += LENGTH_PENALTY

    # Unique word bonus
    if are_unique_words(words):
        total_credits -= UNIQUE_WORD_BONUS

    # Ensure minimum cost of 1 credit
    total_credits = max(BASE_COST, total_credits)

    # Palindrome check (double the cost)
    if is_palindrome(text):
        total_credits *= PALINDROME_MULTIPLIER

    # Round to 2 decimal places
    # return total_credits.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return total_credits
