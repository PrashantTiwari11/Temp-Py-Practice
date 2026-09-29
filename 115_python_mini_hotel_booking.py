# 115_python_mini_hotel_booking.py
# Mini Hotel Booking System - 10 practical features

rooms = {
    101: {"type": "Single", "price": 1500, "booked": False},
    102: {"type": "Double", "price": 2500, "booked": True},
    103: {"type": "Deluxe", "price": 3500, "booked": False},
    104: {"type": "Single", "price": 1500, "booked": False},
}

# 1. Display all rooms
print("1. All rooms:", rooms)

# 2. Count rooms
print("2. Total rooms:", len(rooms))

# 3. Available rooms
available = [number for number, room in rooms.items() if not room["booked"]]
print("3. Available rooms:", available)

# 4. Booked rooms
booked = [number for number, room in rooms.items() if room["booked"]]
print("4. Booked rooms:", booked)

# 5. Find rooms by type
room_type = "Single"
print("5. Single rooms:", [number for number, room in rooms.items() if room["type"] == room_type])

# 6. Find rooms under a budget
budget = 2000
print("6. Rooms under budget:", [number for number, room in rooms.items() if room["price"] <= budget])

# 7. Book an available room
rooms[103]["booked"] = True
print("7. Booked room 103:", rooms[103])

# 8. Cancel a booking
rooms[102]["booked"] = False
print("8. Cancelled room 102:", rooms[102])

# 9. Calculate a 2-night bill
room_number = 101
nights = 2
bill = rooms[room_number]["price"] * nights
print("9. Bill:", bill)

# 10. Hotel summary
available_count = sum(not r["booked"] for r in rooms.values())
booked_count = sum(r["booked"] for r in rooms.values())
print("10. Summary:", {
    "available": available_count,
    "booked": booked_count,
    "occupancy_percent": round(booked_count / len(rooms) * 100, 2)
})
