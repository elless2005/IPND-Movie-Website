import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""
    	Behavior: initializes instances of movies
    	Inputs: self, movie title string, storyline string, poster image url, youtube url
    	Outputs: none
    	""" 
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		"""
    	Behavior: from webbrowser module, uses the open function to open movie trailer url on youtube
    	Inputs: self, youtube url
    	Outputs: webbrowser opens to given url
    	""" 