def permute_a_palindrome(input):
    input = input.lower()

    impares = 0

    for letra in set(input):
        if input.count(letra) % 2 != 0:
            impares += 1

    return impares <= 1
