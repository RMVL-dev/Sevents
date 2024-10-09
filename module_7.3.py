import re


class WordsFinder:

    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with (open(file_name, 'r') as file):
                pattern = '[,.=!?;: \n]'
                all_words[file_name] = re.split(pattern, file.read().replace(' - ', ' '))
        return all_words

    def find(self, word):
        dict_to_return = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_to_return[name] = words.index(word.lower())+1 #+1 так как нужна позиция
        return dict_to_return

    def count(self, word):
        word_count = 0
        max_count = 0
        file_name = ""

        for name, words in self.get_all_words().items():
            for string in words:
                if string.lower() == word.lower():
                    word_count += 1
            if word_count > max_count:
                file_name = name
                max_count = word_count

        return dict([(file_name, max_count)])


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
