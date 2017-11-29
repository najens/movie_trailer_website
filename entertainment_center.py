import media
import fresh_tomatoes

# Create instances of the Movie class.
lion_king = media.Movie(
    "The Lion King",
    ("Lion cub and future king Simba searches for his identity. His eagerness "
     "to please others and penchant for testing his boundaries sometimes gets "
     "him into trouble."),
    media.Movie.VALID_RATINGS[0],
    "8.5",
    "1h 28min",
    "Walt Disney Pictures",
    ["Roger Allers", "Rob Minkoff"],
    ["Irene Mecchi", "Jonathon Roberts", "Linda Woolverton"],
    ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"],
    "24 June 1994",
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS0"
     "0MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SY1000_CR0"
     ",0,673,1000_AL_.jpg"),
    "https://www.youtube.com/watch?v=4sj1MT05lAA")
                        
inception = media.Movie(
    "Inception",
    ("A thief, who steals corporate secrets through use of dream-sharing "
     "technology, is given the inverse task of planting an idea into the mind "
     "of a CEO."),
    media.Movie.VALID_RATINGS[2],
    "8.8",
    "2h 28min",
    "Warner Bros",
    ["Christopher Nolan"],
    ["Christopher Nolan"],
    ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
    "16 July 2010",
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5"
     "BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg"),
    "https://www.youtube.com/watch?v=d3A3-zSOBT4")
                        
lotr_fellowship = media.Movie(
    "The Lord of the Rings: The Fellowship of the Ring",
    ("A meek Hobbit from the Shire and eight companions set out on a journey "
     "to destroy the powerful One Ring and save Middle Earth from the Dark "
     "Lord Sauron."),
    media.Movie.VALID_RATINGS[2],
    "8.8",
    "2h 58min",
    "New Line Cinema",
    ["Peter Jackson"],
    ["J.R.R. Tolkien", "Fran Walsh"],
    ["Elijah Wood", "Ian McKellen", "Orlando Bloom"],
    "19 December 2001",
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BN2EyZjM3NzUtNWUzMi0"
     "0MTgxLWI0NTctMzY4M2VlOTdjZWRiXkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SY999_CR0,"
     "0,673,999_AL_.jpg"),
    "https://www.youtube.com/watch?v=V75dMMIW2B4")
                             
up = media.Movie(
    "Up",
    ("Seventy-eight year old Carl Fredricksen travels to Paradise Falls in "
     "his home equipped with balloons, inadvertently taking a young "
     "stowaway."),
    media.Movie.VALID_RATINGS[1],
    "8.3",
    "1h 36min",
    "Pixar Animation Studios",
    ["Pete Docter", "Bob Peterson"],
    ["Pete Docter", "Bob Peterson"],
    ["Edward Asner", "Jordan Nagai", "John Ratzenberger"],
    "29 May 2009",
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5"
     "BanBnXkFtZTgwNzE1MzEyMTE@._V1_SY1000_CR0,0,664,1000_AL_.jpg"),
    "https://www.youtube.com/watch?v=ZE_V0g9q4g0&pbjreload=10")
                        
dark_knight = media.Movie(
    "The Dark Knight",
    ("When the menace known as the Joker emerges from his mysterious past, he "
     "wreaks havoc and chaos on the people of Gotham, the Dark Knight must "
     "accept one of the greatest psychological and physical tests of his "
     "ability to fight injustice."),
    media.Movie.VALID_RATINGS[2],
    "9.0",
    "2h 32min",
    "Warner Bros",
    ["Christopher Nolan"],
    ["Jonathan Nolan", "Christopher Nolan"],
    ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
    "18 July 2008",
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5"
     "BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg"),
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")
                          
gladiator = media.Movie(
    "Gladiator",
    ("When a Roman General is betrayed, and his family murdered by an "
     "emperor's corrupt son, he comes to Rome as a gladiator to seek "
     "revenge."),
    media.Movie.VALID_RATINGS[3],
    "8.5",
    "2h 35min",
    "DreamWorks",
    ["Ridley Scott"],
    ["David Franzoni"],
    ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"],
    "5 May 2000",
    ("https://images-na.ssl-images-amazon.com/images/M/MV5BMDliMmNhNDEtODUyOS0"
     "0MjNlLTgxODEtN2U3NzIxMGVkZTA1L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY"
     "1000_CR0,0,675,1000_AL_.jpg"),
    "https://www.youtube.com/watch?v=ol67qo3WhJk")

# Store the instances of the Movie class in a list called movies.                        
movies = [lion_king, inception, lotr_fellowship, up, dark_knight, gladiator]

# Run the open_movies_page function from the fresh_tomatoes module. This
# function takes in a list of movie objects and creates an html web page.                           
fresh_tomatoes.open_movies_page(movies)