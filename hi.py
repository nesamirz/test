def scramble_string(input_str):
    even_chars = input_str[::2]  # Get every other character starting from index 0
    odd_chars = input_str[1::2]  # Get every other character starting from index 1
    scrambled_str = even_chars + odd_chars  # Concatenate even and odd characters
    return scrambled_str

# Call the function. I'm using the string "Miqdad"
scrambled = scramble_string("Miqdad")

# Print the scrambled string
print(scrambled)2