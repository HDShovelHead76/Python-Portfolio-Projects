import pandas as pd
from pathlib import Path

# ---------- Data Loading (Class Variables) ----------
class DataStore:
    HOTELS_FILE = Path("Hotels/hotels.csv")
    CARDS_FILE = Path("CreditCards/cards.csv")
    CARDS_SECURITY_FILE = Path("CreditCards/card_security.csv")

    hotels_df = pd.read_csv(HOTELS_FILE, dtype={"id": str})
    cards = pd.read_csv(CARDS_FILE, dtype=str).to_dict(orient="records")
    cards_security_df = pd.read_csv(CARDS_SECURITY_FILE, dtype=str)

    @classmethod
    def save_hotels(cls):
        cls.hotels_df.to_csv(cls.HOTELS_FILE, index=False)


# ---------- Base Hotel ----------
class Hotel:
    def __init__(self, hotel_id: str):
        self.hotel_id = hotel_id

    @property
    def name(self) -> str:
        return DataStore.hotels_df.loc[DataStore.hotels_df["id"] == self.hotel_id, "name"].squeeze()

    @property
    def available(self) -> bool:
        availability = DataStore.hotels_df.loc[DataStore.hotels_df["id"] == self.hotel_id, "available"].squeeze()
        return availability.lower() == "yes"

    def book(self):
        """Mark hotel as booked."""
        DataStore.hotels_df.loc[DataStore.hotels_df["id"] == self.hotel_id, "available"] = "no"
        DataStore.save_hotels()

    def __str__(self):
        return f"Hotel[{self.hotel_id}] - {self.name} ({'Available' if self.available else 'Not Available'})"


# ---------- Spa Hotel ----------
class SpaHotel(Hotel):
    def book_spa_package(self):
        print(f"Spa package booked for {self.name}!")


# ---------- Reservation ----------
class Reservation:
    def __init__(self, customer_name: str, hotel: Hotel):
        self.customer_name = customer_name.title()
        self.hotel = hotel

    def generate(self) -> str:
        return (
            f"\nThank you for your reservation!\n"
            f"Name: {self.customer_name}\n"
            f"Hotel: {self.hotel.name}\n"
        )

    def __repr__(self):
        return f"<Reservation for {self.customer_name} at {self.hotel.name}>"


# ---------- Spa Ticket ----------
class SpaTicket(Reservation):
    def generate(self) -> str:
        return (
            f"\nThank you, enjoy your Spa Day!\n"
            f"Name: {self.customer_name}\n"
            f"Hotel: {self.hotel.name}\n"
        )


# ---------- Credit Card ----------
class CreditCard:
    def __init__(self, card_number: str):
        self.card_number = card_number

    def validate(self, expiration: str, name_on_card: str, cvc: str) -> bool:
        card_data = {
            "number": self.card_number,
            "expiration": expiration,
            "cvc": cvc,
            "holder": name_on_card
        }
        return card_data in DataStore.cards

    def __repr__(self):
        return f"<CreditCard ending {self.card_number[-4:]}>"


# ---------- Secure Credit Card ----------
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password: str) -> bool:
        matched = DataStore.cards_security_df.loc[
            DataStore.cards_security_df["number"] == self.card_number, "password"
        ]
        if matched.empty:
            print("No matching card number found in security database.")
            return False
        return matched.squeeze() == given_password


# ---------- Application Entry ----------
def main():
    print(DataStore.hotels_df)

    hotel_id = input("Enter the ID of the Hotel: ").strip()
    hotel = SpaHotel(hotel_id)

    if hotel.available:
        credit_card = SecureCreditCard("1234123412341234")

        if credit_card.validate("12/26", "JOHN SMITH", "123"):
            if credit_card.authenticate("mypass"):
                hotel.book()
                name = input("Enter your name: ").strip()
                reservation_ticket = Reservation(name, hotel)
                print(reservation_ticket.generate())

                if input("Would you like to purchase a Spa Package? (yes/no): ").lower() == "yes":
                    hotel.book_spa_package()
                    spa_ticket = SpaTicket(name, hotel)
                    print(spa_ticket.generate())
            else:
                print("Credit card authentication failed.")
        else:
            print("Payment problem, please try again.")
    else:
        print("Hotel is not available.")


if __name__ == "__main__":
    main()
