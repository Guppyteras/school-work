import threading
import time

class TicketBooking:
    def __init__(self, total_seats):
        self.available_seats = total_seats
        self.lock = threading.Lock()

    def book_seat(self, counter_id):
        with self.lock:  # Acquire the lock
            if self.available_seats > 0:
                seat_number = self.available_seats
                self.available_seats -= 1  # Decrement available seats
                print(f"Counter {counter_id} booked seat {seat_number}")
            else:
                print(f"No seats available for Counter {counter_id}")

def main():
    total_seats = 100  # Define max seats
    ticket_booking = TicketBooking(total_seats)  # Instantiate ticket booking instance
    
    # Create a list to hold all the threads
    threads = []
    
    # Create 110 threads simulating 110 counters
    for i in range(1, 111):
        thread = threading.Thread(target=ticket_booking.book_seat, args=(i,))
        threads.append(thread)
        thread.start()  # Start the thread

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()