# ======== Question 1 =========

flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

for name, item, quantity in flights:
    print(f'Itinerary 1: {name} - From {item} to {quantity}')
    for name, item, quantity in flights[-1:]:
        print(f'Itinerary 2: {name} - From {item} to {quantity}')
    break
# ======== Question 2 ==========

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def add_books(books):
    for book, author in library:
        if books == book:
            print("Sorry, that book is already in the library!")
            return library
    library.append(books)
    return library
print(add_books(("Dune", "Frank Herbert")))

# ======== Question 3 ===========


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

for name, item, quantity in orders:
    print(f'Order 1: {name} - {item}: quantity: {quantity}')
    for name, item, quantity in orders[1:]:
        print(f'Order 2: {name} - {item}: quantity: {quantity}')
    break