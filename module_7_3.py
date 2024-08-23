import string


class WordsFinder:
    def __init__(self, *files_names):
        self.files_names = files_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.files_names:
            with open(file_name, encoding='utf-8') as file:
                file_text = file.read().lower()
                for p in string.punctuation:
                    file_text = file_text.replace(p, '')
            all_words[file.name] = file_text.split()
        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                return {name: words.index(word.lower()) + 1}
            else:
                return f'Слово {word} отсутствует в тексте'

    def count(self, word):
        counter = 0
        for name, words in self.get_all_words().items():
            for w in words:
                if word.lower() == w:
                    counter += 1
            return {name: counter}


def main():
    # finder2 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt')
    # print(finder2.get_all_words())
    # print(finder2.find('Решении'))
    # print(finder2.count('text'))

    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())
    print(finder2.find('TEXT'))
    print(finder2.count('teXT'))


if __name__ == '__main__':
    main()
