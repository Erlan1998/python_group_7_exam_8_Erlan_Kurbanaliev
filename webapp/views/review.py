from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.models import Review, Product
from webapp.forms import ProductForm, SearchForm, ReviewForm
from django.urls import reverse
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin




class ReviewCreateView(CreateView):
    model = Product
    template_name = 'review/add.html'
    form_class = ReviewForm
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('id'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        form.save_m2m()
        return redirect('product', id=product.id)


class ReviewUpdateView(UpdateView):
    template_name = 'review/update.html'
    model = Review
    form_class = ReviewForm
    context_object_name = 'review'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.product.id})


class ReviewDelete(DeleteView):
    template_name = 'review/delete.html'
    model = Review
    context_object_name = 'review'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.product.id})
