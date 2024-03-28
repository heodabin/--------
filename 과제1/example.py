class Reservation:
    def __init__(self, name, contact_number, date, time):
        self.name = name
        self.contact_number = contact_number
        self.date = date
        self.time = time

class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def make_reservation(self, name, contact_number, date, time):
        reservation = Reservation(name, contact_number, date, time)
        self.reservations.append(reservation)
        print("Reservation successfully made!")

    def display_reservations(self):
        print("Reservations:")
        for idx, reservation in enumerate(self.reservations, start=1):
            print(f"{idx}. Name: {reservation.name}, Contact Number: {reservation.contact_number},"
                  f"Date: {reservation.date}, Time: {reservation.time}")

    def delete_reservation(self, index):
        if 0 < index <= len(self.reservations):
            del self.reservations[index - 1]
            print("Reservation successfully deleted!")
        else:
            print("Invalid reservation index.")

def main():
    reservation_system = ReservationSystem()

    while True:
        print("\n1. Make a reservation")
        print("2. View reservations")
        print("3. Delete a reservation")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            contact_number = input("Enter your contact number: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time: ")
            reservation_system.make_reservation(name, contact_number, date, time)

        elif choice == '2':
            reservation_system.display_reservations()

        elif choice == '3':
            index = int(input("Enter the index of the reservation to delete: "))
            reservation_system.delete_reservation(index)

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
