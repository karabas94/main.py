"""
Реализовать программу(несколько функций) цензор.
Принимает файл с текстом и список слов.
На выходе:
1) новый файл с тем же текстом, но заданные слова заменены на звездочки,
2) файл stat.txt(формат данных JSON) со статисткой(обновляемый) в виде:
название файла, список слов, сколько раз каждое слово встретилось в тесте.
3)файл stat.csv(формат данных csv) со статисткой(обновляемый) в виде:
название файла, список слов, сколько раз каждое слово встретилось в тесте.
"""
import csv
import json


def censor(filename: str, blacklist: list):
    """This function is censor. Function have file with text and list of string
    with bad words which will be replaced by stars and create censored file"""
    statistic = {}
    for word in blacklist:
        with open(filename, "r") as file:
            text = file.read()
            statistic.update({word: text.count(word)})
            read_text = text.replace(word, "*" * len(word))
        with open(filename, "w") as file:
            file.write(read_text)
        with open("censor_text.txt", "w") as file:
            file.write(read_text)

    def stat_json():
        """This function is updated statistic with format json: name of file, bad words, count bad words in text file"""
        with open("stat.txt", "a") as stat_file_json:
            json.dump({filename: statistic}, stat_file_json)

    stat_json()

    def stat_csv():
        """This function is updated statistic with format csv: name of file, bad words, count bad words in text file"""
        with open("stat.csv", "a", newline="", ) as stat_file_csv:
            wr = csv.writer(stat_file_csv)
            wr.writerow({filename})
            write = csv.DictWriter(stat_file_csv, li)
            write.writeheader()
            write.writerow(statistic)

    stat_csv()


li = ["Russia", "Belarus", "Lukashenko"]
censor("text.txt", li)
