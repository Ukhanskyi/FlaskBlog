# Вхідний масив
enteredData = [[1, 0, 1, 0, 0, 0, 0, 1, 1],
               [1, 0, 1, 0, 1, 0, 0, 1, 1],  # Уханський
               [1, 0, 1, 0, 0, 0, 1, 1, 1],

               [0, 1, 0, 1, 0, 1, 0, 0, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 0],  # Микола
               [0, 1, 0, 1, 0, 1, 1, 0, 0],

               [0, 0, 1, 0, 0, 1, 0, 1, 0],
               [0, 1, 1, 0, 0, 1, 0, 1, 0],  # Дмитрович
               [0, 0, 1, 0, 1, 1, 0, 1, 0]]

# Масив вагових коефіцієнтів (взяв 2 масиви щоб виконати умову зупину)
# Якщо різниця між ітераціями менша-рівна якомусь числу то стоп

w_old = [[.09, .12, .32, .31, .45, .92, .56, .04, .81, .73],
         [.39, .34, .67, .08, .35, .22, .76, .64, .01, .79],
         [.58, .68, .75, .14, .18, .14, .24, .43, .57, .34]]

w_new = [[.09, .12, .32, .31, .45, .92, .56, .04, .81, .73],
         [.39, .34, .67, .08, .35, .22, .76, .64, .01, .79],
         [.58, .68, .75, .14, .18, .14, .24, .43, .57, .34]]

n = 0.6  # коефіцієнт швидкості навчання
k = 0.5  # коефіцієнт оновлення для коефіцієнта швидкості навчання
stepsCounter = 0  # лічильник кроків
stopValue = 0.0005  # значення зупину
runCycle = True  # Запуск циклу
distanceArr = []  # масив відстаней


# Функція відстані нейронів
def distance(w, s):
    distance = 0
    i = 0
    for a in range(9):
        distance += (w[i] - s[i]) ** 2
        i += 1
    return distance


# Вічний цикл (масксимум 100 кроків, можна і 1000000 поставити)
while runCycle and stepsCounter < 100:
    runCycle = False
    i = 0

    while i < len(enteredData):
        # обчислюєм відстань нейронів
        a1 = distance(w_new[0], enteredData[i])
        a2 = distance(w_new[1], enteredData[i])
        a3 = distance(w_new[2], enteredData[i])
        # шукаєм переможця і міняєм коефіцієнти вагові
        distanceArr.append([a1, a2, a3])  # відстані заношу в масив
        j = 0
        while j < len(enteredData[0]):
            if a1 < a2 and a1 < a3:
                # print("Winner A1")
                w_old[0][j] += n * (enteredData[i][j] - w_old[0][j])
                w_new[0][j] = w_old[0][j] + n * (enteredData[i][j] - w_old[0][j])
            elif a2 < a1 and a2 < a3:
                # print("Winner A2")
                w_old[1][j] += n * (enteredData[i][j] - w_old[1][j])
                w_new[1][j] = w_old[1][j] + n * (enteredData[i][j] - w_old[1][j])
            elif a3 < a1 and a3 < a2:
                # print("Winner A3")
                w_old[2][j] += n * (enteredData[i][j] - w_old[2][j])
                w_new[2][j] = w_old[2][j] + n * (enteredData[i][j] - w_old[2][j])
            j += 1
        i += 1

    n = k * n  # оновлюється коефіцієнт швидкості навчання
    stepsCounter += 1

    '''*********** умова зупину ********************'''
    ''' Якщо різниця між елемантами нового і старого масиву менша за значення
        зупину (в прикладі 0.0005) то зупиняєм цикл, інакше - продовжуєм'''
    i_s = 0
    while i_s < 3:
        j_s = 0
        while j_s < 10:
            if abs(w_new[i_s][j_s] - w_old[i_s][j_s]) >= stopValue:
                runCycle = True
            j_s += 1
        i_s += 1

    '''*******************************************'''
i_print = 0
while i_print < 9:
    print(str(enteredData[i_print]) + "\tКлас: " + str(distanceArr[i_print].index(min(distanceArr[i_print])) + 1))
    #  + str(distanceArr[i_print])
    # Клас - це індекс найменшої відстані ( + 1 добавив щоб не виводило 0, 1, 2 а 1,2,3)
    i_print += 1
print("Кількість кроків: " + str(stepsCounter))

