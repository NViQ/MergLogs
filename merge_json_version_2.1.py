import json
import sys


def merge_jsonFiles(filename1, filename2, filename3):
    with open(filename1, 'r') as file1, \
            open(filename2, 'r') as file2, \
            open(filename3, 'w+') as output_file:
        try:
            line1 = file1.readline()
            line2 = file2.readline()
            while True:
                if line1 and line2:
                    if json.loads(line1).get('timestamp') <= json.loads(
                            line2).get('timestamp'):
                        output_file.write(line1)
                        line1 = file1.readline()
                    else:
                        output_file.write(line2)
                        line2 = file2.readline()
                elif line1 and not line2:
                    output_file.write(line1)
                    line_1 = file1.readline()
                elif not line1 and line2:
                    output_file.write(line2)
                    line2 = file2.readline()
                elif not line1 and not line2:
                    break
        finally:
            file1.close()
            file2.close()
            output_file.close()




def main():
    if len(sys.argv) < 5:
        return
    if sys.argv[3] != '-o':
        return
    merge_jsonFiles(sys.argv[1], sys.argv[2], sys.argv[4])


if __name__ == '__main__':
    main()
