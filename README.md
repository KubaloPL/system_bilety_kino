# system_bilety_kino
# test

Zadanie:  **System rezerwacji biletów do kina**  
Celem zadania jest stworzenie systemu rezerwacji biletów do kina. Program powinien umożliwiać zarządzanie filmami, rezerwacjami oraz klientami z wykorzystaniem klas i dziedziczenia. W zadaniu należy zaimplementować co najmniej dwie klasy główne oraz klasę dziedziczącą, która rozszerza funkcjonalność jednej z głównych klas.Wymagania:  

1.  **Stwórz klasę** `**Movie**` **(Film):**

-   Klasa powinna przechowywać informacje o tytule filmu, czasie trwania oraz dostępnych godzinach seansów.

-   Metody:

-   `__init__(self, title, duration, showtimes)`: Konstruktor inicjalizujący dane filmu.
-   `add_showtime(self, time)`: Dodaje nową godzinę seansu.
-   `remove_showtime(self, time)`: Usuwa istniejącą godzinę seansu.

-   `display_details(self)`: Wyświetla szczegóły filmu.

1.  **Stwórz klasę** `**Customer**` **(Klient):**

-   Klasa powinna przechowywać dane klienta: imię, nazwisko oraz listę zarezerwowanych biletów.

-   Metody:

-   `__init__(self, first_name, last_name)`: Konstruktor inicjalizujący dane klienta.
-   `add_reservation(self, movie, time)`: Dodaje rezerwację na dany film i godzinę.

-   `display_reservations(self)`: Wyświetla listę rezerwacji klienta.

1.  **Stwórz klasę dziedziczącą** `**VIPCustomer**` **(Klient VIP):**

-   Dziedziczy z klasy  `Customer`  i dodaje funkcjonalność:

-   Zniżki na bilety (np. 20%).

-   Prywatne seanse (rezerwacja całej sali).

-   Dodatkowe metody:

-   `get_discounted_price(self, price)`: Zwraca cenę biletu po zniżce.

-   `book_private_show(self, movie, time)`: Rezerwuje cały seans dla VIP-a.

1.  **Stwórz główną klasę** `**Cinema**` **(Kino):**

-   Zarządza filmami i klientami.

-   Metody:

-   `__init__(self)`: Inicjalizuje listę dostępnych filmów i klientów.
-   `add_movie(self, movie)`: Dodaje nowy film do repertuaru.
-   `add_customer(self, customer)`: Dodaje nowego klienta.

-   `display_movies(self)`: Wyświetla wszystkie filmy w repertuarze.

1.  **Wymagania dodatkowe:**

-   Użyj  **dziedziczenia**, aby klasa  `VIPCustomer`  rozszerzała funkcjonalność klasy  `Customer`.
-   W programie głównym (np. w funkcji  `main`) utwórz co najmniej dwa filmy, jednego zwykłego klienta i jednego klienta VIP.
-   Zademonstruj działanie metod (np. dodawanie rezerwacji, wyświetlanie szczegółów filmu i rezerwacji).

Przykład działania:  

1.  Program wyświetla dostępne filmy w repertuarze kina.
2.  Klient rezerwuje bilet na film, wybierając tytuł i godzinę seansu.
3.  Klient VIP rezerwuje bilet z uwzględnieniem zniżki lub cały prywatny seans.
4.  Program wyświetla szczegóły wszystkich rezerwacji klientów oraz filmy w repertuarze.


```
import os
import datetime

class AppointmentManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    @staticmethod
    def validate_phone_number(phone_number: str) -> bool:
        """Sprawdza czy number telefonu ma 9 cyfr."""
        return len(phone_number) == 9 and phone_number.isdigit()
    
    def check_file_exists(self) -> bool:
        """Sprawdza czy istnieje plik o podanej ścieżce"""
        return os.path.exists(self.file_path)

    def get_appointments_from_file(self) -> list:
        """Wczytuje zapisane wizyty z pliku."""
        if self.check_file_exists():
            with open(self.file_path, 'r') as file:
                return file.readlines()
        return []
    
    def check_availability(self, appointments: list, date: str) -> bool:
        """Sprawdza czy jest mniej niż 8 wiyt na daną datę."""
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Nieprawidłowy format daty. Oczekiwano YYYY-MM-DD")
            return False
        
        return sum(date in appt for appt in appointments) < 8
    
    def save_appointment(self, phone_number: str, date: str, time: str) -> bool:
        """Zapisuje nową wizytę, jeśli numer telefonu i data są poprawne."""
        if not self.validate_phone_number(phone_number):
            print("Nieprawidłowy numer telefonu.")
            return False

        appointments = self.get_appointments_from_file()
        if not self.check_availability(appointments, date):
            print("Brak wolnych terminów na ten dzień.")
            return False

        with open(self.file_path, 'a') as file:
            file.write(f"{phone_number};{date};{time}\n")
        print("Wizyta została napisana.")
        return True
    
    def show_available_hours(self, date: str) -> None:
        """Wyświetla dostępne godziny wizyt na podaną datę."""
        appointments = self.get_appointments_from_file()
        if not self.check_availability(appointments, date):
            print("Brak wolnych terminów na ten dzień.")
            return

        working_hours = [f"{hour}:00" for hour in range(9,17)]
        booked_hours = [appt.split(';')[2].strip() for appt in appointments if date in appt]
        available_hours = [hour for hour in working_hours if hour not in booked_hours]

        if available_hours:
            print("Dostępne godziny:", ", ".join(available_hours))
        else:
            print("Brak wolnych terminów na ten dzień.")

# Przykładowe użyie
file_path = "appointments.txt"
appointment_manager = AppointmentManager(file_path)
date = input("Podaj datę (YYYY-MM-DD): ")
appointment_manager.show_available_hours(date)
```