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
Traceback (most recent call last):
  File "/home/lmazuel/git/unbrandingdemo/sample_openai.py", line 25, in <module>
    completion = client.chat_completions.create_chat_completion({
  File "/home/lmazuel/git/unbrandingdemo/openai/openai/operations/_operations.py", line 2629, in create_chat_completion
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