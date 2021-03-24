from io import BytesIO
import base64
import gzip
import random

def gzip_b64encode(data):
    compressed = BytesIO()
    with gzip.GzipFile(fileobj=compressed, mode='w') as f:
        f.write(data.encode('utf-8'))
    return base64.b64encode(compressed.getvalue()).decode('ascii')


def lambda_handler(event, context):
    with open("index.html") as file:
        response=file.read()

    with open("wordlist.txt") as words:
        wordlist=words.read().splitlines()
    random.shuffle(wordlist)
    wordlist=wordlist[:50]

    response=response.replace("REPLACEME"," ".join(wordlist))
    return {
    'isBase64Encoded': True,
    'statusCode': 200,
    'headers':{
        'Content-Type': 'text/html',
        'Content-Encoding': 'gzip',
        'Access-Control-Allow-Origin': '*'
        },
    'body': gzip_b64encode(response)
    }