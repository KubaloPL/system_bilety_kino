# system_bilety_kino


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
