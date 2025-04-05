import random


data_file_path = "./data/dictionary.txt"


def get_definitions_for_table():
    definitions = []
    with open(data_file_path, "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[0:]:
            word, definition, translation, source = line.split(";")
            definitions.append([cnt, word, definition, translation])
            cnt += 1
    return definitions


def write_definition(new_word, new_definition, new_translation):
    new_definition_line = f"{new_word};{new_definition};{new_translation};user"
    with open(data_file_path, "r", encoding="utf-8") as f:
        existing_definitions = [l.strip("\n") for l in f.readlines()]
        old_definitions = existing_definitions[0:]
    definitions_sorted = old_definitions + [new_definition_line]
    definitions_sorted.sort()
    new_definitions = definitions_sorted
    with open(data_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_definitions))


class ForGame:

    def __init__(self):
        self.__answer = 'none'

    def get_definition_for_game(self):
        with open(data_file_path, "r", encoding="utf-8") as f:
            file_list = f.readlines()
        size = len(file_list)
        choice = random.randint(0, size - 1)
        word, definition, _, _ = file_list[choice].split(";")
        self.__answer = word
        return word, definition

    def answer_check(self, answer):
        return answer == self.__answer


utility = ForGame()