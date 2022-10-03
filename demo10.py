


import re
import csv
import collections

def log_file_reader(filename):
    with open(filename) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[.+\]'
        ip_list = re.findall(regex, log)
        return ip_list

        log_file = open(filename, "r+")
        for row in log_file:
            print(row)
            regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - - \[.+\]'
            ip_list = re.findall(regex, row)
            print()
            return ip_list
        pass


def count_ip(ip_list):
    return collections.Counter(ip_list)


def write_to_csv(counter):
    with open('liste_ip_date_nombre_de_fois_code_retour.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Liste des IP avec date nombre de fois et code retour']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))


if __name__ == "__main__":
    write_to_csv(count_ip(log_file_reader('acces.log')))
