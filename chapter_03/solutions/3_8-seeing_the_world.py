"""
3-8. Seeing the World: 

Think of at least five places in the world you'd like to visit.

    • Store the locations in a list. Make sure the list is not in 
    alphabetical order.

    • Print your list in its original order. Don't worry about printing 
    the list neatly; just print it as a raw Python list.
    
    • Use sorted() to print your list in alphabetical order without 
    modifying the actual list.

    • Show that your list is still in its original order by printing 
    it.
    
    • Use sorted() to print your list in reverse-alphabetical order 
    without changing the order of the original list.
    
    • Show that your list is still in its original order by printing it 
    again.
    
    • Use reverse() to change the order of your list. Print the list to 
    show that its order has changed.
    
    • Use reverse() to change the order of your list again. Print the 
    list to show it's back to its original order.
    
    • Use sort() to change your list so it's stored in alphabetical 
    order. Print the list to show that its order has been changed.
    
    • Use sort() to change your list so it's stored in 
    reverse-alphabetical order. Print the list to show that its order 
    has changed.
"""
# List of places I'd like to visit.
place_to_visit = ["Barcelona", "Rome", "Istambul", "Tokyo", "The Bahamas"]

# Print the list
print(f"Original:\n{place_to_visit}")

# Print the list in alphabetical order without changing the order of 
# the original list.
print(f"\nSorted:\n{sorted(place_to_visit)}")

# Show that the list is still in its original order.
print(f"\nOriginal:\n{place_to_visit}")

# Print the list in reverse-alphabetical order without changing the 
# order of the original list.
print(f"\nSorted in reverse order:\n{sorted(place_to_visit, reverse=True)}")

# Show that the list is still in its original order.
print(f"\nOriginal:\n{place_to_visit}")

# Change the order of your original list.
place_to_visit.sort()
print(f"\nPermanently sorted:\n{place_to_visit}")

# Show that the list has changed its original order.
print(f"\nOriginal:\n{place_to_visit}")