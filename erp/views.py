from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm, InBoundForm, OutBoundForm, Inventory
# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product')
    else:
        return redirect('/sign-in')


def product_list(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_inven = Inventory.objects.all().order_by('-updated_at')
            for inv in all_inven:
                inv.product.size = dict(inv.product.sizes)[inv.product.size]

            my_product_form = ProductForm()
            inbound_form = InBoundForm()
            outbound_form = OutBoundForm()
            return render(request, 'erp/product_list.html', {'inventorys': all_inven, 'create_form': my_product_form, 'inbound_form': inbound_form, 'outbound_form': outbound_form})
        return redirect('/sign-in/')


@login_required
def product_create(request):
    if request.method == 'POST':
        my_product_form = ProductForm(request.POST)
        if my_product_form.is_valid():
            cloth_code = my_product_form.cleaned_data['code']
            cloth_size = my_product_form.cleaned_data['size']
            if 'jean' in cloth_code and cloth_size != 'F':
                return redirect('/')
            my_product_form.save()
            return redirect('/')
        return redirect('/product/')


@login_required
def inbound(request):
    if request.method == 'POST':
        inbound_form = InBoundForm(request.POST)
        if inbound_form.is_valid():
            inbound_form.save()
            return redirect('/')
        return redirect('/product/')


@login_required
def outbound(request):
    if request.method == 'POST':
        outbound_form = OutBoundForm(request.POST)
        if outbound_form.is_valid():
            if outbound_form.cleaned_data['code_name_size'].stock_count - outbound_form.cleaned_data['amount'] < 0:
                return redirect('/')
            outbound_form.save()
            return redirect('/')
        return redirect('/product/')