Usage
=====

Let's start with an example on how to find the diff between two
dictionaries using :func:`.diff` method:

```python
from dictdiffer import diff, patch, swap, revert

first = {
    "title": "hello",
    "fork_count": 20,
    "stargazers": ["/users/20", "/users/30"],
    "settings": {
        "assignees": [100, 101, 201],
    }
}

second = {
    "title": "hellooo",
    "fork_count": 20,
    "stargazers": ["/users/20", "/users/30", "/users/40"],
    "settings": {
        "assignees": [100, 101, 202],
    }
}

result = diff(first, second)

assert list(result) == [
    ('change', ['settings', 'assignees', 2], (201, 202)),
    ('add', 'stargazers', [(2, '/users/40')]),
    ('change', 'title', ('hello', 'hellooo'))]
```

Now we can apply the diff result with :func:`.patch` method:

```python
result = diff(first, second)
patched = patch(result, first)
assert patched == second
```

Also we can swap the diff result with :func:`.swap` method:

```python
result = diff(first, second)
swapped = swap(result)

assert list(swapped) == [
    ('change', ['settings', 'assignees', 2], (202, 201)),
    ('remove', 'stargazers', [(2, '/users/40')]),
    ('change', 'title', ('hellooo', 'hello'))]
``` 

    
