# movie_trailer_website

movie_trailer_website is a python project that uses class objects to create a movie trailer website. When you run the code, it will create an html page with movie information that will open in your browser. In the webpage you can read movie details and play a trailer by clicking on a movie container.

## Software Requirements

- [Python 2.7.x](https://www.python.org/downloads/release/python-2714/)
- [Git or Git Bash](https://git-scm.com/downloads)

## Installation Instructions

- Open Git or Git Bash in you workspace directory
- Clone the GitHub repository
  ```
  $ git clone https://github.com/najens/movie_trailer_website.git
  ```
## Run Program

- To run the python script:
  ```
  $ cd movie_trailer_website
  $ python entertainment_center.py
  ```

## Customize Movies

- Open entertainment_center.py in your favorite text editor
- Edit or Add a new instances of the Movie class
 
  ```
  # Create instances of the Movie class.
  lion_king = media.Movie(
      "The Lion King",
      ("Lion cub and future king Simba searches for his identity. His " 
	   "eagerness to please others and penchant for testing his boundaries "
	   "sometimes gets him into trouble."),
      media.Movie.VALID_RATINGS[0],
      "8.5",
      "1h 28min",
      "Walt Disney Pictures",
      ["Roger Allers", "Rob Minkoff"],
      ["Irene Mecchi", "Jonathon Roberts", "Linda Woolverton"],
      ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"],
      "24 June 1994",
      ("https://images-na.ssl-images-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE"
	   "3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SY"
	   "1000_CR0,0,673,1000_AL_.jpg"),
      "https://www.youtube.com/watch?v=4sj1MT05lAA")
  ```
    A movie class contains the following attributes:
    - movie_title: is the title of the movie
    - movie_storyline: is the storyline of the movie
    - movie_rating: is the rating of the movie
	- movie_score: is the IMDB rating of the movie from 0.0-10
	- movie_runtime: is the length of the movie #h ##m
	- movie_producer: is the production company of the movie
	- movie_directors: is a list of directors for the movie
	- movie_writers: is a list of writers for the movie
	- movie_stars: is a list of the main stars of the movie
	- movie_release_date: is the release date of the movie dd mmmm yyyy
	- poster_image: is the url of the poster image of the movie
	- trailer_youtube: is the url of the youtube trailer
  
