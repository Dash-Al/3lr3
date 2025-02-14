#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Генерирование списка возможных слов из матрицы символов
def find_words(board, dictionary):
    found_words = set()
    rows, cols = len(board), len(board[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    def dfs(x, y, path, visited):
        path += board[x][y]  # Добавляем текущий символ к пути
        if path in dictionary:
            found_words.add(path)  # Если слово найдено, добавляем его в набор
        if len(path) > max_length:
            return
        for dx, dy in directions:  # Проверяем все возможные направления
            new_x, new_y = x + dx, y + dy

            if (0 <= new_x < rows and
                    0 <= new_y < cols and
                    (new_x, new_y) not in visited):
                visited.add((new_x, new_y))
                dfs(new_x, new_y, path, visited)
                visited.remove((new_x, new_y))

    max_length = max(len(word) for word in dictionary)
    for i in range(rows):
        for j in range(cols):
            visited = set()
            visited.add((i, j))
            dfs(i, j, '', visited)

    return found_words
# Исходные данные
board = [
    ['О', 'А', 'Е'],
    ['И', 'Н', 'Т'],
    ['Р', 'С', 'Л']
]
dictionary = ['КОЛ', 'САЛ', 'ТИНА', 'РИС', 'ЛЕС', 'НО', 'ТЛЕН', 'РИН', 'СТО']
# Вызов функции find_words
result = find_words(board, dictionary)
print(result) 
