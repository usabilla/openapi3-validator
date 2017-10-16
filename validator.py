import sys
from os import path, getcwd
from openapi_spec_validator import validate_spec_url


def validate(file_name):
    validate_spec_url('file://' + path.join(getcwd(), file_name))


def help():
    print('usage: ' + path.basename(__file__) + ' <spec>')


def main(argv):
    if (len(argv) != 1):
        print('Invalid usage!')
        help()
        sys.exit(2)

    validate(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])
