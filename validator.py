import pkg_resources
pkg_resources.require("openapi_spec_validator==0.3.1")

import sys
import jsonschema

from sys import argv
from os import path, getcwd
from openapi_spec_validator import validate_spec
from openapi_spec_validator import openapi_v3_spec_validator
from openapi_spec_validator.handlers import UrlHandler

def getspec(url):
        handler = UrlHandler('file')
        url = 'file://' + path.join(getcwd(), url)
        spec = handler(url)
        return spec


def validate(url):
    
    counter = 0
    try:

        spec = getspec(url)

        for i in openapi_v3_spec_validator.iter_errors(spec, spec_url=url):
            counter += 1
            print_error(
                counter,
                ':'.join(i.absolute_path),
                i.message,
                i.instance
            )

    except jsonschema.RefResolutionError as e:
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
    print("Use at least Python 3.5.0")
    print("usage: " + path.basename(__file__) + " <spec>")
    print("-v Python Version")
    print("-a Assume openapi.yaml in ")
    print("Example: python validator.py openapi.yaml")
    print("Example: python validator.py -v")



def main(argv):
    if len(argv) == 0:
        print("Invalid usage!")
        help()
        sys.exit(2)

    sys.exit(validate(argv))

def initValidations():
    if (len(sys.argv) < 2):
        help()
        exit(1)

    if (sys.argv[1] == "-v"):
        print(sys.version_info)
        exit(0)

    if (sys.version_info < (3, 5, 0)):
        print("Minumum version Python 3.5.0")
        exit(0)

    if (sys.argv[1] == "-a"):
        main("openapi.yaml")    
        exit(0)


if __name__ == "__main__":

    #initValidations()

    main("openapi.yaml")
    #main(sys.argv[1])
