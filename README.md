# unbrandingdemo

## Prep a Python env

```shell
python3 -m venv venv
source venv/bin/activate
```

## Prep a TypeSpec generation env

```shell
git clone https://github.com/bterlson/openai-in-typespec
```

## Run the emitter

```shell
tsp compile openai-in-typespec/main.tsp
```