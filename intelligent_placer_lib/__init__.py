from .intelligent_placer import placer
import pandas as pd

"""
    Данный пакет представляет собой функцию "placer", в которую пользователь должен передать путь к изображению
    На изображении должен быть многоугольник и предметы
    Функция ответит на вопрос можно ли поместить предметы в многоугольник и выведет результаты на экран
    Так же, если нет необходимости отрисовки изображений на экран, в нее можно передать второй параметр False



    Код ниже используется для демонстрации работы пакета "intelligent placer"
    На вход передается файл "info.xlsx", содержащий информацию о изображениях. Структура файла:
        1. Колонка "name" содержит название изображения в папке в формате ".jpg" (пример: 1.jpg)
        2. Колонка "result" одержит правильный результат в формате 0 (False), 1 (True) (пример: 1)
        3. Колонка "description" содержит описание теста (не является обязательной) (пример: тест из 10 предметов)
    Так же на вход подается путь к изображениям
    Результаты будут выводиться на экране
    Для использования демонстрации импортируйте отсюда функцию "placer_demo" и передайте в нее нужные параметры
    
    from intelligent_placer_lib placer_demo
    placer_demo(path_excel="info.xlsx", path_dataset="images/dataset/")
    
    
    
    
    Автор пакета: Редченко Е.Ю. студент СПБПУ гр. 5030102/90401
    Дата релиза: 14.12.2022
"""

KEY_NAME = "name"
KEY_RESULT = "result"
KEY_DESCRIPTION = "description"


def placer_demo(path_excel: str, path_dataset: str):
    df = pd.read_excel(path_excel)

    successes = []
    fails = []

    count = 0
    for index, row in df.iterrows():
        count += 1
        result = placer(path_dataset + row[KEY_NAME])

        if result == row[KEY_RESULT]:
            successes.append(row[KEY_NAME])
            print(f"TEST {count} passed")
        else:
            fails.append(row[KEY_NAME])
            print(f"TEST {count} NOT passed")

        print(f"filename: {row[KEY_NAME]} \t"
              f"result: {result}\t"
              f"correct result: {True if row[KEY_RESULT] else False}\t\t"
              # f"description: {row[KEY_DESCRIPTION]}")
              "description: " + (row[KEY_DESCRIPTION] if not pd.isnull(row[KEY_DESCRIPTION]) else "-"))

    print(f"\nAll {count} tests were completed!\n"
          f"Success count: {len(successes)}\n"
          f"Fail count: {len(fails)}\n"
          f"Success rate: {len(successes) / count * 100} %\n")
