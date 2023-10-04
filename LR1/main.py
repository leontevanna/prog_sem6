from typing import List
from mathstats import MathStats

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
    # запускающая функция
    data = read_data(FILE)
    c = count_invoice(data[:5])
    print(f'Всего инвойсов (invoices): {c}')  # 2
    c = count_invoice(data[:11])
    print(f'Всего инвойсов (invoices): {c}')  # 5
    c = count_invoice(data)
    print(f'Всего инвойсов (invoices): {c}')  # 16522

    data2 = MathStats(FILE2)
    slice_test1 = data2.data[:2]  # первые две строки данных
    slice_test2 = data2.data[::]
    print(len(slice_test2))

    # print(data2.min, data2.max)
    print(data2.get_mean(slice_test2))
    print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)


def read_data(file: str) -> List[dict]:
    # считывание данных и возвращение значений в виде списка из словарей
    import csv
    data = []
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for _r in reader:
            row = _r
            row = {
                'InvoiceNo': _r['InvoiceNo'],
                'InvoiceDate': _r['InvoiceDate'],
                 'StockCode': int(_r['StockCode']),
                 'Quantity': int(_r['Quantity'])
             }
            data.append(row)
    return data


def count_invoice(data: List[dict]) -> int:
    count = 0
    # 1. Создаем список виденных инвойсов (пустой), пробегаемся по
    # data и если в списке нет очередного инвойса, то добавляем его туда
    # в конце считаем сколько элементов в нем есть.
    # 2. Создаем множество и добавляем туда по очереди все встреченные
    # элементы. Поскольку это множество, инвойсы в нем не будут
    # повторяться. В конце считаем сколько элементов.

    # 3. Counter
    from collections import Counter

    # Реализуем получение номер invoices и помещение их в список
    # TO DO: Через генератор списка
    invoices = [_el['InvoiceNo'] for _el in data]
    count = len(Counter(invoices))
    return count


def count_different_values(data: List[dict], key: str) -> int:
  count = 0
  temp = -3
  for _el in data:
    if (temp != _el[key]):
        count += 1
        temp = _el[key]
  return count
  """
    TO DO
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """


def get_total_quantity(data: List[dict], stock_code: int) -> int:
    """
    TO DO
    Возвращает общее количество проданного товара для данного stock_code
    """
    result = 0
#    for _el in data:
#      if _el['StockCode'] == stock_code
#        result = 
    result = sum([_el['Quantity'] for _el in   data if _el['StockCode'] == stock_code])
    return result


if __name__ == "__main__":
    main()
