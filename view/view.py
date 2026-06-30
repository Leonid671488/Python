class View:
    @staticmethod
    def menu():
        return int(input("1. Enter\n"
                         "2. Register\n"
                         ">>> "))

    @staticmethod
    def enter():
        name = input("Name: ")
        password = input("Password: ")
        return name, password

    @staticmethod
    def role():
        return int(input("1. User\n"
                         "2. Driver\n"
                         ">>> "))

    @staticmethod
    def register_user():
        name = input("Name: ")
        age = int(input("Age: "))
        phone = input("Phone: ")
        password = input("Password: ")
        return name, age, phone, password

    @staticmethod
    def register_driver():
        name = input("Name: ")
        age = int(input("Age: "))
        phone = input("Phone: ")
        password = input("Password: ")
        car = input("Car: ")
        car_number = input("Car number: ")
        car_class = input("Car class: ")
        return name, age, phone, password, car, car_number, car_class

    @staticmethod
    def mkorder(cursor):
        starting_address = input("Starting address: ")
        ending_address = input("Ending address: ")
        View.show_drivers(cursor)
        driver_id = input("Driver ID: ")
        return starting_address, ending_address, driver_id, cursor

    @staticmethod
    def close_order(cursor):
        View.show_orders(cursor)
        return input("Order ID: "), cursor

    @staticmethod
    def new_password():
        return input("Password: ")

    @staticmethod
    def massage(text):
        print(text)

    @staticmethod
    def show_drivers(cursor):
        cursor.execute(f"select * from drivers where car_class = '{input("Car class: ")}'")
        drivers = cursor.fetchall()
        for driver in drivers:
            print(f"Name: {driver[0]}, Age: {driver[1]}, phone: {driver[2]}, Car: {driver[4]}, Car number: {driver[5]}, Driver ID: {driver[7]}")

    @staticmethod
    def show_orders(cursor):
        cursor.execute("select * from orders where status = 'active'")
        orders = cursor.fetchall()
        for order in orders:
            cursor.execute(f"select * from users where user_id = {order[2]}")
            user = cursor.fetchone()
            print(f"Name: {user[0]}, Age: {user[1]}, Phone: {user[2]}, From: {order[0]}, To: {order[1]}, Order ID: {order[5]}")

    @staticmethod
    def user_menu():
        return int(input("1. Change password\n"
                         "2. Make order\n"
                         "0. Exit\n"
                         ">>> "))

    @staticmethod
    def driver_menu():
        return int(input("1. Change password\n"
                         "2. Close order\n"
                         "3. Show orders\n"
                         "0. Exit\n"
                         ">>> "))

