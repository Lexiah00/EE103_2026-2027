for A in range(11):
    for B in range(11):
        for C in range(11):
            if B == A -2 and C == 2 * A and A + B + C == 10:
                print(
                    f"Alyssa sold: {A} tickets, Ben sold: {B} tickets, and Cindy sold: {C} tickets."
                )