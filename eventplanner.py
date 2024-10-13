attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
projector = "no projector" if attendees < 50 else "Projector needed"
stero= "live music" if attendees > 75 else "Aux/Bluetooth"

catering = input("Do you want vegitarian? ")
veggies = "Veggie Delight Caterers" if catering == "yes" else "Gourmet Meals Caterers"

print(venue)
print(stero)
print(projector)
print(veggies)