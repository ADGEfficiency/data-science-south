---
title: 'OpenAI Function Calling in Python'
description: 'Why this new feature is a game changer for developers.'
date: '2023-08-15'
tags:
- Algorithms
- Software Engineering
---

**OpenAI function calling is a game changer for developers**.

It allows programmers to have more control over the OpenAI API.

![](/images/openai-functions/hero.png "Prompt: 'calling functions with the open ai api, vibrant, style of dali'. Seed: 42.<br />Created with Stable Diffusion 1.")

**This post explains what function calling is and how to use it in Python**.

The key concepts will be demonstrated with an example of evaluating the quality of text, using a schema generated with Pydantic.

## Year of the LLM

**Large Language Models (LLMs) broke out into the public in 2023**.

A Large Language Model (LLM) is a neural network that predicts the next token in a sequence of natural language.

The attention mechanism combined with a massive scale of data, compute and network parameters, has led to incredible model performance.

Millions of people now use ChatGPT, where users interact with an LLM as a sequence of prompts and responses through a web application.

**It's also possible to use an LLM via an API call** -- a developer can access an LLM via a HTTP request, and can use the data in the response in an application.

Calling the API offers different options and control than the ChatGPT web application.

One option available to developers who use the OpenAI API is function calling.

## Why is Function Calling Useful?

**Function calling allows you to define the schema of the Open AI API response.**

By specifying the schema of the response, a developer can reliably extract data from the API response into a programming language like Python.

Without function calling, developers can attempt to get LLMs returning valid JSON data via prompt engineering, but this is unreliable.

**With function calling, a developer can send their desired schema into the API as a function call**.  The LLM will then return data following that schema.

Instead of hacking together a prompt, OpenAI handle the prompt engineering to follow the provided schema.

Below is a pseudocode example of how function calling works:

```pseudocode
#  schema of the openai api response
schema = {
    "name": str,
    "age": int
}

#  http GET request to openai
#  we include our schema we want as part of the request
response = http.get("openai.com/api", schema=schema)

#  read data from the response into our program
name = response["name"]
age = response["age"]
```

In the example above we:

- define a schema,
- call the OpenAI API with a prompt and schema,
- read the data we get back into our program.

### Function Calling Without Functions

The name function calling is misleading -- the LLM doesn't actually call a function.  Instead the schema is used in the prompt on the OpenAI side.

**This explains how natural language descriptions in your JSON schema are used -- they end up as part of the prompt**.

### Unlikely to be Perfect

As function calling is prompt engineering, it's unlikely that you can ever guarantee that an LLM will generate valid JSON.

This means developers will need to handle the failure cases when the LLM returns data outside of the desired schema.

Practically however, function calling will be valuable for many developers and businesses even with a non-zero error rate.

## Evaluating Text with Function Calling

Now we will develop a Python example of function calling by evaluating the quality of text.

The complete example is at the bottom of this post and on [GitHub](https://github.com/ADGEfficiency/data-science-south-projects/tree/main/blog/openai-functions).

### Creating a JSON Model Schema with Pydantic

At the heart of our function call is the JSON schema we want the LLM response to follow.

**We will use Pydantic to create our schema**.  Pydantic is a Python library for data validation, and provides a way to generate JSON schemas from models with `model_json_schema()`.

**We start by defining a Pydantic model that represents an evaluation of text**:

```python
import pydantic

class Evaluation(pydantic.BaseModel):
    """Assessment of a piece of natural language."""
    grammar_errors: list[str] = pydantic.Field(
        default_factory=list, description="grammatical mistakes"
    )
    spelling_errors: list[str] = pydantic.Field(
        default_factory=list, description="spelling mistakes"
    )
    corrected_text: str = pydantic.Field(
        description="the correct text",
        default="a sentence to evaluate"
    )
```

The types and descriptions for each of the fields will end up both in our schema, and in the prompt used on the OpenAI side.

We can pull out the JSON schema from an initialized Pydantic model using `model_json_schema()`:

```python
evaluation = Evaluation()
schema = evaluation.model_json_schema()
print(schema)
```

```output
{
    'description': 'Assessment of a piece of natural language.',
    'properties': {
        'grammar_errors': {
            'description': 'grammatical mistakes',
            'items':{'type': 'string'},
            'title': 'Grammar Errors',
            'type': 'array'
        },
        'spelling_errors': {
            'description': 'spelling mistakes',
            'items': {'type': 'string'},
            'title': 'Spelling Errors',
            'type': 'array'
        },
        'corrected_text': {
            'default': 'a sentence to evaluate',
            'description': 'the correct text',
            'title':'Corrected Text',
            'type': 'string'
        }
    },
    'title': 'Evaluation',
    'type': 'object'
}
```

### Functions List

To pass this schema into the OpenAI API, we create a list of our functions in Python.  This list will end up as part of our API call:

```python
functions = [
    {
        "name": "evaluate_text",
        "description": "Evaluate text for errors.",
        "parameters": {
            "type": schema["type"],
            "properties": schema["properties"],
        },
        "required": list(evaluation.model_dump().keys()),
    }
]
```

It's important to include all the fields in the `"required"` section of the function call.

### Prompt

**The next thing we need is a prompt** -- this will be the text that we evaluate:

```python
prompt = "Text to evaluate `The cad jumped over mat.`"
```

### Calling the API

**Finally we can call the API using the `openai` Python library**.

This requires that you have an environment variable `OPENAI_API_KEY` set.

We use a `system` message to give the LLM context on the task -- this is in addition to the schema we send in with `functions`.  The prompt is in our first `user` message:

```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[
        {
            "role": "system",
            "content": "You are proof reading text.",
        },
        {
            "role": "user",
            "content": prompt
        },
    ],
    functions=functions,
    temperature=0,
)
```

Using a temperature of `0` makes the LLM as deterministic as possible -- GPU non-determinism and gamma ray bit flipping permitting.

### Extracting the Function Call Response

After receiving the response from the API, we can pull out the evaluation from the response:

```python
import json

choice = response["choices"][0]
evaluation = json.loads(
    choice["message"]["function_call"]["arguments"]
)
print(evaluation)
```

```output
{
    'grammar_errors': ["Missing article 'the' before 'mat'."],
    'spelling_errors': ["'cad' should be 'cat'."],
    'corrected_text': 'The cat jumped over the mat.'
}
```

We can then use our Pydantic model to validate the JSON returned by the API:

```python
validated = Evaluation(**evaluation)
print(validated)
```

```output
Evaluation(
    grammar_errors=["Missing article 'the' before 'mat'."],
    spelling_errors=["'cad' should be 'cat'."],
    corrected_text='The cat jumped over the mat.'
)
```

While not strictly necessary, we can also check that we have no message where a non-function call OpenAI API call would have a message:

```python
assert choice["message"]["content"] is None
```

The great thing about this code is that we can change how we evaluate text by changing a single Pydantic class.

**It's easy for us to change the task we want the LLM to do, and we get validation for free**.

We could extend our evaluation to also check if the text is hard to read, by adding a `hard_to_read_score` field:

```python
import pydantic

class Evaluation(pydantic.BaseModel):
    """Assessment of a piece of natural language."""

    grammar_errors: list[str] = pydantic.Field(
        default_factory=list, description="grammatical mistakes"
    )
    spelling_errors: list[str] = pydantic.Field(
        default_factory=list, description="spelling mistakes"
    )
    corrected_text: str = pydantic.Field(
        description="the correct text", default="a sentence to evaluate"
    )
    hard_to_read_score: float = pydantic.Field(
        0.5, description="how hard the sentence is to read, 0 is hard, 1 is easy"
    )
```


## Full Python Code

The full example of using the OpenAI API and Pydantic for evaluating text is below and on [GitHub](https://github.com/ADGEfficiency/data-science-south-projects/tree/main/blog/openai-functions).

Requirements are:

```text
fn:requirements.txt
pydantic>=2.1.1
openai==0.27.8
```

Example evaluating text:

```python
import json

import openai
import pydantic


class Evaluation(pydantic.BaseModel):
    """Assessment of a piece of natural language."""

    grammar_errors: list[str] = pydantic.Field(
        default_factory=list, description="grammatical mistakes"
    )
    spelling_errors: list[str] = pydantic.Field(
        default_factory=list, description="spelling mistakes"
    )
    corrected_text: str = pydantic.Field(
        description="the correct text", default="a sentence to evaluate"
    )
    hard_to_read_score: float = pydantic.Field(
        0.5, description="how hard the sentence is to read, 0 is hard, 1 is easy"
    )


if __name__ == "__main__":
    #  instance of our `pydantic` model
    evaluation = Evaluation()

    #  get a json schema
    schema = evaluation.model_json_schema()

    #  create a function using our schema
    functions = [
        {
            "name": "evaluate_text",
            "description": "Evaluate text for mistakes, errors and ease of reading.",
            "parameters": {
                "type": schema["type"],
                "properties": schema["properties"],
            },
            "required": list(evaluation.model_dump().keys()),
        }
    ]

    #  text to evaluate
    prompt = "Text to evaluate `The cad jumped over mat.`"
    print(f"{prompt=}")

    #  call the openAI api using the `openai` Python package
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {
                "role": "system",
                "content": "You are proof reading text.",

            },
            {
                "role": "user",
                "content": prompt
            },
        ],

        functions=functions,
        temperature=0,
    )

    #  extract out the first choice from the response
    choice = response["choices"][0]

    #  make a dictionary from the function call response
    evaluation = json.loads(choice["message"]["function_call"]["arguments"])
    print(f"{evaluation=}")

    #  validate the response
    validated = Evaluation(**evaluation)
    print(f"{validated=}")
```

```output
prompt="Text to evaluate `The cad jumped over mat.`"

evaluation={
    'grammar_errors': ["The sentence is missing an article before 'mat'."],
    'spelling_errors': ["'cad' should be 'cat'."],
    'hard_to_read_score': 0.9,
    'corrected_text': 'The cat jumped over the mat.'
}

validated=Evaluation(
    grammar_errors=["The sentence is missing an article before 'mat'."],
    spelling_errors=["'cad' should be 'cat'."],
    hard_to_read_score=0.9,
    corrected_text='The cat jumped over the mat.'
)
```
