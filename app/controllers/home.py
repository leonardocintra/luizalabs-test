from beer.controllers import BeerView


class HomeView(BeerView):

    def index(self):
        return self.render('index.html')
