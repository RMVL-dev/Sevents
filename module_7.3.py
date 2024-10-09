import re


class WordsFinder:

    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with (open(file_name, 'r') as file):
                pattern = '[,.=!?;:\n]'
                all_words[file_name] = re.sub(pattern, ' ', file.read().replace(' - ', '')).lower().split()
        return all_words

    def find(self, word):
        dict_to_return = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_to_return[name] = words.index(word.lower()) + 1  #+1 так как нужна позиция
        return dict_to_return

    def count(self, word):
        word_count = 0
        dict_to_return = {}

        for name, words in self.get_all_words().items():
            for string in words:
                if string.lower() == word.lower():
                    word_count += 1
            dict_to_return[name] = word_count
            word_count = 0

        return dict_to_return


'''
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
'''


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))


'''
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
'''

'''
finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))
'''

'''
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
'''