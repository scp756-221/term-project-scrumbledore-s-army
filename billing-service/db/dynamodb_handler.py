import boto3

from decouple import config

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME = config("REGION_NAME")

resource = boto3.resource(
    'dynamodb',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION_NAME,
)

order_table = resource.Table('order')

def get_user_data(user_id):
    response = order_table.get_item(
        Key = {
            'user_id' : user_id
        },
        AttributesToGet=[
            'amount', 'paid'
        ]
    )
    
    return response

def pay_bill(user_id):
    response = order_table.update_item(
        Key = {
            'user_id': user_id
        },
        AttributeUpdates={
            'paid': {
                'Value'  : True,
                'Action' : 'PUT'
            }
        },
        ReturnValues = "UPDATED_NEW" # returns the new updated values
    )

    return response