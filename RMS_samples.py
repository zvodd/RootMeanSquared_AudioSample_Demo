# DELTA = 1 / 44800 # 44.8khz sample rate

def read_file(csvfile):
    """reads csv file and return content as a list of lists"""
    file = open(csvfile)

    for count, value in enumerate(file.readlines()):
        if count < 6:  # ignores header row
            pass
        else:
            line = value.replace('\n', '').split(',')
            # yield(tuple((float(x) for x in line)))
            if line[0] != "[-inf]" and line[0] != "[inf]":
                yield(float(line[0]))


def main():
    for fname in ["sample-data.csv", "sample-data_dB.csv"]:
        print(fname, ":")
        n = 1
        sqrtotal = 0
        total = 0
        for spl in read_file(fname):
            n += 1
            total += spl
            sqrtotal += spl * 2
        RMS = ((n / 1) * sqrtotal) ** 0.5
        print("total", total)
        print("sqrtotal", sqrtotal)
        print("RMS", RMS)
        print("\n----------\n")


if __name__ == '__main__':
    main()
