print("Hello, world!")
def longest_substring_without_duplicates(s):
    start = 0
    max_len = 0
    max_substring = ""
    char_to_index = {}

    for i, char in enumerate(s):
        if char in char_to_index and char_to_index[char] >= start:
            start = char_to_index[char] + 1

        char_to_index[char] = i

        if i - start + 1 > max_len:
            max_len = i - start + 1
            max_substring = s[start:i + 1]

    return max_substring, max_len


if __name__ == "__main__":
    input_str = input("input: ")
    substring, length = longest_substring_without_duplicates(input_str)
    print(f"output: {substring} length: {length}")
