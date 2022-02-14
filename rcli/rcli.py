import cmd
import json
import requests

class Rcli(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
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
        ## Uncomment below 

        # response = requests.get(
        #     "A.B.C.D"
        # )

        # if response.status_code != 200:
        #     print("Unable to get menu. Please retry in some time.")
        
        # menu_items = response.json()

        ## ----------------------------------------------


        #remove this line
        dummy_data = open('./rcli/dummy.json')
        menu_items = json.load(dummy_data)
        # remove above line

        print()
        print("######## MENU ########")

        for item in menu_items["items"]:
            item_name = item["name"]
            item_price = item["price"]
            item_id = item["id"]
            
            item_name_parts = item_name.split("_")
            item_name_parts = [i.capitalize() for i in item_name_parts]
            item_name = ' '.join(item_name_parts)

            print()
            print("Item Id: {0}".format(item_id))
            print("{0}: ${1}".format(item_name, item_price))

        print()
        
    def do_quit(self, arg):
        """
        Quit the program.
        """
        return True
        


if __name__ == '__main__':
    Rcli().cmdloop()