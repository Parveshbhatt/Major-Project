from csv import writer
def writeToCsv(data):
    with open('results.csv', 'a',newline='') as f:
        writer_obj = writer(f)
        writer_obj.writerow(data)
        f.close()

        