from django.shortcuts import render, get_object_or_404

from books.models import Books, Poster
from . import forms
from django.views import generic


class SearchListView(generic.ListView):
        template_name = 'blog/books_list.html'
        context_object_name = 'books'
        paginate_by = 5

        def get_queryset(self):
                return Books.objects.filter(name__icontains=self.request.GET.get('q'))

        def get_context_data(self,*, object_list=None, **kwargs):
                context = super().get_context_data(**kwargs)
                context['q'] = self.request.GET.get('q')
                return context
class EditBookView(generic.edit.UpdateView):
        template_name = "blog/edit_books.html"
        form_class = forms.BookForm
        success_url = "/books/books_catalog"

        def get_object(self, **kwargs):
                book_id = self.kwargs.get('book_id')
                return get_object_or_404(Books, id=book_id)

        def form_valid(self, form):
                print(form.cleaned_data)
                return super(EditBookView, self).form_valid(form=form)


class BooksDeleteList(generic.DeleteView):
        template_name = "blog/confirm_delete.html"

        def get_object(self, **kwargs):
                book_id = self.kwargs.get('book_id')
                return get_object_or_404(Books, id=book_id)


class CreateBookView(generic.CreateView):
        template_name = "blog/create_books.html"
        form_class = forms.BookForm
        success_url = "/books/books_catalog"

        def form_valid(self, form):
                print(form.cleaned_data)
                return super(CreateBookView, self).form_valid(form=form)



class BooksListView(generic.ListView):
        template_name = 'blog/books_list.html'
        context_object_name = 'books'
        model = Books
        ordering = ['-id']

        def get_queryset(self):
                return self.model.objects.all()

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context['poster'] = Poster.objects.order_by('-id')
                return context


class BooksDetailView(generic.DetailView):
        template_name = 'blog/books_detail.html'
        context_object_name = 'book_id'

        def get_object(self, **kwargs):
                book_id = self.kwargs.get('book_id')
                return get_object_or_404(Books, id=book_id)

