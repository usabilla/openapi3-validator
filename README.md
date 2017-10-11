# OpenAPI v3 Validator

This is essencially a docker image that runs
https://github.com/p1c2u/openapi-spec-validator and can be plugged into CI
servers or even be used during development.

It's still being improved but it already helps us to ensure that our API specs
are actually following the [OpenAPI
specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md).

## Usage

### CI server

We currently use Circle-CI to validate our pull requests, and their new
configuration format (v2) allows us to use customised docker images to run the
jobs. So we just had to add this workflow job:

```yml
  validate-spec:
    docker:
      - image: usabillabv/openapi3-validator
    steps:
      - checkout
      - run: python /opt/validator.py <path to your file>
```

### Development

We can also use this image locally by running the following command (on the root
folder of your project:

```sh
$ docker run -it --rm -v ${PWD}:/project -w /project usabillabv/openapi3-validator python /opt/validator.py <path to your file>
```

Optionally you can create an alias and just use it, like:

```sh
$ alias openapi3-validate="docker run -it --rm -v ${PWD}:/project -w /project usabillabv/openapi3-validator python /opt/validator.py"
$ openapi3-validate <path to your file>
```

The output is not really friendly but it does the basic stuff (exit code is
correct).
