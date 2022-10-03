#1 ouvrir un fichier log, lire son contenu et trouver tous les adresses ip
#2 comptabiliser le nombres de requettes
#3 écrire les resultats obtenus dans un fichier csv
    filename = C:\Users\Cefim\PycharmProjects\pythonProject1\venv\log.access.txt
    import re
    import csv
    from collections import counter

    def reader(filename):
        with open(filename) as f:
            log =f.read()

            regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

            ips_list = re.findall(regexp, log)

            return ips_list
    def count(ips_list):
        return counter(ips_list):

    def write_csv(counter):
        with open('output.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            header = ['IP', 'Frequence']

            writer.writerow(header)

            for item in counter:
                writer.writerow((item, counter[item]))


    if _name_==_'_main_':
        write_csv(count(reader('log')))
