from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView,  UpdateView, DetailView, DeleteView
from django.urls import reverse, reverse_lazy
from webapp.forms import SearchForm, ProductForm
from webapp.models import Product, Review
from django.db.models import Q
from django.utils.http import urlencode


class ProductView(ListView):
    template_name = 'products/index_product.html'
    model = Product
    context_object_name = 'products'
    ordering = ('name', 'category')
    paginate_by = 5
    paginate_orphans = 2

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['search_form'] = self.form

        if self.search_data:
            kwargs['query'] = urlencode({'search_value': self.search_data})

        return kwargs


class ProductDetailView(DetailView):
    template_name = 'products/product_view.html'
    model = Product
    pk_url_kwarg = "id"
    context_object_name = 'product'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_list = Review.objects.filter(product=self.get_object())
        paginator = Paginator(object_list, self.paginate_by, )
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if page_obj.paginator.num_pages == 1:
            context['is_paginated'] = False
        else:
            context['is_paginated'] = True
        context['page_obj'] = page_obj
        context['reviews'] = page_obj.object_list
        return context


class ProductCreate(CreateView):
    template_name = 'products/create.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.id})


class ProductUpdate(UpdateView):
    template_name = 'products/product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse('product', kwargs={'id': self.object.id})


class ProductDelete(DeleteView):
    template_name = 'products/delete.html'
    model = Product
    context_object_name = 'product'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('index_all')