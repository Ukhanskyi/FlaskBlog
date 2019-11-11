#!/usr/bin/env python3


def my_logic_func(x):
    return int((not x[0] and x[1]) or not x[2])


def perceptron(x, w):
    summator = x[0] * w[0] + x[1] * w[1] + x[2] * w[2]
    if summator >= tresshold:
        summator = 1
    else:
        summator = 0
    return summator


dataset = [
    # x0 x1 x2
    [0, 0, 1],  # 0
    [0, 1, 0],  # 1
    [0, 1, 1],  # 1
    [1, 0, 1],  # 0
    [1, 1, 0],  # 1
    [1, 1, 1],  # 0
    # [1, 0, 0],  # 1                not working
    # [0, 0, 0]	# 0
]

weight = [.95, .478689, .5697]
tresshold = 0.5             # Порогове значення
stepsCounter = 0            # Лічильник кроків
n = .08                     # Коефіцієнт швидкості навчання
runCycle = True             # Запуск циклу

while runCycle and stepsCounter < 1000:
    runCycle = False
    i = 0

    while i < len(dataset):
        etalon = my_logic_func(dataset[i])  # Еталон (значення логічної функції
        neuron = perceptron(dataset[i], weight)  # Нейрон (значення перцептрона)

        print("Еталон: " + str(etalon) + "; Нейрон: " + str(neuron) + "; w1: " + str(weight[0]) + "; w2: " +
              str(weight[1]) + "; w3: " + str(weight[2]) + "; x1: " + str(dataset[i][0]) + "; x2: " +
              str(dataset[i][1]) + "; x3: " + str(dataset[i][2]))

        if etalon != neuron:
            ''' Якщо значення не співпадають, то оновлюємо вагові коефіцієни '''
            weight[0] += n * dataset[i][0] * (etalon - neuron)
            weight[1] += n * dataset[i][1] * (etalon - neuron)
            weight[2] += n * dataset[i][2] * (etalon - neuron)
            runCycle = True
        i += 1

        # print("Еталон: " + str(etalon) + "; Нейрон: " + str(neuron) + "; w1: " + str(weight[0]) + "; w2: " +
        #       str(weight[1]) + "; w3: " + str(weight[2]))

        # print("Еталон: " + str(etalon) + "; Нейрон: " + str(neuron))
    stepsCounter += 1
    print("Крок: " + str(stepsCounter) + "\n")

print("Коефіцієнт швидкості навчання: " + str(n))
print("Загальна кількість кроків: " + str(stepsCounter))
