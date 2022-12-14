from intelligent_placer_lib import placer, placer_demo
import pandas as pd

PATH_EXCEL = "info.xlsx"                            # Путь к excel файлу с информацией
PATH_DATASET = "images/dataset/"                    # Путь к папке с изображениями
KEY_NAME = "name"                                   # Колонка в excel файле, отвечающая за название изображения
KEY_RESULT = "result"                               # Колонка в excel файле, отвечающая за правильный результат
KEY_DESCRIPTION = "description"                     # Колонка в excel файле, отвечающая за описание теста


# Для запуска демонстрационного тестирования (код функции "placer_demo" из файла __init__ в intelligent_placer_lib)
def main():
    df = pd.read_excel(PATH_EXCEL)

    successes = []                                  # Названия изображений, прошедших тет
    fails = []                                      # Названия изображений, не прошедших тест

    count = 0                                       # Счетчик тестов
    for index, row in df.iterrows():
        count += 1
        result = placer(PATH_DATASET + row[KEY_NAME], False)

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


# Для запуска одиночного тестирования
def main2():
    result = placer(PATH_DATASET + "1.jpg")
    print(result)


# Для запуска демонстрационной функции
def main3():
    placer_demo(path_excel=PATH_EXCEL, path_dataset=PATH_DATASET)


if __name__ == '__main__':
    main()
