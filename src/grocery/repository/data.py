import csv

def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    data = read_csv_to_dict(r'C:\Users\Charl\OneDrive\Escritorio\Diseño y Arqui de Software\LayerApp\src\grocery\repository\sample_grocery.csv')
    #for row in data:
    #    print(row)
    return data
