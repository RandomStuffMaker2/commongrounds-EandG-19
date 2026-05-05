from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, Transaction
from .forms import ProductForm, TransactionForm


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'merchstore/product_create.html'
    context_object_name = 'product_create'
    # success_url = 'merchstore/product_list.html'

#this subclass is how owner is autofilled
    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransactionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class CartListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'merchstore/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Transaction.objects.filter(buyer=self.request.user.profile)
    
    def post(self, request, *args, **kwargs):
        return redirect('merchstore:cart')