import argparse
import cmd
import json
from datetime import datetime
from uuid import uuid4

import requests


def parse_args():
    argp = argparse.ArgumentParser(
        'rcli',
        description='Command-line query interface to restaurant service')
    argp.add_argument('name_menu', help="IP address of menu server")
    argp.add_argument('port_menu', type=int, help="Port number of menu server")
    argp.add_argument('name_bill', help="IP address of billing server")
    argp.add_argument('port_bill',
                      type=int,
                      help="Port number of billing server")
    argp.add_argument('name_book', help="IP address of booking server")
    argp.add_argument('port_book',
                      type=int,
                      help="Port number of booking server")

    return argp.parse_args()


def get_url(name, port, endpoint):
    return "http://{}:{}/{}".format(name, port, endpoint)


class Rcli(cmd.Cmd):
    def __init__(self, args):
        cmd.Cmd.__init__(self)
        self.name_bill = args.name_bill
        self.name_menu = args.name_menu
        self.name_book = args.name_book
        self.port_bill = args.port_bill
        self.port_menu = args.port_menu
        self.port_book = args.port_book

        self.user_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(
            uuid4())
        self.booking_id = ""

        self.prompt = 'rql: '
        self.intro = """
Command-line interface to restaurant service.
Enter 'help' for command list.
'Tab' character autocompletes commands.
"""

    def do_menu(self, arg):
        """
        Get the entire menu
        """
        response = requests.get(
            get_url(self.name_menu, self.port_menu, 'getMenuItems'))

        if response.status_code != 200:
            print("Unable to get menu. Please retry in some time.")

        menu_items = response.json()

        print()
        print("######## MENU ########")

        menu_dict = {}

        for item in menu_items["menu_items"]:
            item_name = item["name"]
            item_price = item["price"]
            item_id = item["m_id"]

            item_name_parts = item_name.split("_")
            item_name_parts = [i.capitalize() for i in item_name_parts]
            item_name = ' '.join(item_name_parts)

            item_id = int(item_id)
            sum = item_name + ':' + ' $' + item_price
            menu_dict.update({item_id: sum})

        print()

        dictionary_items = menu_dict.items()
        sorted_items = sorted(dictionary_items)

        for i in range(0, len(sorted_items)):
            print("Item Id:", sorted_items[i][0])
            print(sorted_items[i][1])

            print()

    def do_order(self, arg):
        """
        Placing order
        """
        food = arg.split(";")

        order_list = []
        for item in food:
            order_details = {}
            item = item.strip()
            item_array = item.split(" ")
            order_details['id'] = int(item_array[0])
            order_details['qty'] = int(item_array[1])
            order_list.append(order_details)

        payload = {}
        payload['user_id'] = self.user_id
        payload['order_list'] = order_list
        payload['has_booked'] = self.booking_id != ""

        payload = json.dumps(payload, indent=4)

        response = requests.post(get_url(self.name_menu, self.port_menu,
                                         'takeOrder'),
                                 json=payload)

        if response.status_code == 422:
            print("Incorrect menu items. Please be careful while ordering.")
        elif (response.status_code != 200):
            print("Unable to place order. Please try again!")
        else:
            print("Order placed successfully! Enjoy your meal!!")

    def do_get_cheque(self, arg):
        """
        Get the amount to be paid for your order
        """
        response = requests.get(get_url(self.name_bill, self.port_bill,
                                        'bill'),
                                params={'user_id': self.user_id})

        if response.status_code == 422:
            print(
                "We do not accept charity. Please order some food before paying for it."
            )
        elif response.status_code != 200:
            print("Unable to fetch bill. Please retry in some time.")
        else:
            cheque_details = response.json()

            if (cheque_details['paid'] == False):
                print("Amount to be paid: ${0}".format(
                    cheque_details["amount"]))
            else:
                print(
                    "Though we appreciate your generosity, you have already paid your bill!"
                )

    def do_pay_bill(self, arg):
        """
        Pay the bill for your order
        """
        request_params = {'user_id': self.user_id}

        if self.booking_id != "":
            request_params["booking_id"] = self.booking_id

        response = requests.get(get_url(self.name_bill, self.port_bill, 'pay'),
                                params=request_params)

        if response.status_code == 422:
            print(
                "We do not accept charity. Please order some food in before paying for it."
            )
        elif response.status_code == 409:
            print(
                "Though we appreciate your generosity, you have already paid your bill!"
            )
        elif response.status_code != 200:
            print("Unable to pay bill. Please retry in some time.")

        else:
            print("Thankyou for your payment. Enjoy your day!")

    def do_book_table(self, arg):
        """
        Book the table
        """
        self.booking_id = arg.strip()

        response = requests.get(get_url(self.name_book, self.port_book,
                                        'book'),
                                params={'booking_id': self.booking_id})

        if response.status_code == 422:
            print("Unable to process at the moment. Please re-try later")
        elif (response.status_code != 200):
            print("Unable to book the table. Please try again!")
        else:
            print("Your table is booked! Hope to see you soon!!")
            print("Your Booking ID is:", self.booking_id)

    def do_get_booking(self, arg):
        """
        Get the Booking Information
        """
        book_id = arg.strip()

        response = requests.get(get_url(self.name_book, self.port_book,
                                        'get_booking'),
                                params={'booking_id': book_id})

        if response.status_code == 200:
            self.booking_id = book_id
            print("Welcome to our restaurant!")

        elif response.status_code == 422:
            print(
                "Unable to get your booking. Please try again with the correct booking ID."
            )

        else:
            print("Your request cannot be completed.")

    def do_quit(self, arg):
        """
        Quit the program.
        """
        return True


if __name__ == '__main__':
    args = parse_args()
    Rcli(args).cmdloop()
