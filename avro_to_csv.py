from avro.datafile import DataFileReader
from avro.io import DatumReader
import csv
import sys

if len(sys.argv) != 3:
    print("usage: avro_to_csv.py \"avro-file-name.avro\" \"csv-output-name\"")
    sys.exit("Bad usage!")

avro_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

reader = DataFileReader(open(avro_file_name, "r"), DatumReader())

try:
    with open(csv_file_name, 'wb') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        # Write header
        entry = next(reader)
        header = [str(key) for key, value in entry.iteritems()]
        file_writer.writerow(header)

        # Write remaining rows
        for entry in reader:
            row = [str(value) for key, value in entry.iteritems()]
            file_writer.writerow(row)
finally:
    # guaranty that the reader is closed
    reader.close()
