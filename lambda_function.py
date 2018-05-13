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
