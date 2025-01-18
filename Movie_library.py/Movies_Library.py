
import json

class MovieLibrary:
    def __init__(self, json_file):
        self.json_file = json_file
        self.movies = self.load_movies()

    def load_movies(self):
        
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                return json.load(file)  
        except FileNotFoundError:
            print(f"The file {self.json_file} couldn't be found.")
            return []  
        

    def update_json_file(self):
        
        try:
            with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.movies, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error writing to file: {e}")

    library = MovieLibrary("movie.json")      

#1. Crea un metodo chiamato get_movies che restituisce l’intera collezione di film.

    def get_movies(self):
                                         
        return self.movies
    
    
# 2. Crea un metodo chiamato add_movie che ha i parametri title e director di tipo stringa,
#year di tipo intero e genres di tipo lista (di stringhe).
#Il metodo aggiunge il film alla collezione e aggiorna il file json
    def add_movie(self,title,director,year,genre):
        
   
     new_movie = {
            "title": "A clockwork orange",
            "director": "Stanley Kubrik",
            "year": 1971,
            "genres": ["distopian","crime"],
        }

    self.movies.append(new_movie)
    self.update_json()

#3. Crea un metodo chiamato remove_movie che ha il parametro title.
#Il metodo rimuove dalla collezione il film
#che ha titolo corrispondente (NON case sensitive) a title.
#Il metodo aggiorna il file json e restituisce il film rimosso.

    def remove_movie(self,title):
      title=title.lower

      for movie in self.movies:
          if movie['title'].lower()==title.lover():
              self.movies.remove(movie)
              self.update_json_file()
              return movie

#4. Crea un metodo chiamato update_movie che ha il parametro title
#e i parametri opzionali director, year e genres.
#Il metodo ricerca nella collezione il film
#che ha titolo corrispondente (NON case sensitive) a title.
#Quindi modifica il film,
#applicando il valore di ciascun parametro opzionale non nullo.
#Il metodo aggiorna il file json e restituisce il film coi valori aggiornati.
    def update_movie(self,title,director=None,year=None,genres=None):

        for movie in self.movies:
            if movie["title"].lower() == title.lower():

             if director:
                movie["director"]=director

             if year:
                movie["year"]=year

             if genres: 
                movie["genre"]=genres
            
             self.update_json_file()
             return movie

        else:
             return (f"this movie{title} doesn't exist.")

5#Crea un metodo chiamato get_movie_titles
#che restituisce una lista contenente tutti i titoli dei film nella collezione

def get_movie_titles(self):
        for movies in self.movies:

            return [movie['title'] for movie in self.movies]



#6. Crea un metodo chiamato count_movies
#che restituisce il numero totale dei film nella collezione.

def count_movies(self):
    

     return len(self.movies)



#7. Crea un metodo chiamato get_movie_by_title che ha il parametro title.
#Il metodo restituisce il film
#che ha titolo corrispondente (NON case sensitive) a title.
def get_movie_by_title(self,title):

    for movie in self.movies:
        if movie["title"].lower() == title.lower():
            return movie

   


#8. Crea un metodo chiamato get_movies_by_title_substring
#che ha il parametro substring.
#Il metodo restituisce una lista di tutti i film che contengono, nel titolo,
#una sottostringa corrispondente (case sensitive) a substring.
def get_movies_by_title_substring(self, substring):
    
    if not substring:
        return []  

    matching_movies = [movie for movie in self.movies if substring in movie['title']]
    return matching_movies



#9. Crea un metodo chiamato get_movies_by_year che ha il parametro year.
#Il metodo restituisce una lista di tutti i film con anno corrispondente a year.
def get_movies_by_year(self,year):

  return [movie for movie in self.movies if movie["year"] == year]               



#10. Crea un metodo chiamato count_movies_by_director che ha il parametro director.
#Il metodo restituisce un numero intero che rappresenta,
#quanti film del director scelto sono presenti nella collezione.
#Il director va confrontato in modo NON case sensitive.

def count_movies_by_director(self, director):
        
        director = director.lower()
        return len([movie for movie in self.movies if movie['director'].lower() == director])




#11. Crea un metodo chiamato get_movies_by_genre che ha il parametro stringa genre.
# Il metodo restituisce una lista di tutti i film che hanno genere corrispondente a genre.
#Il genre va confrontato in modo NON case sensitive.
def _movies_by_genre(self,genre=str):
 
 return [movie for movie in self.movies if movie["genre"].lower() == genre.lower()]


#12. Crea un metodo chiamato get_oldest_movie_title che restituisce
#il titolo del film più antico della collezione.
def get_oldest_movie_title(self):
    
    oldest_movie = min(self.movies, key=get_year)

    return oldest_movies["title","year"]




#13. Crea un metodo chiamato get_average_release_year che restituisce
#un float rappresentante la media aritmetica degli anni di pubblicazione
#dei film della collezione.
def get_average_release_year(self):
    
    if not self.movies:
        return 0.0  

    total_years = sum(movie["year"] for movie in self.movies)  
    average_year = total_years / len(self.movies)  
    return float(average_year)

   

#14. Crea un metodo chiamato get_longest_title che restituisce il titolo
#più lungo della collezione di film.

def get_longest_title(self):
    max_length = max(len(movie["title"]) for movie in self.movies)
    return [movie["title"] for movie in self.movies if len(movie["title"]) == max_length]


#15. Crea un metodo chiamato get_titles_between_years che ha due parametri:
#start_year e end_year.
#Il metodo restituisce una lista contenente i titoli dei film pubblicati
#dall’anno start_year fino all’anno end_year (estremi compresi).#

def get_titles_between_years(self, start_year,end_year):
    
   for movie in self.movies:
        return [movie['title'] for movie in self.movies if start_year <= movie['year'] <= end_year]




#16. Crea un metodo chiamato get_most_common_year
#che restituisce l’anno che si ripete più spesso fra i film della collezione.
 #Non considerare il caso in cui vi siano pari merito.#

def get_most_common_year(self):
    
    years = [movie['year'] for movie in self.movies]
    
    year_counts = Counter(years)

    most_common_year = year_counts.most_common(1)[0][0] 
    
    return most_common_year

#17. Modifica il metodo costruttore affinché,
#se nel percorso json_file non viene trovato alcun file,
#venga sollevata l’eccezione FileNotFoundError
#col messaggio personalizzato “File not found: ” seguito dal percorso json_file.#


def update_json(self):

    
    with open(self.movies.json, 'w') as file:

        
        if not movies.json.exists(movies.json):
            
        
            raise FileNotFoundError(f"File not found: {movies.json}")



#18. Modifica i metodi remove_movie e update_movie affinché,
#se non viene trovato alcun film avente come titolo title,
#venga sollevata l’eccezione personalizzata MovieNotFoundError,
#avente il messaggio “Movie was not found”.
#Tale eccezione va definita all’interno della classe MovieLibrary.#

class MovieNotFoundError(Exception):
    pass



class MovieLibrary:
    

    def __init__(self, json_file):
        self.json_file = json_file  
        try:

            
            with open(self.json_file, 'r', encoding='utf-8') as file:

                self.movies = json.load(file)  
        except FileNotFoundError:
            
            self.movies = []

    
    def update_json_file(self):
        with open(self.json_file, "w", encoding="utf-8") as file:

         
            json.dump(self.movies, file, indent=4, ensure_ascii=False)

    
    def remove_movie(self, title):

        
        for movie in self.movies:
        
            
            if movie["title"].lower() == title.lower():
                self.movies.remove(movie)  
                self.update_json_file()  
                return movie  

        
        raise MovieNotFoundError(f"Movie with title '{title}' was not found")





