from movies import Movies
from projection import Projections

class Reservation:

    INSERT_USERNAME = """
        INSERT INTO Reservation(username)
        VALUES(?)
        """

    SEARCH_FOR_USERNAME = """
    SELECT username
    FROM Reservation
    """

    CHOOSE_MOVIE_NAME = """
    SELECT name
    FROM Movies
    WHERE id = ?
    """

    AVALIVABLE_SEATS = """
    SELECT avalivable_seats
    FROM Projections
    """

    UPDATE_ROW_AND_COLUMN = """
    UPDATE Reservation
    SET row = ?, col = ?
    WHERE id = ?
    """

    SET_ROW_AND_COL = """
    SELECT id
    FROM Reservation
    WHERE username = ? AND row=-1 AND col=-1
    """

    SELECT_ROW_AND_COL_WITH_ID = """
    SELECT row, col
    FROM Reservation
    WHERE id = ?
    """

    @classmethod
    def make_reservation(cls, conn, username):

        cursor = conn.cursor()

        cursor.execute(cls.INSERT_USERNAME, (username,))
        Movies.show_current_movies(conn)
        conn.commit()

    @classmethod
    def search_username(cls, conn, username):

        cursor = conn.cursor()

        cursor.execute(cls.SEARCH_FOR_USERNAME)
        conn.commit()

    @classmethod
    def choose_movie(cls, conn, movie_id):
        choice = Projections.show_current_movies(conn, movie_id=movie_id)
        return choice

    @classmethod
    def change_row_col(cls, conn, name, row, column):
        cursor = conn.cursor()

        value = cursor.execute(cls.SET_ROW_AND_COL, (name,))
        result = value.fetchone()[0]
        print(result)
        cursor.execute(cls.UPDATE_ROW_AND_COLUMN, (row, column, result))
        res = cursor.execute(cls.SELECT_ROW_AND_COL_WITH_ID, (result,))
        print(result.fetchone())
        conn.commit()
