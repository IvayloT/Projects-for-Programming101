from datetime import datetime


def count_words(words):
    return {key: words.count(key) for key in words}


def unique_words(words):
    return {key for key in count_words(words)}


def nan_expand(times):
    result = ""
    if times == 0:
        return ""
    for i in range(times):
        result += "not a"
    result += "nan"
    return result


def iterations_of_nan_expand(expanded):
    if nan_expand(expanded.count("Not a")) == expanded:
        return expanded.count("Not a")
    return False


def take_same(items):
    first = items[0]
    n = len(items)
    index = 1
    result = [first]

    while index < n and items[index] == first:
        result.append(items[index])
        index += 1
    return result


def group(numbers):
    result = []

    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)

        items = items[len(current_group):]

    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


def reduce_file_path(path):
    result = []
    parts = [part for part in path.split("/") if part not in [".", ""]]
    while len(parts) != 0:
        part = parts.pop()
    if part == "..":
        if len(parts) != 0:
            parts.pop()
        else:
            result.insert(0, part)
    return "/" + "/".join(result)


def pr(number):
    result = ""
    count = 0
    while number % 3 == 0:
        count += 1
        number /= 3
    result += " ".join(["spam" for i in range(count)])
    if number % 5 == 0:
        result += " ".join(["eggs" if count == 0 else "and eggs"])
    return result


def credit_card(number):
    n = 0
    if len(number) % 2 == 0:
        print("Number card is invalid")
    else:
        print("Number card is valid")
    for i in number[::-1]:
        n = sum(number)
        if n % 10 == 0:
            return True
        else:
            return False


def magic_square(matrix):
    s = []
    for row in matrix:
        s.append(sum(row))

    for i in range(0, len(matrix)):
        s.append(sum([row[i] for row in matrix]))

    s.append(sum([matrix[i][i] for i in range(len(matrix))]))

    i = 0
    result = 0
    for j in range(len(matrix)-1, -1, -1):
        result += matrix[i][j]
        i += 1
    s.append(result)

    return all([s[0] == s[i] for i in range(len(s))])



FRIDAY_INDEX = 4


def friday(start, end):
    count_friday_years = 0
    for year in range(start, end):
        count_fridays_in_year = 0
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            for week in month_calendar:
                if week[FRIDAY_INDEX] != 0:
                    count_fridays_in_year += 1

    if count_fridays_in_year = 53:
        count_friday_years += 1
        return count_friday_years
