import media
import fresh_tomatoes

worlds_end = media.Movie("The World's End", "A pub crawl reunion turns into a fight for saving the planet.", 
	"https://upload.wikimedia.org/wikipedia/en/d/d8/The_World%27s_End_poster.jpg", "https://www.youtube.com/watch?v=rQA7HcRcLNg")

scott_pilgrim = media.Movie("Scott Pilgrim", "To date his dream girl, he must battle with her seven evil exes.",
	"https://upload.wikimedia.org/wikipedia/en/1/14/Scott_Pilgrim_vs._the_World_teaser.jpg", "https://www.youtube.com/watch?v=7wd5KEaOtm4")

galaxy_quest = media.Movie("Galaxy Quest", "Sci-fi actors are launched into a real alien adventure.", 
	"https://upload.wikimedia.org/wikipedia/en/1/1f/Galaxy_Quest_poster.jpg", "https://www.youtube.com/watch?v=B34jbC43XzA")

guardians_galaxy = media.Movie("Guardians of the Galaxy", "Galactic criminals band together to fight a power-hungry warrior.", 
	"https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg", "https://www.youtube.com/watch?v=d96cjJhvlMA")

serenity = media.Movie("Serenity", "Space pirates protect a wanted girl with strange powers.", 
	"https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg", "https://www.youtube.com/watch?v=w8JNjmK5lfk")

silence_lambs = media.Movie("Silence of the Lambs", "To find one serial killer, she must seek the help of another.",
	"https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg", "https://www.youtube.com/watch?v=W6Mm8Sbe__o")

movies = [worlds_end, scott_pilgrim, guardians_galaxy, galaxy_quest, serenity, silence_lambs]

fresh_tomatoes.open_movies_page(movies)
