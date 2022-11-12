# 4 task
# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
  def __init__(self, title, director, budget):
    self.title = title
    self.director = director
    self.budget = budget

  def __repr__(self):
    return f'(Pavadinimas: {self.title}, Režisierius: {self.director}, Biudžetas: {self.budget} USD)'  

  def was_expensive(self):
    if self.budget > 100000000:
      return True
    else:
      return False

movie1 = Movie('Šrekas', 'Andrew Adamson', 60000000)
movie2 = Movie('Hobitas', 'Peter Jackson', 7000000000)

print(movie1, movie2)
print(movie1.was_expensive())
print(movie2.was_expensive())