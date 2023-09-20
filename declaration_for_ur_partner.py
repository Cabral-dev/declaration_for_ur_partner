print("Declaration for my partner")

answer = input("Did you know that i love you? ")

answer_lower = answer.lower()

if answer_lower == "yes":
    x = 1.0
    y = 0.0
elif answer_lower == "no" or answer_lower == "nope":
    x = 0.0
    y = 1.0
else:
    print("Invalid answer. Please, answer with only 'yes' or 'no'.")
    exit()

if x <= y:
    print("Wrong answer")
else:
    print("Of course you know <3. And I love you very much")
