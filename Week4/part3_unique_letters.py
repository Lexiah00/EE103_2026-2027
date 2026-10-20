s = "abcabc"
unique_letters = ""

for char in s:
    if char not in unique_letters:
        unique_letters += char

print("Unique letters count:", len(unique_letters))