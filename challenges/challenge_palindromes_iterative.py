def is_palindrome_iterative(word):
    if not word:
        return False
    for index in range(len(word) // 2):
        if word[index] != word[len(word) - 1 - index]:
            return False
    return True
