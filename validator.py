import sys
from os import path, getcwd

from jsonschema.exceptions import RefResolutionError
from openapi_spec_validator import openapi_v3_spec_validator
from openapi_spec_validator.handlers import UrlHandler

def validate(url):
    url = str(url[0])
    counter = 0
    try:
        handler = UrlHandler('file')
        url = 'file://' + path.join(getcwd(), url)
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
            ""
            "Unable to resolve {e.__context__.args[0]} in {e.args[0]}",
            ""
        )
    except BaseException:
        counter += 1
        print_error(counter, '', sys.exc_info()[0], '')
    finally:
        if counter > 0:
            print()
            print(" [FAIL] %d errors found " % counter)
            return 1
        else:
            print(" [PASS] No errors found ")
            
            return 0


def print_error(count, path, message, instance):
    print()
    print("Error #%d in [%s]:" % (count, path or 'unknown'))
    print("    %s" % message)
    print("    %s" % instance)


def help():
    print("usage: " + path.basename(__file__) + " <spec>")


def main(argv):
    if len(argv) == 0:
        print("Invalid usage!")
        help()
        sys.exit(2)

    sys.exit(validate(argv))


if __name__ == "__main__":
    main(sys.argv[1:])
