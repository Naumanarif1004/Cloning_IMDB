from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie ,Movie_Links

def slider_movies(request):
     movies = Movie.objects.all().order_by('created')[0:3]

     return{'slider_movies': movies}
class HomeView(ListView):
    model =Movie
    template_name='movie/home.html'

   

    def get_context_data(self, **kwargs):
        context = super(HomeView , self).get_context_data(**kwargs)
        context["Most_Watched"] = Movie.objects.filter(status="MW")
        context["Recently_Added"] = Movie.objects.filter(status="RA")
        context["Top_Rated"] = Movie.objects.filter(status="TR")
        return context

class MovieList(ListView):
    model = Movie
    paginate_by = 2
    #template_name = ".html"

class MovieDetail(DetailView):

    model = Movie
    #template_name = ".html"

    #Method for getting the single object
    def get_object(self):
        object = super(MovieDetail ,self).get_object() 
        object.views_count += 1
        object.save()
        return object
    #Method for getting the links dor this object
    def get_context_data(self, **kwargs):
        context = super(MovieDetail ,self).get_context_data(**kwargs)        
        context['links'] = Movie_Links.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        return context

class MovieCategory(ListView):
    paginate_by = 2
    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory , self).get_context_data(**kwargs)
        context["movie_category"] = self.category
        return context

class MovieLanguage(ListView):
    paginate_by = 2
    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage , self).get_context_data(**kwargs)
        context["movie_language"] = self.language
        return context
    
class MovieSearch(ListView):
    model = Movie
    paginate_by = 2
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Movie.objects.filter(title__icontains=query)
        else:
            object_list=self.model.objects.none()

        return object_list

class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list= True
    allow_future = True