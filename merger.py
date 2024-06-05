import csv

def process_zones(input_csv, output_csv):
    with open(input_csv, mode='r', newline='', encoding='utf-8') as input_file:
        reader = csv.reader(input_file, delimiter=';')
        header = next(reader)
        rows = list(reader)

    grouped = []
    i = 0

    while i < len(rows):
        current_row = rows[i]
        
        if i + 1 < len(rows):
            next_row = rows[i + 1]

            if current_row[0:2] + current_row[4:] == next_row[0:2] + next_row[4:]:
                begin_first = int(current_row[2])
                end_first = int(current_row[3])
                begin_second = int(next_row[2])
                end_second = int(next_row[3])

                new_begin = end_first + 1
                new_end = begin_second - 1

                if new_begin <= new_end:
                    new_record = [
                        current_row[0],
                        current_row[1],
                        str(new_begin),
                        str(new_end)
                    ] + current_row[4:]

                    grouped.append(new_record)

                i += 1
            else:
                grouped.append(current_row)
                i += 1
        else:
            grouped.append(current_row)
            i += 1

    with open(output_csv, mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file, delimiter=';')
        writer.writerow(header)
        writer.writerows(grouped)

files = [
    ('origin.csv', 'grouped_zones_origin.csv'),
    ('destination.csv', 'grouped_zones_destination.csv')
]

for input_csv, output_csv in files:
    process_zones(input_csv, output_csv)

