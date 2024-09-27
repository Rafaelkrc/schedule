from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from contact.models import Contact
from contact.forms import ContactForm


def index(request):
    contacts = Contact.objects.all().order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contato - '
    }
    return render(request, 'contact/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(phone__icontains=search_value) |
            Q(email__icontains=search_value)
        ).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contactdetail(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id)
    site_title = f'{single_contact.first_name} {single_contact.last_name} - '
    context = {
        'contact': single_contact,
        'site_title': site_title
    }
    return render(request, 'contact/contact.html', context)


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')
        
        return render(
            request,
            'contact/create.html',
            context
        )

    context = { 'form': ContactForm()}

    return render(
        request,
        'contact/contact_create.html',
        context
    )