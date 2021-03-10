# Maxwell Health / Sun Life Take Home Exercise

## Overview

This exercise is to implement the best possible solution to the exercise below in the time allotted (2 hours max). We're evaluating your ability to take a set of requirements and translate it to working application.


## Exercise

We're big into monitoring at Maxwell Health and we want to know if some of our vendors are up and running! We want you to build a web server that will be display the status of Google and Amazon's home pages every minute.

### Requirements

- In any language (Node, Go, Scala, PHP etc), you want build a web server that implements 3 endpoints

  ```
    http://localhost/v1/amazon-status
    http://localhost/v1/google-status
    http://localhost/v1/all-status
  ```

- The Google and Amazon endpoints, should each make an HTTP request to https://www.google.com and https://www.amazon.com respectively and return JSON as the response body to the client. The response must include the requested URL, status code, request duration in milliseconds, and the current date time (shown here as a timestamp).

```
{
    "url": "https://www.google.com",
    "statusCode": 200,
    "duration": 154,
    "date": 1606636800
}
```
- The all-status route should make HTTP requests to both https://www.google.com and https://www.amazon.com and return JSON as the response body to the client. The response should contain the same data as Google and Amazon routes, but the structure of the response should appear as follows:
```
[
    {
        "url": "https://www.google.com",
        "statusCode": 200,
        "duration": 150,
        "date": 1606636800
    },
    {
        "url": "https://www.amazon.com",
        "statusCode": 200,
        "duration": 273,
        "date": 1606636803
    }
]
```

- Create a UI that can display the results of these http endpoints and fetch new data every minute. We use React but if you prefer another tool that is ok.


- Send us the code. You can send us a zip file, create a github repo, or put it on [glitch](https://www.glitch.com) or [repl.it](https://repl.it)


- **Hold on to your code!** We will use it in a shorter follow up exercise.

## Notes

### Readability

We take care to write code that our teammates can come back to and
understand later. Make your intention clear as you write.

### Architecture

We want to see how you think we should organize the application to meet the business needs. What components do we need? What libraries do we need? What libraries can we omit?

### Build on the shoulders of giants but don't steal

It's perfectly OK to use frameworks and other libraries to get started but the solution should be your own.

### Testing and documentation

We would like to see this well tested and documentated but understand if it's beyond the time constraint.
