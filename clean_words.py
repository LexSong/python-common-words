import json
import re


def is_valid_word(word):
    priority_list = [
        "None",
        "True",
        "False",
        "Exception",
    ]
    if word in priority_list:
        return True
    if word.endswith("Error"):
        return True

    if len(word) == 1:
        return False
    if re.search('[0-9]', word) is not None:
        return False
    if re.search('[A-Z]', word) is not None:
        return False
    return True


with open("data/word_counts.json") as f:
    word_counts = json.load(f)

word_list = [x for x in word_counts if is_valid_word(x)]
print('|'.join(word_list))
