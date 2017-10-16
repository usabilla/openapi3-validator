import sys
from jsonschema.exceptions import RefResolutionError
from colors import color
from os import path, getcwd
from openapi_spec_validator.handlers import UrlHandler
from openapi_spec_validator import openapi_v3_spec_validator


def validate(file_name):
    counter = 0

    try:
        handler = UrlHandler('file')
        url = 'file://' + path.join(getcwd(), file_name)
        spec = handler(url)

        for i in openapi_v3_spec_validator.iter_errors(spec, spec_url=url):
            counter += 1
            print_error(
                counter,
                ':'.join(i.absolute_path),
                i.message,
                i.instance
            )

    except RefResolutionError as e:
        counter += 1
        print_error(
            counter,
            '',
            f'Unable to resolve {e.__context__.args[0]} in {e.args[0]}',
            ''
        )
    except:
        counter += 1
        print_error(counter, '', sys.exc_info()[0], '')
    finally:
        if counter > 0:
            print()
            print(
                color(
                    ' [FAIL] %d errors found ' % counter,
                    fg='white',
                    bg='red',
                    style='bold'
                )
            )
            return 1
        else:
            print(
                color(
                    ' [PASS] No errors found ',
                    fg='white',
                    bg='green',
                    style='bold'
                )
            )
            return 0


def print_error(count, path, message, instance):
    print()
    print(
        color('Error #%d in [%s]:' % (count, path or 'unknown'), style='bold')
    )
    print("    %s" % message)
    print("    %s" % instance)


def help():
    print('usage: ' + path.basename(__file__) + ' <spec>')


def main(argv):
    if len(argv) == 0:
        print('Invalid usage!')
        help()
        sys.exit(2)

    sys.exit(validate(argv[0]))


if __name__ == "__main__":
    main(sys.argv[1:])
