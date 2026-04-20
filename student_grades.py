from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):

        if self.scores[index] > 89:
            return "A"
        elif self.scores[index] > 79:
            return "B"
        elif self.scores[index] > 69:
            return "C"
        elif self.scores[index] > 59:
            return "D"
        elif self.scores[index] > 49:
            return "E"
        else:
            return "F"

    def find(self, key):
        result = []
        for index, score in enumerate(self.scores):
            if score == key:
                result.append(index)

        return result

    def get_sorted(self):
        numbers = self.scores
        size = len(numbers)

        for i in range(size):
            swapped = False

            for j in range(0, size - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    swapped = True

            if not swapped:
                break
        return numbers



if __name__ == "__main__":
    results = StudentsGrades(random_numbers(30, 0, 100))

    for i in range(results.count()):
        print(f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")

    print(f"Plný počet: {results.find(100)}")
    print(f"Seřazeno: {results.get_sorted()}\n")
