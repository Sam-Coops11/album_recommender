##
# album_recommender.py
# Sam Cooper
# 25/5/21
# Asks the user to enter an album, title, genre and rating
# The user can add, edit, delete and rate an album
# If the user rates an album, recommend another album of the same genre


# Add function
def add(albums):
    """
    Adds an album to the albums collection
    asks user for title, artist, genre, rating
    Returns the updated album
    """
    # Add a title, artist and genre which are strings
    title = input("Title of album: ")
    artist = input("Artist: ")
    genre = input("Genre: ")

    # Add a rating between 1 and 5 and force input
    MIN_RATING = 1
    MAX_RATING = 5
    while True:
        try:
            rating = int(input("Rating ({} to {}): ".format(MIN_RATING, MAX_RATING)))
            if rating < MIN_RATING or rating > MAX_RATING:
                print("Rating must be between {} to {}".format(MIN_RATING, MAX_RATING))
            else:
                break
        except:
            print("Rating must be between {} to {}".format(MIN_RATING, MAX_RATING))

    # add values to album dict.
    album = {"title":title, "artist":artist, "genre":genre, "rating":rating}

    # add our album to album collection
    albums.append(album)
    
    return albums

    
# Edit function


# Delete function


# Display all albums
def display_all(albums):
    """
    Prints all albums in collection
    """
    print()
    for album in albums:
        print("Title: ", album["title"])
        print("Artist: ", album["artist"])
        print("Genre: ", album["genre"])
        print("Rating: ", album["rating"])
        print()
# Rate function


# Recommend function


# Menu
def menu(albums):
    """
    Displays options
    """

    # print menu and loop it until user quits
    choice = None
    while choice != "Q":
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
            albums = add(albums)
        elif choice == "E":
            pass
        elif choice == "D":
           pass
        elif choice == "P":
           display_all(albums)
        elif choice == "R":
           pass
        elif choice == "Q":
           print("Goodbye!")
        else:
            print("That is not an option")

# Main routine

if __name__ == "__main__":
    # list of dict. of albums
    albums = []
    # call menu
    menu(albums)
    
