class iPod:    
    def __init__(self, max_song_capacity):
        self.max_song_capacity = max_song_capacity
        self.library = {}
        self.num_songs = 0
    
    def space_available(self):
        #write this method
    
    def add_song(self, artist, song_name):
        if self.space_available() == 0:
            print("No more room for songs")
        else:

            #write missing code

            print(song_name + " by " + artist + " was added to the music library")
            
    def song_in_library(self, artist, song_name):
        """ (iPod, str, str) -> bool
        return true if song_name by artist is in the library"""

        #write missing code

    def remove_song(self, artist, song_name):
        """remove artist if no songs by artist"""
        if not song_in_library(artist, song_name):
            print("Song not found")
        else:

            #write missing code

            print(song_name + " by " + artist + " was removed from the music library")  