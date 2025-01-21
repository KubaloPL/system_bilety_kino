import time

class Movie():

    def __init__(self, title:str, duration:int, showtimes:list):
        '''Movie class, duration in seconds, showtimes is a list of strings'''
        self.title = title
        self.duration = duration
        self.showtimes = showtimes

    def add_showtime(self,time: str):
        '''Add showtime, format: HH:MM'''
        self.showtimes.append(time)
    
    def remove_showtime(self,time: int):
        '''Remove showtime from the table, format: HH:MM'''
        if time in self.showtimes:
            self.showtimes.remove(time)

    def display_details(self, prefix: str = ""):
        print(f"{prefix}Tytuł filmu: {self.title}")
        print(f"{prefix}Długość filmu: {time.strftime('%H:%M:%S', time.gmtime(self.duration))}")
        totaltimes = ""
        for times in self.showtimes:
            totaltimes = totaltimes + times + ", "
        totaltimes = totaltimes[:-2]
        print(f"{prefix}Lista godzin seansu: {totaltimes}")


class Customer:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.reservations: list = []

    def add_reservation(self, movie:Movie, time:str):
        if time in movie.showtimes:
            self.reservations.append([movie.title, time])

    def display_reservations(self):
        print(f"Rezerwacje dla: {self.first_name} {self.last_name}:")
        for reservation in self.reservations:
            print(f"    - Seans '{reservation[0]}' o godzinie {reservation[1]}")

class VIPCustomer(Customer):
    def __init__(self, first_name, last_name):
        self.private_reservations: list = []
        super().__init__(first_name, last_name)

    def get_discounted_price(self, price:int):
        return price * 0.8
    
    def book_private_show(self, movie: Movie, time: str):
        self.private_reservations.append([movie.title, time])
    
    def display_private_reservations(self):
        print(f"Prywatne rezerwacje dla VIP'a: {self.first_name} {self.last_name}:")
        for reservation in self.private_reservations:
            print(f"    - Seans '{reservation[0]}' o godzinie {reservation[1]}")


class Cinema:
    def __init__(self):
        self.movies: list[Movie] = []
        self.customers: list[Customer] = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)
    
    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def display_movies(self):
        print("Wszystkie filmy:")
        for movie in self.movies:
            movie.display_details(prefix="    - ")
            print("")

def main():
    cinema = Cinema()

    movie1 = Movie("Test", 6792, ["12:00", "16:00"])
    customer1 = Customer("Obama", "Barack")
    VIPcustomer1 = VIPCustomer("Donald", "Trump")

    cinema.add_movie(movie1)
    cinema.add_customer(customer1)
    cinema.add_customer(VIPcustomer1)

    movie1.display_details()

    customer1.add_reservation(movie1,"12:00")
    customer1.display_reservations()

    VIPcustomer1.book_private_show(movie1, "16:00")
    VIPcustomer1.display_private_reservations()

    cinema.display_movies()


if __name__ == "__main__":
    main()