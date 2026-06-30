from model.model import *
from view.view import *
from controller.controller import *
import psycopg2

connection = psycopg2.connect(
    host="127.0.0.1",
    user="postgres",
    password="",
    dbname="main"
)

my_cursor = connection.cursor()

def main(conn, cursor):
    try:
        view = View()
        role = None
        user = None

        answer = view.menu()
        if answer == 1:
            role = view.role()
            if role == 1:
                user = User.alternative_init(*view.enter(), cursor)
            elif role == 2:
                user = Driver.alternative_init(*view.enter(), cursor)
            else:
                print("Error")
                main(conn, cursor)
        elif answer == 2:
            role = view.role()
            if role == 1:
                user = User(cursor, *view.register_user())
                user.save_user(conn, cursor)
            elif role == 2:
                user = Driver(cursor, *view.register_driver())
                user.save_driver(conn, cursor)
            else:
                print("Error")
                main(conn, cursor)
        else:
            print("Error")
            main(conn, cursor)

        controller = Controller(user, view)
        while True:
            if role == 1:
                answer = controller.user_menu()
                if answer == 0:
                    break
                elif answer == 1:
                    controller.change_password(conn, cursor)
                elif answer == 2:
                    controller.mkorder(conn, cursor)
                else:
                    print("Error")
            elif role == 2:
                answer = controller.driver_menu()
                if answer == 0:
                    break
                elif answer == 1:
                    controller.change_password(conn, cursor)
                elif answer == 2:
                    controller.close_order(conn, cursor)
                elif answer == 3:
                    controller.show_orders(cursor)
                else:
                    print("Error")
            else:
                print("Error")

    except Exception as e:
        print(e)
        main(conn, cursor)


main(connection, my_cursor)

my_cursor.close()
connection.close()
