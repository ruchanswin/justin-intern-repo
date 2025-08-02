def is_palindrome(word: str) -> bool:
    """Check if the given word is a palindrome."""
    cleaned = word.lower().replace(' ', '')
    return cleaned == cleaned[::-1]


# Example usage and simple test
if __name__ == "__main__":
    test_words = ["level", "deified", "hello", "A man a plan a canal Panama", "Python"]
    for word in test_words:
        print(f"'{word}' is palindrome? {is_palindrome(word)}")
