import re


def get_word_list(source):
    pattern = r'<(.*?)>'
    matches = re.findall(pattern, source)
    return set(matches)


def get_map_from_set(word_set):
    word_to_value_map = {}
    for word in word_set:
        value = input("Give me a " + word + ":    ")
        word_to_value_map[word] = value
    return word_to_value_map


def get_string_from_source(source):
    file = open(source)
    return file.read()


def print_new_text(old_text, dictionary):
    for word in dictionary:
        old_text = old_text.replace("<" + word + ">", dictionary.get(word))
    print(old_text)


if __name__ == '__main__':
    text = get_string_from_source("source.txt")
    word_map = get_map_from_set(get_word_list(text))
    print_new_text(text, word_map)
