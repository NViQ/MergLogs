import json
import sys


def merge_jsonFiles(filename):
    result = list()
    for f1 in filename:
        with open(f1, 'r') as infile:
            while infile:
                line = infile.readline()
                if not line:
                    break
                result.append(json.loads(line))
    sort_result = sorted(result, key=(lambda x: x['timestamp']))


    with open(sys.argv[4], 'w') as output_file:
        json.dump(sort_result, output_file)


def main():
    if len(sys.argv) < 5:
        return
    if sys.argv[3] != '-o':
        return
    files = [sys.argv[1], sys.argv[2]]
    merge_jsonFiles(files)



if __name__ == '__main__':
    main()
