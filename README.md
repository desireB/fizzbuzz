## FizzBuzz

A web application that implements an “interactive” FizzBuzz game
(https://en.wikipedia.org/wiki/Fizz_buzz), where the appropriate Fizz/Buzz/number is returned as
a response to an http(s) request

## Getting the code

Clone the repository.

### Installation

You can `python3 -m flask run` or use docker :

```
docker build --tag fizzbuzz .
docker run -it -p 80:5000 --name fizz fizzbuzz
```
