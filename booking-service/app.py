import argparse
from urllib import response

from flask import Flask, make_response, request
from sqlalchemy import true

import db.dynamodb_handler as dynamodb

app = Flask(__name__)


def parse_args():
    argp = argparse.ArgumentParser('Booking-service')
    argp.add_argument('port_book',
                      type=int,
                      help="Port number of booking server")

    return argp.parse_args()


@app.route('/book', methods=['GET'])
def book_table():
    booking_id = request.args.get('booking_id')
    response = dynamodb.get_booking_data()
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        for table_data in response['Items']:
            if table_data['available']:
                available_table_id = table_data['table_id']
                update_response = dynamodb.book_table(booking_id, available_table_id)
                if (update_response['ResponseMetadata']['HTTPStatusCode'] ==
                        200):
                    return {
                        "booking_id":booking_id
                    }
                else:
                    return make_response("Could not make the booking.", 400)

    return make_response("No table available.", 422)


@app.route('/get_booking', methods=['GET'])
def get_booking():
    booking_id = request.args.get('booking_id')
    if booking_id == None or booking_id == "":
        return make_response('No booking id found!', 422)
    response = dynamodb.get_booking_data()
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        for table_data in response['Items']:
            if table_data['booking_id'] == booking_id:
                return make_response('Success!', 200)

    return make_response('Could not find the booking!', 422)


if __name__ == '__main__':
    args = parse_args()
    app.run(host='0.0.0.0', port=args.port_book, debug=True)