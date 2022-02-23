import boto3

from decouple import config

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME = config("REGION_NAME")

client = boto3.client(
    'dynamodb',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME,
)

resource = boto3.resource(
    'dynamodb',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME,
)

menu_table = resource.Table('menu')

def GetItemFromBook(id=None):
    response=menu_table.scan()
    # response = menu_table.get_item(
    #     Key = {
    #         'id' : "allmykeys"
    #     }
    # )

    return response