from database.database import Database

class MusicTracks:

    @staticmethod
    def get_music_tracks(track_id: int):
        stmt = "SELECT * FROM music_tracks WHERE id =%s"
        Database.cursor().execute(stmt, (track_id,))
        return Database.cursor().fetchone()

    @staticmethod
    def get_all():


    @staticmethod
    def get_by_id(track_id: int):
        stmt = "SELECT * FROM tracks"
        Database.cursor().execute(stmt)
        return Database.cursor().fetchall()

    @staticmethod
    def get_by_name(track_name: int):
        stmt = "SELECT * FROM tracks"
        Database.cursor().execute(stmt)
        return Database.cursor().fetchall()

    @staticmethod
    def get_by_creation_date(track_creation_date: int):
        stmt = "SELECT * FROM tracks"
        Database.cursor().execute(stmt)
        return Database.cursor().fetchall()

    @staticmethod
    def get_by_track_legnt(track_lenght: int):
        stmt = "SELECT * FROM tracks"
        Database.cursor().execute(stmt)
        return Database.cursor().fetchall()