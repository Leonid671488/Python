class Order:
    def __init__(self, starting_address, ending_address, driver_id, user_id, status="active", order_id="default"):
        self.starting_address = starting_address
        self.ending_address = ending_address
        self.driver_id = driver_id
        self.user_id = user_id
        self.status = status
        self.order_id = order_id

    def save_order(self, connection, cursor):
        cursor.execute(f"insert into orders(starting_address, ending_address, user_id, driver_id, status) values('{self.starting_address}', '{self.ending_address}', {self.user_id}, {self.driver_id}, '{self.status}')")
        connection.commit()


class User:
    def __init__(self, cursor, name, age, phone, password, user_id="default"):
        self.name = name
        self.age = age
        self.phone = phone

        cursor.execute(f"select user_password from users")
        passwords = cursor.fetchall()
        cursor.execute(f"select driver_password from drivers")
        passwords.extend(cursor.fetchall())
        if password not in passwords:
            self.password = password
        else:
            raise Exception("Incorrect password")

        self.user_id = user_id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password

    def change_password(self, new_password, connection, cursor):
        if len(new_password) >= 8:
            cursor.execute(f"update users set user_password = '{new_password}' where user_id = {self.user_id}")
            connection.commit()

    @classmethod
    def alternative_init(cls, name, password, cursor):
        cursor.execute(f"select * from users where user_name = '{name}' and user_password = '{password}'")
        result = cursor.fetchone()
        return cls(cursor, *result)

    def save_user(self, connection, cursor):
        cursor.execute(f"insert into users(user_name, age, phone, user_password) values('{self.name}', {self.age}, '{self.phone}', '{self.password}')")
        connection.commit()

    def mkorder(self, starting_address, ending_address, driver_id, cursor, connection):
        order = Order(starting_address, ending_address, driver_id, self.user_id)
        order.save_order(connection, cursor)

    @staticmethod
    def close_order(order_id, cursor, connection):
        cursor.execute(f"update orders set status = 'not active' where order_id = {order_id}")
        connection.commit()


class Driver(User):
    def __init__(self, cursor, name, age, phone, password, car, car_number, car_class, driver_id="default"):
        super().__init__(cursor, name, age, phone, password, driver_id)
        self.car = car
        self.car_number = car_number
        self.car_class = car_class

    def change_password(self, new_password, connection, cursor):
        if len(new_password) >= 8:
            cursor.execute(f"update drivers set driver_password = '{new_password}' where driver_id = {self.user_id}")
            connection.commit()

    @classmethod
    def alternative_init(cls, name, password, cursor):
        cursor.execute(f"select * from drivers where driver_name = '{name}' and driver_password = '{password}'")
        result = cursor.fetchone()
        return cls(cursor, *result)

    def save_driver(self, connection, cursor):
        cursor.execute(f"insert into drivers(driver_name, age, phone, driver_password, car, car_number, car_class) values('{self.name}', {self.age}, '{self.phone}', '{self.password}', '{self.car}', '{self.car_number}', '{self.car_class}')")
        connection.commit()
