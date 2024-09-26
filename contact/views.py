from django.shortcuts import get_object_or_404, render
from contact.models import Contact


def index(request):
    contacts = Contact.objects.all().order_by('-id')
    context = {'contacts': contacts, }
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id)
    context = {'contact': single_contact, }
    return render(request, 'contact/contact.html', context)
