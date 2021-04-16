## FizzBuzz

A web application that implements an “interactive” FizzBuzz game
(https://en.wikipedia.org/wiki/Fizz_buzz), where the appropriate Fizz/Buzz/number is returned as
a response to an http(s) request

Request| Response 2 |
| --- | ------  |
| 4   | 4       |
| 5   | Buzz    |
| 9   | Fizz    |
| 15  | FizzBuzz|
| 5426| 5426    |  


## Getting the code

Clone the repository.

### Installation

You can `python3 -m flask run` or use docker :

```
docker build --tag fizzbuzz .
docker run -it -p 80:5000 --name fizz fizzbuzz
```
### Use

# no UI
```
curl http://127.0.0.1:5000/fizzbuzz/4
```

# browser
Using your browser go to http://127.0.0.1:5000/fizzbuzz/4
