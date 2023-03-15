import json
import sys


def merge_jsonFiles(filename1, filename2, filename3):
    objects = [filename1, filename2]
    for file in objects:
        with open(file, 'r') as infile:
            for f1 in infile:
                with open(filename3, 'a+') as output_file:
                    i = 0
                    output_file.seek(i, 1)
                    while output_file:
                        line = output_file.readline()
                        if not line:
                            output_file.write(str(json.loads(f1)))
                            output_file.write('\n')
                            break
                        if json.loads(line).get('timestamp') >= json.loads(f1).get('timestamp'):
                            output_file.write(str(json.loads(f1)).replace('\'', '\"'))
                            output_file.write('\n')
                            break
                        i += output_file.tell()

def main():
    if len(sys.argv) < 5:
        return
    if sys.argv[3] != '-o':
        return
    merge_jsonFiles(sys.argv[1], sys.argv[2], sys.argv[4])


if __name__ == '__main__':
    main()
