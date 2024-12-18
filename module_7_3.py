class WordsFinder:
    file_names = []
    def __init__(self, *args):
        self.args = args
        self.file_names.extend(args)

    def get_all_words(self):
        all_words = {}
        punct_list = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for name_file in self.file_names:
            with open(name_file, 'r', encoding= 'utf-8') as file:
                while True:
                    lines = file.readlines()
                    if not lines:
                        break
                    all_words[name_file] = []
                    for low_line in lines:
                        low_line = low_line.lower()
                        for punct in punct_list:
                            low_line = low_line.replace(punct, '')
                        all_words[name_file].extend(low_line.split())
        return all_words

    def find(self, find_word):
        result = {}
        low_find_word = find_word.lower()
        for file_name in self.file_names:
            with open(file_name, encoding= 'utf-8') as file:
                words_counter = 0
                for line in file:
                    words = line.split()
                    for word in words:
                        low_word = word.lower()
                        words_counter += 1
                        if low_find_word == low_word:
                            if file_name not in result:
                                result[file_name] = words_counter
        return result

    def count(self, find_word):
        result = {}
        low_find_word = find_word.lower()
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                word_count = 0
                for line in file:
                    words = line.split()
                    for word in words:
                        low_word = word.lower()
                        if low_find_word == low_word:
                            word_count += 1
                        result[file_name] = word_count
        return result




wf = WordsFinder('text1.txt')

print(wf.get_all_words())
print(wf.find("TexT"))
print(wf.count('tEXt'))