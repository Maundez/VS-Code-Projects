# In a file called emojize.py, 
# implement a program that prompts the user for a str in English
# and then outputs the “emojized” version of that str, 
# converting any codes (or aliases) therein to their corresponding emoji.
# https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias

import emoji
emoji_input = input("Input: ")
emoji_output = emoji.emojize(emoji_input, language="alias")

print(f"Output: {emoji_output}")

