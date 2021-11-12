import random
listapaixnidiou=["rock","paper","scissors"]

print(
    """
    Welcome to Rock-Papper-Scissors
    if you win u will be a happy person 😃
    """)
while True:
    print("Ti tha paijeis ?")
    epilogh_xrhsth = input ("Grapse rock,paper or scissors :")
    if epilogh_xrhsth in listapaixnidiou:
        epilogh_xrhsth=random.choice(listapaixnidiou)
        print(
        f"\nErijes '{epilogh_xrhsth}',kai o upologisths erije '{epilogh_xrhsth}'"
    )
    else:
        print(f"\n Egrapses '{epilogh_xrhsth},h opoia den einai swsth OPOTE EXASES")
         
    epanalipsi = input("n\Thes na paijeis kialo? (y/n): ")  
    if epanalipsi.lower() == "n":
        break

    print()

input("\n\nPress the enter key to exit")                
    

