##
# album_recommender.py
# Sam Cooper
# 25/5/21
# Asks the user to enter an album, title, genre and rating
# The user can add, edit, delete and rate an album
# If the user rates an album, recommend another album of the same genre


# Add function


# Edit function


# Delete function


# Display all


# Rate function


# Recommend function


# Menu
def menu(albums):
    """
    Displays options
    """

    # print menu and loop it until user quits
    while True:
        print("""
Welcome to the album rater/recommender
(A)dd an album
(E)dit an album
(D)elete an album
(P)rint all albums
(R)ate an album
(Q)uit""")
        choice = input("Please enter your choice: ").strip().upper()

        if choice == "A":
            pass
        elif choice == "E":
            pass
        elif choice == "D":
           pass
        elif choice == "P":
           pass
        elif choice == "R":
           pass
        elif choice == "Q":
           print("Goodbye!")
           break
        else:
            print("That is not an option")

# Main routine

if __name__ == "__main__":
    #dict. of dict. of albums
    albums = {
        }
    menu(albums)
    
