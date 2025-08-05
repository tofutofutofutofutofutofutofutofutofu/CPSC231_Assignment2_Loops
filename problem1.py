# Christopher Lee
# ID: 10136117
#
# Movies list contains the list of 30 movies names
#
movies = ["Wall-E (2008)",
          "The Ring (2002)",
          "Minions (2015)",
          "The Mummy (1999)",
          "Mean Girls (2004)",
          "Million Dollar Baby (2004)",
          "The Desolation of Smaug (2013)",
          "Love Actually (2003)",
          "Scarface (1983)",
          "Oldboy (2003)",
          "Die Hard (1988)",
          "The Bourne Identity (2002)",
          "The Secret Life of Walter Mitty (2013)",
          "The Incredibles (2004)",
          "Battleship (2012)",
          "The Strangers (2008)",
          "Ratatouille (2007)",
          "Toy Story (1995)",
          "Dogville (2003)",
          "Coco (2017)",
          "Cool Hand Luke (1967)",
          "Alien (1979)",
          "Baywatch (2017)",
          "Epic Movie (2007)",
          "Stalker (1979)",
          "Up (2009)",
          "Thor: Ragnarok (2017)",
          "The Matrix Revolutions (2003)",
          "What We Do in the Shadows (2014)",
          "Deadpool (2016)"]

#
# ratings list contains the rating for 30 movies. For example:
# Deadpool(2016) has rating 5
#

ratings = [1, 5, 0, 0, 0, 1, 2, 3, 4, 4, 4, 3, 4, 0, 0, 0, 1, 2, 3, 4, 4, 4,
           1, 4, 0, 0, 0, 1, 2, 5]

totalMovies = 0
moviesNotSeen = 0

# This creates a new list that's sorted in ascending order
sortedRatings = ratings[:]
sortedRatings.sort()
# Next it takes the highest rating and stores it as both the high and low rating
highRating = sortedRatings[-1]
lowRating = sortedRatings[-1]
# These are empty lists to store the good and bad rated movies in
favouriteMovies = []
badMovies = []

for movieScore in ratings:
    # Counting the number of movies
    totalMovies += 1
    # If the score is zero, count how many movies haven't been seen
    if movieScore == 0:
        moviesNotSeen += 1
    # Since this is if else it'll ignore 0 and store the lowest number other than that
    else:
        if movieScore < lowRating:
            lowRating = movieScore

# if the rating in the rating list is the same as the highest or lowest value,
# this appends the list to the appropriate list
for indexRating, elementRating in enumerate(ratings):
    if elementRating == highRating:
        favouriteMovies.append(movies[indexRating])
    elif elementRating == lowRating:
        badMovies.append(movies[indexRating])
# This is the output the assignment wanted
print(f"Hello [error: friend name not found]! \n\nIt looks like you've seen {totalMovies - moviesNotSeen} out of {totalMovies} movies.")
print(f"\nYour favourite movies were:")
# Simple way to print the list without the brackets
for i in favouriteMovies:
    print(f"    {i}")
print(f"\nYour least favourite movies were:")
for i in badMovies:
    print(f"    {i}")
