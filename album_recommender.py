##
# album_recommender.py
# Sam Cooper
# 25/5/21
# Asks the user to enter an album, title, genre and rating
# The user can add, edit, delete and rate an album
# If the user rates an album, recommend another album of the same genre


# Add function
def add(albums, album_id):
    """
    Adds an album to the albums collection
    asks user for title, artist, genre, rating
    Increments the album_id
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
        except ValueError:
            print("Rating must be between {} to {}".format(MIN_RATING, MAX_RATING))

    # add values to album dict.
    album = {"title":title, "artist":artist, "genre":genre, "rating":rating}

    # add our album to album collection
    albums[album_id] = album

    #increment album_id
    album_id += 1
    
    return albums, album_id

    
# Edit function


# Delete function


# Display all


# Rate function


# Recommend function


# Menu
def menu(albums, album_id):
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
            add(albums, album_id)
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
    albums = {}

    # track the current album ID
    album_id = 0
    menu(albums, album_id)
    
