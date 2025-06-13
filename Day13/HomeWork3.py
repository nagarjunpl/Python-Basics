
# Ticket Booking System

seats = 8

while seats : # automatically checks if seats is not zero
    print(f"Available seats: {seats}")

    print("Book one seat")
    seats = seats - 1
    print(f"Seats left: {seats}")
print("All seats are booked!")

# countdown timer using time module
import time

countdown = 10
print("Countdown starts now!")
while countdown > 0:
    print(countdown)
    time.sleep(0)  # Wait for 1 second
    countdown -= 1
