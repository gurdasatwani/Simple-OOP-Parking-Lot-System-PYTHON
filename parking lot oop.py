import datetime, random

val = [[" "] * 6 for i in range(6)]
heading = ["Date", "Day", "From", "To", "Name", "Phone No.", "Adderss", "Car No."]


class parking_lot:
    # Date,Day,No. Of Car
    date = datetime.date.today()
    day = date.strftime("%A")
    money = 0
    no_of_car = 0

    # Register
    def __init__(self, name, phone, address, car_no):
        self.From = None
        self.to = None
        self.name = name
        self.phone = phone
        self.address = address
        self.car_no = car_no
        self.token = None

    # Show Parking Lot
    def show_pl(self):
        for i in range(37):
            run = random.sample(range(6), 2)
            if val[run[0]][run[1]] == " ":
                val[run[0]][run[1]] = "P"
                parking_lot.no_of_car += 1
                parking_lot.money += 100
            else:
                continue
        row = 0
        for i in val:
            row += 1
            print("\t" * 4)
            for x in i:
                print(f"| {x} ", end="")
            print("|", row)
        print("\n  A   B   C   D   E   F")

    # Where To Park Car
    def park_car(self, row, column):
        try:
            column = column.upper()
            dit = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
            column = dit.get(column)
            if val[row - 1][column] == " ":
                val[row - 1][column] = "P"
                self.token = f"{row-1}{column}"
                parking_lot.no_of_car += 1
                self.From = datetime.datetime.now().time().strftime("%H:%M:%S")
                print(f"Your Token No. {self.token}")
            else:
                return print("\nThat Place Is Booked")
        except:
            return print("Invalid Input")

    # Show Person Info
    def get_info(self):
        for i, j in zip(
            heading,
            [
                parking_lot.date,
                parking_lot.day,
                self.From,
                self.to,
                self.name,
                self.phone,
                self.address,
                self.car_no,
            ],
        ):
            print(i, end=f":- {j}\n\n")

    # Remove The Car
    def remove_car(self, token):
        token = list(str(token).zfill(2))
        try:
            if len(token) > 2:
                return print("\nInvalid Token No.")
            if val[int(token[0])][int(token[1])] == "P":
                val[int(token[0])][int(token[1])] = " "
                parking_lot.no_of_car -= 1
                self.to = datetime.datetime.now().time().strftime("%H:%M:%S")
                parking_lot.money += 100
                print("\nTotal Cost 100 Thanks! Come Again..")
            else:
                return print("\nTheir Is No Car")
        except:
            return print("Invalid Input")


pl = parking_lot('john',3332227980,'Homeless','672962')