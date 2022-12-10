import csv    
def import_csv(csvfilename):
    data = []
    row_index = 0
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        for row in reader:
            if row:  # avoid blank lines
                row_index += 1
                data.append(row)
    return data
