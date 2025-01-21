import time


class Movie():
    '''Movie class, duration in seconds, showtime format HH:MM'''
    def __init__(self, title:str, duration:int, showtimes:list[str]):
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
        '''Displays title, formatted length and all showtime hours, optional prefix argument'''
        print(f"{prefix}Tytuł filmu: {self.title}")
        print(f"{prefix}Długość filmu: {time.strftime('%H:%M:%S', time.gmtime(self.duration))}")
        totaltimes = ""
        for times in self.showtimes:
            totaltimes = totaltimes + times + ", "
        totaltimes = totaltimes[:-2]
        print(f"{prefix}Lista godzin seansu: {totaltimes}")


class Customer:
    '''Customer class, first and last name as strings'''
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.reservations: list = []

    def add_reservation(self, movie:Movie, time:str):
        '''Adds reservation to a movie at a specific time'''
        if time in movie.showtimes:
            self.reservations.append([movie.title, time])
        else:
            print("BŁĄD: Nie znaleziono takiej godziny na rezerwacje seansu")

    def display_reservations(self):
        '''Displays all reservations of a customer'''
        print(f"Rezerwacje dla: {self.first_name} {self.last_name}:")
        for reservation in self.reservations:
            print(f"    - Seans '{reservation[0]}' o godzinie {reservation[1]}")

class VIPCustomer(Customer):
    '''VIP Customer class, inherited from Customer'''
    def __init__(self, first_name, last_name):
        self.private_reservations: list = []
        super().__init__(first_name, last_name)

    def get_discounted_price(self, price:int):
        '''VIP customers get a discount on ticket prices, this function handles the formula'''
        return price * 0.8
    
    def book_private_show(self, movie: Movie, time: str):
        '''Books an entire movie reserved entirely to the VIP customer at any time'''
        self.private_reservations.append([movie.title, time])
    
    def display_private_reservations(self):
        '''Displays all private reservations of a VIP customer'''
        print(f"Prywatne rezerwacje dla VIP'a: {self.first_name} {self.last_name}:")
        for reservation in self.private_reservations:
            print(f"    - Seans '{reservation[0]}' o godzinie {reservation[1]}")


class Cinema:
    '''Cinema class for storing all movies and customers of a specific cinema'''
    def __init__(self):
        self.movies: list[Movie] = []
        self.customers: list[Customer] = []

    def add_movie(self, movie: Movie):
        '''Adds a movie to a cinema'''
        self.movies.append(movie)
    
    def add_customer(self, customer: Customer):
        '''Adds a customer to a cinema'''
        self.customers.append(customer)

    def display_movies(self):
        '''Displays all movies' details within a cinema'''
        print("Wszystkie filmy:")
        for i,movie in enumerate(self.movies):
            movie.display_details(prefix="    - ")
            if i < len(self.movies) -1:
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