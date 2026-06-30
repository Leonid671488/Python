class Controller:
    def __init__(self, user, view):
        self.user = user
        self.view = view

    def mkorder(self,connection, cursor):
        self.user.mkorder(*self.view.mkorder(cursor), connection)
        self.view.massage("Order added")

    def close_order(self, connection, cursor):
        self.user.close_order(*self.view.close_order(cursor), connection)
        self.view.massage("Order completed")

    def change_password(self, connection, cursor):
        self.user.change_password(self.view.new_password(), connection, cursor)
        self.view.massage("Password changed")

    def user_menu(self):
        return self.view.user_menu()

    def driver_menu(self):
        return self.view.driver_menu()

    def show_orders(self, cursor):
        return self.view.show_orders(cursor)
