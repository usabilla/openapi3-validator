# OpenAPI v3 Validator

This is essencially a docker image that runs
https://github.com/p1c2u/openapi-spec-validator and can be plugged into CI
servers or even be used during development.

It's still being improved but it already helps us to ensure that our API specs
are actually following the [OpenAPI
specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md).

## Usage


First you need to pull the image from [Docker Hub](https://hub.docker.com):

```sh
docker pull usabillabv/openapi3-validator
```

Then you can use it to validate specs available on a shared volume:

```sh
$ docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator <path to your file>
```

Or available via an HTTP(s) endpoint:

```sh
$ docker run -it --rm usabillabv/openapi3-validator <uri>
```

Optionally you can create an alias and just use it, like:

```sh
$ alias openapi3-validate="docker run -it --rm -v $(pwd):/project -w /project usabillabv/openapi3-validator"
$ openapi3-validate <path to your file or uri>
```

