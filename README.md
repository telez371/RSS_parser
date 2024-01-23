# Django Backend / Local Development (for dep introspection and intellisense)

## Install Brew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

eval "$(/opt/homebrew/bin/brew shellenv)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.bashrc

brew install make gcc

```

## Install Requirements

```bash
brew install python@3.12
pip3.12 install -r requirements.dev.txt
```

## Install Pre-Commits

```shell
pre-commit install
```

# Run

## First time

```shell
echo "DJANGO_DEBUG=1" > .env
```


## Default Admin creds

```
admin:admin
```


## Admin interface

```
http://localhost:8000/admin/
```

# Working with deps
##  Build base image
```shell
docker build -t sales_app/base .
```

## Add libs

```shell
docker run -it -v $(pwd):/app -w /app sales_app/base:latest poetry add [name-libs]
```

```shell
docker run -it -v $(pwd):/app -w /app sales_app/base:latest poetry update --lock
```

## Update requirements.txt

```shell
docker run -it -v $(pwd):/app -w /app sales_app/base:latest poetry export --without-hashes -o requirements.txt
```
## Development
```shell
docker run -it -v $(pwd):/app -w /app sales_app/base:latest poetry export --without-hashes --with dev -o requirements.dev.txt
```


## Run server
```shell
docker-compose up --build
```

## Run RSS
```shell
python manage.py fetchrss
```# RSS_parser
