# Jean Tu
# ITP 115, Spring 2017
# Assignment 7: Music Library
# jeantu@usc.edu
"""
We are simulating a Music Library.
The Music Library will be a dictionary <key, value> = <string: artist name, list: albums by that artist>
Where the user is able to view their albums, remove albums, add albums, remove artists
    and randomly generate their new playlist. I had also worked on the Extra Credit.
"""
import MusicLibraryHelper
import random
#--------GLOBAL VARIABLES--------
dictionary = [] #the dictionary is first empty
musicDatabase = "musiclibrary.dat"
playlist = [] # for when they want to create their own playlist

# Input: none
# Return value: none
# Print out the menu options to the user (see sample output)
def displayMenu():
    choice = 0
    while choice != 9:
    # choiceValid = False
    # while choiceValid == False:
        print("\nWelcome to Your Music Library!!")
        print("Options:")
        print("\t1) Display library")
        print("\t2) Display all artists")
        print("\t3) Add an album")
        print("\t4) Delete an album")
        print("\t5) Delete an artist")
        print("\t6) Search library")
        print("\t7) Generate a random playlist")
        print("\t8) Make your own playlist")
        print("\t9) Exit")
        choice = input("> ")
        if choice.isdigit():
            if choice == "1":
                displayLibrary(dictionary)
            elif choice == "2":
                displayArtists(dictionary)
            elif choice == "3":
                addAlbum(dictionary)
            elif choice == "4":
                done = deleteAlbum(dictionary)
                if done == True:
                    print("\nDelete Album Success\n")
                else:
                    print("\nDelete Album Fail.\n")
            elif choice == "5":
                done = deleteArtist(dictionary)
                if done == True:
                    print("\nArtist Deleted Successfully.\n")
                else:
                    print("\nDelete Artist Failed.\n")
            elif choice == "6":
                searchLibrary(dictionary)
            elif choice == "7":
                generateRandomPlaylist(dictionary)
            elif choice == "8":
                generateCustomPlaylist(dictionary)
            elif choice == "9":
                print("Saving your music library...\nGoodbye!\n")

                MusicLibraryHelper.saveLibrary(musicDatabase, dictionary)
                return

        choiceValid = True


# Input: a dictionary representing the music library
# Return value: none
# Print out the entire music library. The user should be able to see all the
#       albums associated with each artist in their library in a nice, readable format (see sample output).
def displayLibrary(musicLibDictionary):
    artists = musicLibDictionary.keys()
    #converting the dictionary items into a list to be able to use indexing
    artists = list(artists)
    #counter = 0
    for artist in artists:
        print("\nArtist:", artist)
        print("Albums:")
        albums = musicLibDictionary[artist]
        for album in albums:
            print("\t-", album)


# Input: a dictionary representing the music library
# Return value: none
# Print out all the artists currently in the user’s music library.
def displayArtists(musicLibDictionary):
    print("\nDisplaying all artists:")
    artists = musicLibDictionary.keys()
    for artist in artists:
        print("-", artist)

# Input: a dictionary representing the music library
# Return value: none
# Ask the user for the name of an artist and the name of the album they would like to add.
# Check if the artist is already in the dictionary, and if so, add the album to  the artist’s existing list of
#   albums. If the artist is not in the dictionary, add a new key (artist) to the dictionary along with the new value (list
#   containing the new album).
# Error checking: the user’s input should not be case sensitive – if they
#   enter "adele" or "ADELE" and the artist "Adele" already exists in their library, this
#   should add the new album to the already existing key. If the user is adding an album that already exists
#   for an artist, do nothing (no duplicate albums). This should also be case insensitive.
def addAlbum(musicLibDictionary):
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    artist = artist.rstrip() #will remove the white space after the word
    album = album.rstrip()
    artist = artist.title() #making them into first letter capital format
    album = album.title()
    #check to see if the artist is already in the dictionary
    artistExists = False
    artists = musicLibDictionary.keys()
    for art in artists:
        print(art, artist)
        if artist == art:
            artistExists = True
    #if the artist exists take their list and add it
    if artistExists == True:
        listOfAlbums = musicLibDictionary[artist]
        #check to see if the album already exists
        albumInAlbums = False
        for singleAlbum in listOfAlbums:
            if album == singleAlbum:
                albumInAlbums = True
            #else continue
        if albumInAlbums == False:# if it doesn't already exist, add it
            musicLibDictionary[artist].append(album)
        else:
            print("The Album already exists ")
    else: #create a new key for that artist
        newList = [album] #creating a new list with just the new album
        musicLibDictionary[artist] = newList

# Input: the dictionary representing the music library
# Return value: a boolean value – True if an album was successfully deleted, or False if the
#   album was not successfully deleted. Ask the user for the name of an artist and the name of the album they
#   would like to remove.
# Check that both the artist and the album are in the dictionary before removing the album, and then return True.
# If the artist or the album are not in the dictionary, do not modify the dictionary and return False.
# Error checking: the album name and artist names should not be case sensitive.
def deleteAlbum(musicLibDictionary):
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    artist = artist.title()
    album  = album.title()
    artists = musicLibDictionary.keys()
    artistFound = False
    albumFound = False
    for art in artists:
        if art == artist: #found the artist, now find the song
            artistFound = True
    if artistFound == True: #the artist exists, check if the song exists
        albums = musicLibDictionary[artist]
        for singleAlbum in albums:
            if singleAlbum == album:
                albumFound = True
    if albumFound == True: # found it, and can remove it
        index = 0
        listOfAlbums = musicLibDictionary[artist]
        for al in listOfAlbums:
            if al == album:
                del listOfAlbums[index]
            else:
                index += 1
        musicLibDictionary[artist] = listOfAlbums #assigning the new list
        return True
    return False #will get to this if the artist or album doesn't exist

# Input: the dictionary representing the music library
# Return value: a boolean value – True if an artist was successfully deleted, or False if the artist
#   was not successfully deleted. Ask the user for the name of an artist. Check that the artist is in the
#   dictionary before deleting the artist. Return True if the artist was deleted, or False if the artist
#   was not found in the music library.
# Error checking: the artist’s name should not be case sensitive.
def deleteArtist(musicLibDictionary):
    artist = input("Enter artist to delete: ")
    artist = artist.title() #making sure that it's in the same format at the database
    artistList = musicLibDictionary.keys()
    if artist in artistList:
        musicLibDictionary.pop(artist) #removing the artist from the list
        return True
    return False #if the artist doesn't exist


# Input: the dictionary representing the music library
# Return value: none
# Ask the user for a search term (note that this search term could be an artist or an album). Search through
#   all of the artists and print out the names of any artists containing the search term. Search through all
#   of the albums in the dictionary and print out any album names containing the search term. Note that your
#   search should not be case sensitive. In other words, searching for "ADELE" or "adele" should still return
#   you the artist "Adele"
def searchLibrary(musicLibDictionary):
    term = input("\nPlease enter a search term: ")
    term = term.title()
    artists = musicLibDictionary.keys()
    artistHits = False
    print("Artists containing \'"+term+"\': ")
    for artist in artists:
        if term in artist:
            print("-", artist)
            artistHits = True
    if artistHits == False:
        print("\tNo Results")

    albumHits = False
    albums = musicLibDictionary.values()
    print("Albums containing \'"+ term + "\': ")
    for album in albums:
        if len(album) > 1: # if there is more than 1 item in the list
            for single in album:
                if term in single:
                    print("-", single)
                    albumHits = True
    if albumHits == False:
        print("\tNo Results")


# Input: the dictionary representing the music library
# Return value: none
# Generate a random playlist for the user by randomly selecting one
#   album from every artist in the library. Print the library out to the user in
#   a nice format.
def generateRandomPlaylist(musicLibDictionary):
    artists = musicLibDictionary.keys()
    list = [] # list to store the different artists with their albums
    for artist in artists:
        albums = musicLibDictionary[artist]
        if len(albums) > 1: # if there is more than 1 album add them all
            counter = 0
            while counter <= len(albums)-1:
                list.append(albums[counter] + " by " + artist)
                counter += 1
        else:
            counter = 0
            list.append(albums[counter] + " by " + artist)
    copyList = list
    print("Here is your random playlist: ")
    while len(list) >= 1:
        choosen = random.choice(copyList)
        print("-", choosen)
        copyList.remove(choosen) #the list will continue to grow smaller until it is 0

# input the dictionary
# Return value = none
# allow the user to generate their own play list by selecting the artist, then album
# after they have selected one, ask the user if they would like to add another
def generateCustomPlaylist(musicLibDictionary):
    artists = musicLibDictionary.keys()
    global playlist
    addMore = True
    while addMore == True: #while the user wants to add more songs
        printPlaylist(playlist)
        art = selectArtists(artists)
        album = selectedAlbum(art)
        entry = album + " by " + art
        if entry in playlist:
            print("That albums is already in your playlist, so it won't be added")
        else:
            playlist.append(entry) #adding the song to the list
        cont = input("Would you like to continue building your playlist? (y/n): ")
        if cont.lower() == "n":
            printCompletedPlaylist(playlist)
            addMore = False
        #else, it will continue

# input = the list of songs
# output = none
# helper function for the user generating their own playlist
def printPlaylist(list):
    print("Your playlist so far: ")
    counter = 0
    while counter <= len(list)-1:
        print("-", list[counter])
        counter += 1
    print("----\n")

#input playlist
#output none
# will print the completed playlist
def printCompletedPlaylist(list):
    print("Your completed playlist: ")
    for item in list:
        print('-', item)

#input = artist list
# returns the artist that was chosen
def selectArtists(artists):
    counter = 0
    dict = {}
    for art in artists:
        print(str(counter) + ")", art)
        dict[counter] = art
        counter += 1
    selected = input("\nSelect an artist from the list by entering it's number (0-" + str(counter-1) + ") : ")
    if selected.isdigit():
        if int(selected) >= 0 and int(selected) < counter-1:
            print(dict[int(selected)])
            return dict[int(selected)]
        else:
            # print("Counter -1", counter-1)
            print("\nPlease enter a number within the bounds")
            selectArtists(artists)
    else:
        print("\nPlease enter a number")
        selectArtists(artists)

#input = artist to be able to get their albums
def selectedAlbum(artist):
    # print("Inside selected album") #debugg
    global dictionary
    albums = dictionary[artist]
    dict = {} #creating empty dictionary
    counter = 0
    for singleAlbum in albums:
        print(str(counter) + ")", singleAlbum)
        dict[counter] = singleAlbum #adding the item to the dictionary to be found using the index
        counter += 1
    selected = input("Select an album from the list by entering its number (0-" + str(counter-1) + "): ")
    if selected.isdigit():
        selected = int(selected)
        if selected == 0:
            return dict[selected]
        elif selected >= 0 and selected <= counter-1:
            return dict[selected]
        else:
            selectedAlbum(artist)
    else:
        selectedAlbum(artist)



    
def main():
    global dictionary
    dictionary= MusicLibraryHelper.loadLibrary(musicDatabase) #loading in the database
    displayMenu()


main()