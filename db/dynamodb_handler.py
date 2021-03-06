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
seating_table = resource.Table('seating')


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


def get_user_data(user_id):
    response = order_table.get_item(Key={'user_id': user_id},
                                    AttributesToGet=['amount', 'paid'])

    return response


def pay_bill(user_id):
    response = order_table.update_item(
        Key={'user_id': user_id},
        AttributeUpdates={'paid': {
            'Value': True,
            'Action': 'PUT'
        }},
        ReturnValues="UPDATED_NEW"  # returns the new updated values
    )

    return response


def set_table_availability(table_id):
    response = seating_table.update_item(
        Key={'table_id': table_id},
        AttributeUpdates={
            'available': {
                'Value': True,
                'Action': 'PUT'
            },
            'booking_id': {
                'Value': None,
                'Action': 'PUT'
            }
        },
        ReturnValues="UPDATED_NEW"  # returns the new updated values
    )

    return response


def get_booking_data():
    response = seating_table.scan()

    return response


def book_table(table_id, booking_id=None):
    response = seating_table.update_item(
        Key={'table_id': table_id},
        AttributeUpdates={
            'available': {
                'Value': False,
                'Action': 'PUT'
            },
            'booking_id': {
                'Value': booking_id,
                'Action': 'PUT'
            }
        },
        ReturnValues="UPDATED_NEW"  # returns the new updated values
    )

    return response
