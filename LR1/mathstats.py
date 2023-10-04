"""
Для вычисления дисперсии и ср. квадр. отклонения использовать 
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление среднего по оффлайн и онлайн тратам
        """

        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = (sums['offline'] / len(data), sums['online'] / len(data))

        return self._mean

    @property
    def max(self):
        # TODO
        return self._max

    @property
    def min(self):
        # TODO
        return self._min

    @property
    def disp(self):
        return self._disp

    # по аналогии — со среднем квадратичным отклонением
    @property
    def sigma_sq(self):
        return self._sigma_sq
