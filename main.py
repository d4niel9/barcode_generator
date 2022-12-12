import barcode
from barcode.writer import ImageWriter



def menu():
    instructions = """
    *******************************************
                    BARCODE GENERATOR
    * Instructions:
    - Enter barcode
    - Enter name image to generate
    *******************************************
    """
    print(instructions)

def bar_code():
    try:
        # Generte bar_code object
        number = input("Number: >>> ")
        name_file = input("Name image barcode: >>> ")
        barcode_format = barcode.get_barcode_class("upc")

        # Save bar_code
        my_barcode = barcode_format(number, writer=ImageWriter())
        my_barcode.save("./output/" + name_file)
    except Exception as err:
        print(err)

def main():
    menu()
    bar_code()


if __name__ == "__main__":
  main()
