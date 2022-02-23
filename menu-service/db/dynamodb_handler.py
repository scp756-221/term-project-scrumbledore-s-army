import boto3

from decouple import config

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME = config("REGION_NAME")

resource = boto3.resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
)

menu_table = resource.Table('menu')
order_table = resource.Table('order')


def get_menu():
    response = menu_table.scan()
    response = response["Items"]

    return {"menu_items": response}


def add_order(user_id, price, is_paid):
    response = order_table.put_item(Item={
        'user_id': user_id,
        'amount': price,
        'paid': is_paid
    })

    return response
