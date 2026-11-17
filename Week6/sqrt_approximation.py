from secret_data import secret_number

epsilon = 0.01
guess = secret_number / 2.0
guesses = 0

while abs(guess**2 - secret_number) >= epsilon:
    guess = guess - (guess**2 - secret_number) / (2 * guess)
    guesses += 1

print(
    f"[Newton-Raphson] Sqrt of {secret_number} is ~{guess:.4f} | Guesses: {guesses}"
)