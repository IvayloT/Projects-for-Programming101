import sqlite3


conn = sqlite3.connect("movie.db")
cursor = conn.cursor()

create_movie_table = """
CREATE TABLE IF NOT EXISTS
Movie(id INTEGER PRIMARY KEY,name TEXT,raiting INTEGER)
"""

insert_movie = """
INSERT INTO Movie(name,raiting)
VALUES("The Hunger Games: Catching Fire", 7.9),
      ("Wreck-it-Ralph", 7.8),
      ("Her", 8.3)
      """
cursor.execute(create_movie_table)
cursor.execute(insert_movie)
conn.commit()
