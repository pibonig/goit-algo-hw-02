from collections import deque


def is_palindrome(s):
    s = s.replace(" ", "").lower()

    d = deque(s)

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False

    return True


if __name__ == "__main__":
    word = "  Madam, in Eden, I’m Adam  "
    result = is_palindrome(word)
    print("The text is a palindrome! 🎉" if result else "The text is not a palindrome 😔")
