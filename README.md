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

## Test no azure

```shell
cd openai
grep -ri azure *
```

## Install the package

```shell
python3 -m venv venvruntime
source venvruntime/bin/activate
pip install -e openai
pip list
```

## Run the sample

```shell
export OPENAI_API_KEY=put a key here
python sample_openai.py
```

should give

```shell
----- standard request -----
This is a test.

----- failed request -----
UserAgent was: python-openai/1.0.0b1 Python/3.10.12 (Linux-5.10.102.1-microsoft-standard-WSL2-x86_64-with-glibc2.35)

Traceback (most recent call last):
  File "/home/lmazuel/git/unbrandingdemo/sample_openai.py", line 47, in <module>
    completion = client.create_chat_completion(
  File "/home/lmazuel/git/unbrandingdemo/openai/openai/_operations/_operations.py", line 796, in create_chat_completion
    raise HttpResponseError(response=response, model=error)
corehttp.exceptions.HttpResponseError: Operation returned an invalid status 'Bad Request'
Content: {
    "error": {
        "message": "you must provide a model parameter",
        "type": "invalid_request_error",
        "param": null,
        "code": null
    }
}
```