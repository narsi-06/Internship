def is_palindrome(s: str) -> bool:
    cleaned = "".join(s.split()).lower()
    
    return cleaned == cleaned[::-1]

word1 = "madam"
word2 = "racecar"
word3 = "hello"

print(f"{word1} → {is_palindrome(word1)}")
print(f"{word2} → {is_palindrome(word2)}")
print(f"{word3} → {is_palindrome(word3)}")
