class SongLength:
    def __init__(self, length):
        self.lenght = length
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        parts = [int(part.strip()) for part in length.split(":")]

        if len(parts) == 3:
            self.hours = parts[0]
            self.minutes = parts[1]
            self.seconds = parts[2]
        elif len(parts) == 2:
            self.minutes = parts[0]
            self.seconds = parts[1]
        else:
            raise ValueError("Lenght not correct: {}".format(length))

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.hours * 60 + self.minutes

    def get_seconds(self):
        return self.get_minutes() * 60 + self.seconds


class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.__lengthObject = SongLength(length)

    def __str__(self):
        return "{} - {} from {} - {}"\
              .format(self.title, self.artist, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.__str__())

    def prepare_json(self):
        song_dict = self.__dict__
        return{key: song_dict[key] for key in song_dict if not key.startwith(" ")}

    def get_length(self, seconds=False, minutes=False, hours=False):
        if not seconds and not minutes and not hours:
            return self.length

        if seconds:
            return self.lengthObject.get_seconds()

        if minutes:
            return self.lengthObject.get_minutes()

        if hours:
            return self.lengthObject.get_hours()


class PlayList:
    def __init__(self, name, repeat=False, shuffle=False):
        self.songs = []
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.shuffle_played_songs = set()
        self.current_song_index = 0

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        try:
            self.songs.remove(song)
        except ValueError:
            pass

    def total_length(self):
        total_seconds = sum([song.get_length(seconds=True) for song in self.songs])
        return str(datetime.timedelta(seconds = total_seconds))

        def artists(self):
            all_artists = [song.artist for song in self.songs]
            return {name: all_artists.count(name) for name in all_artists}

        def has_next_song(self):
            return self.current_song_index < len(self.songs)

        def shuffle(self):
            song = random.choice(self.songs)

            while song in self.shuffle_played_songs:
                song = random.choice(self.songs)

            self.shuffle_played_songs.add(song)

            if len(self.shuffle_played_songs) == len(self.songs):
                self.shuffle_played_songs = set()

            return song

        def next_song(self):
            if self.repeat == "Song":
                return self.songs[self.current_song_index]

            if self.shuffle:
                return self.shuffle()

            if not self.has_next_song() and self.repeat =="None":
                raise Exception("end of PlayList")

            if not self.has_next_song() and self.repeat == "Playlist":
                self.current_song_index = 0

            song = self.songs[self.current_song_index]
            self.current_song_index += 1

            return song

        def print_playlist(self):
            headers = ["Artist", "song", "length"]
            table = []

            for song in self.songs:
                table.append(song.artist, song.title, song.length)
            print(tabulate(table,headers=headers))

        def prepare_json(self):
            data = {
                "name": self.name,
                "songs": [song.prepare_json() for song in songs]
                }
            return data

        def save(self, indent=True):
            filename = self.name.replace("", "-") + ".json"

            with open(filename, "w") as f:
                f.write(json.dumps(self.prepare_json(), indent=indent))

        @staticmethod
        def load(filename):
            with open(filename, "r") as f:
                contents = f.read()
                data = json.loads(contents)
                p = PlayList(data["name"])

                for dict_song in data["songs"]:
                    song = song(artist=dict_song["artist"]), title = dict_song["title"], album = dict_song["album"], length = dict_song["length"]
                    return p

         def test_load():
            p = Playlist.load("Manowar - songs.json")
            try:
                while True:
                    song = p.next_song()
                    print(str(song))
                    time.sleep(1)
                except Exception as e:
                    print(e)

        def test_save():
            s = Song(album="The Sons of Odin", title="Odin", artist="Manowar", length="3:44")
            s1 = Song(album="The Sonds of Odin", title="Sons of Odin", artist="Manowar", length="6:08")
            p = Playlist("Manowar songs", repeat="SONG")
            p.add_song(s)
            p.add_song(s1)
            p.add_song(Song(album="Fallen", title="Bring Me To Life (radio edit)", artist="Evanesence", length="3:30"))
            p.pprint_playlist()
            p.save()

test_load()

            }



