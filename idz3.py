#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#С помощью алгоритма поиска в глубину находим минимальное расстояние между начальным и конечным пунктами
import itertools
def dfs(start, end, visited, current_distance, min_distance, distance_matrix):
    """Поиск в глубину для нахождения минимального расстояния."""
    if start == end:
        return min(current_distance, min_distance)
    for next_city in range(len(distance_matrix)):
        if not visited[next_city]:
            visited[next_city] = True
            current_distance += distance_matrix[start][next_city]
            min_distance = dfs(next_city, end, visited, current_distance, min_distance, distance_matrix)
            current_distance -= distance_matrix[start][next_city]
            visited[next_city] = False  # Backtrack

    return min_distance
def find_min_distance_dfs(distance_matrix, start, end):
    """Ищем минимальное расстояние между начальным и конечным пунктами."""
    visited = [False] * len(distance_matrix)
    visited[start] = True
    return dfs(start, end, visited, 0, float('inf'), distance_matrix)
# Пример использования
if __name__ == "__main__":
    # Матрица расстояний между городами для 10 узлов
    distance_matrix = [
        [0, 222, 234, 420, 498, 677, 853, 555, 457, 455],
        [222, 0, 59, 545, 732, 456, 17, 109, 983, 833],
        [234, 59, 0, 232, 183, 100, 938, 78, 73, 284],
        [420, 545, 232, 0, 37, 274, 112, 82, 877, 458],
        [498, 732, 183, 37, 0, 883, 755, 560, 555, 101],
        [677, 456, 100, 274, 883, 0, 768, 643, 638, 184],
        [853, 17, 938, 112, 755, 768, 0, 462, 674, 654],
        [555, 109, 78, 82, 560, 643, 462, 0, 212, 666],
        [457, 983, 73, 877, 555, 638, 674, 212, 0, 656],
        [455, 833, 284, 458, 101, 184, 654, 666, 656, 0],
    ]

    start_city = 0  # Начальный пункт
    end_city = 9  # Конечный пункт
    # Поиск с помощью DFS
    min_distance_dfs = find_min_distance_dfs(distance_matrix, start_city, end_city)
    # Решение задачи коммивояжера
    def calculate_total_distance(route, distance_matrix):
        """Вычисление общей дистанции для данного маршрута."""
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += distance_matrix[route[i]][route[i + 1]]
        return total_distance
    print(f"Минимальное расстояние с помощью DFS от пункта {start_city} до {end_city}: {min_distance_dfs}")
