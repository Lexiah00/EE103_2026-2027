from secret_data import secret_year

guesses = 0
found_year = None

for guess in range(2027):
    guesses += 1
    if guess == secret_year:
        found_year = guess
        break

print(f"[Guess and Check] Secret year: {found_year} | Total guesses: {guesses}")