# OpenAPI v3 Validator

This is essentially a docker image that runs
https://github.com/p1c2u/openapi-spec-validator and can be plugged into CI
servers or even be used during development.

It's still being improved, but it already helps us to ensure that our API specs
are actually following the [OpenAPI
specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md).

## Usage

First you need to pull the image from [Docker Hub](https://hub.docker.com):

```sh
docker pull usabillabv/openapi3-validator
```

The validator can be run with the following arguments:
```sh
usage: [-h] (-f FILE | -u URL | -p PATH) [-n SPEC_NAME]

Open API spec validation tool

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  full path to open api spec file, multiple arguments are supported
  -u URL, --url URL     uri to open api spec, multiple arguments are supported
  -p PATH, --path PATH  open api spec files lookup path
  -n SPEC_NAME, --spec-name SPEC_NAME
                        open api spec file name, multiple arguments are supported. Used in conjunction with --path option. Default value: *openapi.yaml, *openapi.yml
  -i, --ignore-missing-spec
                        do not fail processing if spec file is missing. Used in conjunction with --path option.                      
```

Then you can use it to validate specs available on a shared volume.

### Validate spec file(s) by the full path

```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator --file <path to the first file> --file <path to the second file>
```
or
```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator -f <path to the first file> -f <path to the second file>
```

### Lookup and validate spec file(s):

The tool will search for _openapi.yaml_ spec file by default in the provided path tree: 
```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator --path /project
```
or you can provide specific spec file name(s) for lookup with a support of wildcards: 
```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator --path /project --spec-name *-open-api-*.yaml --spec-name other-file.yaml
```
or
```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator -p /project -n *-open-api-*.yaml -n other-file.yaml
```

### Validate spec file via url(s)

```sh
$ docker run -it --rm usabillabv/openapi3-validator --url <first url> --url <second url>
```
or
```sh
$ docker run -it --rm usabillabv/openapi3-validator -u <url>
```

Optionally you can create an alias and just use it, like:

```sh
$ alias openapi3-validate='docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator'
$ openapi3-validate <any available args>
```

## Legacy mode usage

Validate specs available on a shared volume:
```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator <path to your file>
```
Or available via an HTTP(s) endpoint:
```sh
$ docker run -it --rm usabillabv/openapi3-validator <uri>
```