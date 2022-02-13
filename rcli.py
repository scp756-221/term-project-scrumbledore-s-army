
import argparse
import cmd
import re

# import requests

# order_id
# user_id
# amount
# paid

#DEFAULT_AUTH = ''
class Mcli(cmd.Cmd):
    def __init__(self):
        # self.name = args.name
        # self.port = args.port
        cmd.Cmd.__init__(self)
        self.prompt = 'mql: '
        self.intro = """
Command-line interface to music service.
Enter 'help' for command list.
"""
# # 'Tab' character autocompletes commands.

#     def parse_args():
#         argp = argparse.ArgumentParser(
#             'mcli'
#             description='Command line query interface for Restaurant'
#         )
#         argp.add_argument(
#             'name',
#             help="DNS name or IP address of music server"
#             )
#         argp.add_argument(
#             'port',
#             type=int,
#             help="Port number of music server"
#             )
#         return argp.parse_args()

    # def get_url(name, port):
        #return "http://{}:{}/api/v1/music/".format(name, port)
    

    def do_order(self, arg):
       
        # url = get_url(self.name, self.port)
        # args = parse_quoted_strings(arg)
        payload = {
            'OrderDetail': args[0]
        }

        r = requests.post(
            url,
            json=payload,
            headers={'Authorization': DEFAULT_AUTH}
        )
        print(r.json())

#     # def unique_id:

#     # def help:

#     # def get_bill:
    
#     # def pay_bill:


# #foodlist = "fish 2 dog 2 cow 2"
# food= args[0].split()

# quant = []
# foody = []

# print(food)

# for i in range(0,len(food)):
#     if(i%2==1):
#         quant.append(food[i])
#     else:
#         foody.append(food[i])

# print(quant, foody)

#     def do_order(self, arg):
       
#         args = parse_quoted_strings(arg)
#         url = get_url(self.name, self.port)
#         payload = {
#             'OrderDetail': args[0]
#         }

#         r = requests.post(
#             url,
#             json=payload,
#             headers={'Authorization': DEFAULT_AUTH}
#         )
#         print(r.json())



if __name__ == '__main__':
    # args = parse_args()
    Mcli().cmdloop()