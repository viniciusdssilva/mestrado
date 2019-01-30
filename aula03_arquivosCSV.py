import csv

with open('products.csv') as arq_csv:
    reader = csv.DictReader(arq_csv)
    for linha in reader:
        print(linha['ProductName'], linha['QuantityPerUnit'], linha['UnitPrice'])
