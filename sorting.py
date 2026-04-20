import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):

    size = len(numbers)

    for index in range(size - 1):
        min_index = index

        for i in range(index + 1, size):
            if numbers[i] < numbers[min_index]:
                min_index = i

        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

def bubble_sort(numbers):
    size = len(numbers)

    plt.ion()
    plt.show()

    for i in range(size):
        swapped = False

        for j in range(0, size - i - 1):

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)


            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        if not swapped:
            plt.ioff()
            plt.show()
            break


if __name__ == "__main__":
    numbers_A = random_numbers(20)
    print(numbers_A)
    selection_sort(numbers_A)
    print(numbers_A)


    numbers_B = random_numbers(20)
    print(numbers_B)

    plt.ion()
    plt.show()

    bubble_sort(numbers_B)
    print(numbers_B)


