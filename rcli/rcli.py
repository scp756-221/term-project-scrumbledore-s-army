import argparse
import cmd
import json
import requests
from datetime import datetime
from uuid import uuid4

def parse_args():
    argp = argparse.ArgumentParser(
        'rcli',
        description='Command-line query interface to restaurant service'
        )
    argp.add_argument(
        'name_menu',
        help="IP address of menu server"
        )
    argp.add_argument(
        'port_menu',
        type=int,
        help="Port number of menu server"
        )
    argp.add_argument(
        'name_bill',
        help="IP address of billing server"
        )
    argp.add_argument(
        'port_bill',
        type=int,
        help="Port number of billing server"
        )

    return argp.parse_args()

def get_url(name, port, endpoint):
    return "http://{}:{}/{}".format(name, port, endpoint)


class Rcli(cmd.Cmd):
    def __init__(self, args):
        cmd.Cmd.__init__(self)
        self.name_bill = args.name_bill
        self.name_menu = args.name_menu
        self.port_bill = args.port_bill
        self.port_name = args.port_menu
        self.user_id = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        
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
            get_url(self.name_menu, self.port_name, 'getMenuItems')
        )

        if response.status_code != 200:
            print("Unable to get menu. Please retry in some time.")
        
        menu_items = response.json()

        print()
        print("######## MENU ########")

        for item in menu_items["menu_items"]:
            item_name = item["name"]
            item_price = item["price"]
            item_id = item["mid"]
            
            item_name_parts = item_name.split("_")
            item_name_parts = [i.capitalize() for i in item_name_parts]
            item_name = ' '.join(item_name_parts)

            print()
            print("Item Id: {0}".format(item_id))
            print("{0}: ${1}".format(item_name, item_price))

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
            item_array  = item.split(" ")
            order_details['id'] = int(item_array[0])
            order_details['qty'] = int(item_array[1])
            order_list.append(order_details)

        payload = {}
        payload['user_id'] = self.user_id
        payload['order_list'] = order_list

        payload = json.dumps(payload, indent = 4) 
        
        response = requests.post(
            get_url(self.name_menu, self.port_name, 'takeOrder'),
            json=payload
        )
        
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
        response = requests.get(
            get_url(self.name_bill, self.port_bill, 'bill'),
            params={'user_id': self.user_id}
        )

        if response.status_code == 422:
            print("We do not accept charity. Please order some food in before paying for it.")  
        
        if response.status_code != 200:
            print("Unable to fetch bill. Please retry in some time.")
        
        cheque_details = response.json()

        if (cheque_details['paid'] == False):
            print("Amount to be paid: ${0}".format(cheque_details["amount"]))
        else:
            print("Though we appreciate your generosity, you have already paid your bill!")

    def do_pay_bill(self, arg):
        """
        Pay the bill for your order
        """

        response = requests.get(
            get_url(self.name_bill, self.port_bill, 'pay'),
            params={'user_id': self.user_id}
        )
        
        if response.status_code == 422:
            print("We do not accept charity. Please order some food in before paying for it.")  
        elif response.status_code == 409:
            print("Though we appreciate your generosity, you have already paid your bill!")  
        elif response.status_code != 200:
            print("Unable to pay bill. Please retry in some time.")
        else:
            print("Thankyou for your payment. Enjoy your day!")
             
    def do_quit(self, arg):
        """
        Quit the program.
        """
        return True
        

if __name__ == '__main__':
    args = parse_args()
    Rcli(args).cmdloop()