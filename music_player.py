class SongNode():
    def __init__(self, songName, album, artist):
        self.songName = songName
        self.album = album
        self.artist = artist
        self.prev = None
        self.next= None

class Playlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        
    def add_song(self, songName, album, artist):
        node = SongNode(songName, album, artist)
        
        if not self.head:
            self.head = self.tail = self.current = node # if there is only one song
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
    def show_current(self): #to identify the song currently playing
        if self.current:
            print("Now Playing",self.current.songName,"-",self.current.artist,"from the album",self.current.album)
      
                
    def next_track(self):
        if self.current and self.current.next:#if there is a next song and a currrent song playing
            self.current = self.current.next #next song becomes current song
            
    def prev_track(self):
        if self.current and self.current.prev: #if there is a previous song and a currrent song playing
            self.current = self.current.prev #previous song becomes current song



my_vibe = Playlist() # object of Class Playlist
#songs in my_vibe
my_vibe.add_song("Asaksuabashi", "B4SA", "Nine Vicious")
my_vibe.add_song("The Truth", "Studio Addict", "Nine Vicious")
my_vibe.add_song("Ball Hog Summer", "Ball Hog Summer", "Protect")
my_vibe.add_song("Havana", "Havana", "Pz'")
my_vibe.add_song("Durango", "Durango", "Pz'")
my_vibe.add_song("New Means", "FOR NOTHING", "Nine Vicious")
my_vibe_.add_song("Imma krazy X", "Studio Addict", "Nine Vicious")

my_vibe.show_current()
my_vibe.next_track()
my_vibe.next_track()
my_vibe.show_current()

#user adding songs
