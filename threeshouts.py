def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    word=word1+word2+word3
    # Define inner
    def inner():
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return inner()

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))