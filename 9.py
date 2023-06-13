import re


def change_cells(row):
    pattern = r"\d+"
    elements = row[0].split(";")

    date = elements[0]
    email = elements[1]
    matches = re.findall(pattern, row[1])
    converted_date = date.replace("/", "-")
    converted_email = email.replace("@", "[at]")
    converted_num = ''.join(matches)
    new_row = [converted_email, converted_num, converted_date]

    return new_row


def main(table):
    result = []

    for row in table:
        if row not in result and None not in row:
            result.append(row)
    for i in range(len(result)):
        result[i] = change_cells(result[i])
    sorted_result = sorted(result, key=lambda x: x[2])

    return sorted_result


mas = [
    ['2002/05/27;georgij25@yandex.ru', '(675) 685-7114'],
    ['2001/12/22;aleksandr22@yahoo.com', '(602) 841-5762'],
]
print(main(mas))
