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
# all_ratings contains the rating of every movie from 4 friends
#

all_ratings = [
    [5, 5, 4, 4, 3, 1, 2, 3, 4, 4, 4, 3, 4, 0, 0, 0, 1, 2, 3, 4, 4, 4, 1, 4, 0, 0, 0, 1, 2, 5],
    [5, 0, 1, 2, 3, 1, 2, 3, 4, 4, 4, 5, 4, 2, 1, 0, 1, 2, 0, 5, 0, 4, 1, 4, 2, 0, 0, 1, 0, 5],
    [5, 2, 3, 4, 4, 0, 0, 0, 4, 5, 0, 3, 0, 0, 0, 3, 4, 0, 1, 4, 4, 4, 0, 4, 0, 3, 0, 1, 2, 5],
    [5, 0, 4, 0, 0, 4, 2, 3, 0, 0, 4, 0, 3, 0, 1, 0, 1, 2, 3, 0, 2, 0, 1, 0, 0, 0, 4, 0, 1, 5],
    [5, 4, 3, 2, 1, 1, 2, 3, 4, 3, 4, 3, 4, 0, 3, 0, 1, 2, 4, 4, 4, 4, 1, 4, 0, 0, 0, 1, 2, 5],
]

def highestFinder(numberlist):
    for indexPopular, elementPopular in enumerate(numberlist):
        fakeList = numberlist[:]
        fakeList.sort()
        if elementPopular == fakeList[-1]:
            print(f"    {movies[indexPopular]}")


def lowestFinder(numberlist):
    for indexPopular, elementPopular in enumerate(numberlist):
        fakeList = numberlist[:]
        fakeList.sort()
        if elementPopular == fakeList[0]:
            print(f"    {movies[indexPopular]}")


averageSeen = []
popularMovies = []
averageRatings = []
fakeList = []
totalMovies = len(movies)
finalAverage = 0
# creating Lists that are the same length as the movie list
for i in range(totalMovies):
    popularMovies.append(0)
    averageRatings.append(0)
# Having two loops lets me navigate to the same place within two lists and
# store multiple variables within the different lists
for outerIndex, friendList in enumerate(all_ratings):
    seenMovies = len(movies)
    # second part is pretty similar to the first assignemnt
    for innerIndex, innerRatings in enumerate(friendList):
        if innerRatings == 0:
            seenMovies -= 1
        else:
            popularMovies[innerIndex] += 1
            averageRatings[innerIndex] += innerRatings
    averageSeen.append(seenMovies)

for i in averageSeen:
    finalAverage += i
finalAverage /= len(averageSeen)

for x, y in enumerate(averageRatings):
    averageRatings[x] /= popularMovies[x]

print(f"\nOn average, Each friend has seen {finalAverage} of the {len(movies)} movies.")
print(f"\nThe most popular movies were:")
highestFinder(popularMovies)
print(f"\nThe least popular movies were:")
lowestFinder(popularMovies)
print(f"\n The highest rated movies were:")
highestFinder(averageRatings)
print(f"\n The lowest rated movies were:")
lowestFinder(averageRatings)