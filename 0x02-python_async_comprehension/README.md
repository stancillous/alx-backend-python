<h2>Python Asynchronous Generators/Asynchronous Comprehensions</h2>

<h5>link ---> https://peps.python.org/pep-0525/ </h5>
<h5>link ---> https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/ </h5>

Async generator coroutine -> an async function with at least one yield keyword
they can only be iterated on using `async for`
e.g

```
async def my_generator():
    ...

res = [number async for number in my_generator()]

```

<h5>Check more from the files in the repo. Or using the links above</h5>