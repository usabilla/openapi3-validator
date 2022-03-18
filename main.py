import argparse
import sys
from validator import validate
from lookup import files_lookup
from colors import color

_DEFAULT_OPEN_API_SPEC_NAMES = {"*openapi.yaml", "*openapi.yml"}


def main(argv):
    parser = init_args_parser()

    # show help message in case of no args provided
    if len(argv) == 0:
        parser.print_help(sys.stderr)
        sys.exit(2)

    # legacy mode with only path or url to the single open api spec file
    # supported to not break existing CI/CD pipelines
    elif len(argv) == 1 and not argv[0].startswith("-"):
        sys.exit(validate(argv[0]))

    else:
        args = parser.parse_args()
        print_arguments(args)
        perform_validation(args)


def init_args_parser():
    parser = argparse.ArgumentParser(description="Open API spec validation tool")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file",
                       action='append',
                       help="full path to open api spec file, multiple arguments are supported")
    group.add_argument("-u", "--url",
                       action='append',
                       help="uri to open api spec, multiple arguments are supported")
    group.add_argument("-p", "--lookup-path",
                       help="open api spec files lookup path")
    parser.add_argument("-n", "--spec-name",
                        action='append',
                        help="open api spec file name, multiple arguments are supported. " +
                             "Used in conjunction with --lookup-path option. Default value: " +
                             ','.join(_DEFAULT_OPEN_API_SPEC_NAMES))
    parser.add_argument("-i", "--ignore-missing-spec",
                        help="do not fail processing if spec file is missing. Used in conjunction with --lookup-path option.",
                        action="store_true")
    return parser


def print_arguments(args):
    print(f"Running Open API spec validation tool with the following arguments:")
    for arg, value in sorted(vars(args).items()):
        if value is not None:
            print(f"{arg}: {value}")


def perform_validation(args):

    spec_file_names = _DEFAULT_OPEN_API_SPEC_NAMES
    if args.spec_name is not None:
        spec_file_names = set(args.spec_name)

    spec_file_paths = get_spec_file_paths(args, spec_file_names)

    errors_counter = 0
    for spec_file_path in spec_file_paths:
        print(f"\n Validating open api spec: {spec_file_path}")
        errors_counter += validate(spec_file_path)
    if errors_counter > 0:
        sys.exit(1)


def get_spec_file_paths(args, spec_file_names):
    if args.lookup_path is not None:
        spec_file_paths = files_lookup(args.lookup_path, spec_file_names)
    elif args.file is not None:
        spec_file_paths = args.file
    else:
        spec_file_paths = args.url

    # ignore_missing_spec should be working only if path argument is present
    if len(spec_file_paths) == 0 and not args.ignore_missing_spec and args.lookup_path is not None:
        print(
            color(
                ' [FAIL] open api spec is not found',
                fg='white',
                bg='red',
                style='bold'
            )
        )
        sys.exit(1)

    return spec_file_paths


if __name__ == "__main__":
    main(sys.argv[1:])
