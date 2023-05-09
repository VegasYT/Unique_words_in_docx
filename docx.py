import os
import docx2txt

# путь к папке с файлами
folder_path = 'files'

# список файлов в папке
files = os.listdir(folder_path)

# словарь для хранения уникальных слов каждого файла
unique_words = {}


# проходимся по каждому файлу
for file in files:
    # проверяем, что файл имеет расширение .docx
    if file.endswith('.docx'):
        # получаем текст из файла
        text = docx2txt.process(os.path.join(folder_path, file))

        # разбиваем текст на слова
        words = set(text.split())

        # проходимся по каждому слову и добавляем его в словарь
        for word in words:
            if word not in unique_words:
                unique_words[word] = set()
            unique_words[word].add(file)


# проходимся по каждому файлу и выводим уникальные слова
for file in files:
    # проверяем, что файл имеет расширение .docx
    if file.endswith('.docx'):
        # получаем текст из файла
        text = docx2txt.process(os.path.join(folder_path, file))

        # разбиваем текст на слова
        words = set(text.split())

        # проходимся по каждому слову и проверяем, что оно уникально
        unique_words_in_file = []

        for word in words:
            if len(unique_words[word]) == 1 and file in unique_words[word]:
                unique_words_in_file.append(word)

        # выводим уникальные слова для файла
        print(f'Уникальные слова для файла {file}: {unique_words_in_file}')
