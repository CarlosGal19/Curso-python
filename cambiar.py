import csv

with open("Datos/Datos_2023-08-08.csv", 'r', newline='', encoding='utf-8') as input_file, \
     open('Datos_2023-08-08.csv', 'w', newline='', encoding='utf-8') as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames

    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        if row['Vistas'] != 'Vistas':
            row['Vistas'] = int(row['Vistas'])
        writer.writerow(row)
