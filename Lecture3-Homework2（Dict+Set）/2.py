class MovieRatingSystem:
    def __init__(self):
        self.movieRatings = {}

    def addMovieRating(self, movieName, rating):
        self.movieRatings[movieName] = rating

    def findMovieRating(self, movieName):
        return self.movieRatings.get(movieName, "Movie not found.")

    def modifyMovieRating(self, movieName, newRating):
        if movieName in self.movieRatings:
            self.movieRatings[movieName] = newRating
            return "Movie rating updated successfully."
        else:
            return "Movie not found."

    def deleteMovieRating(self, movieName):
        if movieName in self.movieRatings:
            del self.movieRatings[movieName]
            return "Movie rating deleted successfully."
        else:
            return "Movie not found."

    def printAllMoviesAndRatings(self):
        for movie, rating in self.movieRatings.items():
            print(f"{movie}: {rating}")

def main():
    movieSystem = MovieRatingSystem()

    while True:
        print("\nMovie Rating System")
        print("1. Add Movie Rating")
        print("2. Find Movie Rating")
        print("3. Modify Movie Rating")
        print("4. Delete Movie Rating")
        print("5. Print All Movies and Ratings")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            movieName = input("Enter movie name: ")
            rating = input("Enter movie rating (0.0 to 10.0): ")
            movieSystem.addMovieRating(movieName, float(rating))
            print("Movie rating added successfully.")
        elif choice == "2":
            movieName = input("Enter movie name: ")
            rating = movieSystem.findMovieRating(movieName)
            print(f"Rating for {movieName}: {rating}")
        elif choice == "3":
            movieName = input("Enter movie name: ")
            newRating = input("Enter new movie rating (0.0 to 10.0): ")
            result = movieSystem.modifyMovieRating(movieName, float(newRating))
            print(result)
        elif choice == "4":
            movieName = input("Enter movie name: ")
            result = movieSystem.deleteMovieRating(movieName)
            print(result)
        elif choice == "5":
            movieSystem.printAllMoviesAndRatings()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
