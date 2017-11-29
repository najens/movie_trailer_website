import webbrowser


class Movie():
    """
    This class stores movie related information
    """

    # Global list of valid movie ratings
    VALID_RATINGS = ["G", "PG", "PG13", "R"]

    def __init__(
            self, movie_title, movie_storyline, movie_rating, movie_score,
            movie_runtime, movie_producer, movie_directors, movie_writers,
            movie_stars, movie_release_date, poster_image, trailer_youtube):
        """
        Constructor that inits Movie class.
            self: is the instance of the Movie class
            movie_title: is the title of the movie
            movie_storyline: is the storyline of the movie
            movie_rating: is the rating of the movie
            movie_score: is the IMDB rating of the movie from 0.0-10
            movie_runtime: is the length of the movie #h ##m
            movie_producer: is the production company of the movie
            movie_directors: is a list of directors for the movie
            movie_writers: is a list of writers for the movie
            movie_stars: is a list of the main stars of the movie
            movie_release_date: is the release date of the movie dd mmmm yyyy
            poster_image: is the url of the poster image of the movie
            trailer_youtube: is the url of the youtube trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.score = movie_score
        self.runtime = movie_runtime
        self.producer = movie_producer
        self.directors = movie_directors
        self.writers = movie_writers
        self.stars = movie_stars
        self.release_date = movie_release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens a browser to play trailer.
            self: is the instance of the Movie class
        """
        webbrowser.open(self.trailer_youtube_url)
