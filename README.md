# AWS API Gateway and Lambda Function using Proxy integration.

## Introduction
This is a very simple copy-pastable Python Lambda Function that integrates with API Gateway.

You can read more about the details here:

* [Set up Lambda Proxy Integrations in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)
* [Create an API in AWS API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html)

## The Function

This function allows you easy access to the request's [headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields), [query string parameters](https://en.wikipedia.org/wiki/Query_string) and body.

Where you're prompted to do your magic, you put all your logic.

Once you're ready finish off the response by setting the [response code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) and the body, then return it to API Gateway.

~~~~python
import json

def lambda_handler(event, context):
   # Prepare a response dictionary as required by API Gateway
   response = {
        'isBase64Encoded': False,
        'statusCode': 0,
        'headers': {'Your-custom-header':'custom-header-value'},
        'body': ''
        }
   
   # Access the headers of the request
   requestHeaders = event['headers']
   myHeader = requestHeaders['my-header'] 
   
   # Access the query string parameters
   # for example if you called api.mysite.com/resource?myparam=custom
   queryParams = event['queryStringParameters']
   myParam = queryParams['myparam']
   
   # Access the body of the request into a dictionary
   requestBody = json.loads(event['body'])
   myField = requestBody['my-field']
   
   
   #-------------------
   # Do your magic here
   #-------------------
   
   
   # When ready to send the response, set the HTTP status code
   response['statusCode'] = 200
   
   # Then set a reply body if needed
   # this is always a JSON string
   response['body'] = json.dumps({'message':'All went well'})

   # And you're ready to send the response to API gateway!
   return response
~~~~

## Dependancies
The function has only one dependancy which is [JSON](https://docs.python.org/3/library/json.html). This comes with the Standard Library in Python.

## Python Version

As it is the function is compatible with both Python 2.7 and Python 3.6.

## Why did I do this?

I felt that there were a lot of doubts around the proxy integration and it also took myself a lot of reading and researching to make it work correctly.

I couldn't find a terribly clear example for Python, so here it is.

hopefully it will save some headeaches to a few, but let me know if it can be improved to suit specific needs.
