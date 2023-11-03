"""
3-6: More Guests
You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.

Start with your program from Exercise 3-4 or Exercise 3-5. Add a 
print() call to the end of your program, informing people that you 
found a bigger dinner table.

• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list. Print a 
new set of invitation messages, one for each person in your list.
"""

# Invite some people to dinner.
guests = ['Isaac Newtow', 'Albert Eienstein', 'Jordan Peterson']

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"\nSorry, {name} can't make it to dinner.")

# Jack can't make it! Let's invite Gary instead.
del(guests[1])
guests.insert(1, 'Karl Marx')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We got a bigger table, so let's add some more people to the list.
print("\nWe got a bigger table!")
guests.insert(0, 'Richard Stallman')
guests.insert(2, 'Lionel Messi')
guests.append('Aristoteles')

name = guests[0]
print(f"{name}, please come to dinner.")

name = guests[1]
print(f"{name}, please come to dinner.")

name = guests[2]
print(f"{name}, please come to dinner.")

name = guests[3]
print(f"{name}, please come to dinner.")

name = guests[4]
print(f"{name}, please come to dinner.")

name = guests[5]
print(f"{name}, please come to dinner.")