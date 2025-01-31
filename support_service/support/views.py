import requests
from django.shortcuts import render
from .forms import TicketForm


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = {
                "queue": form.cleaned_data['queue'],
                "title": form.cleaned_data['title'],
                "description": form.cleaned_data['description'],
                "submitter_email": form.cleaned_data['submitter_email'],
                "priority": form.cleaned_data['priority'],
            }
            response = requests.post(
                'http://127.0.0.1:8000/api/tickets/',
                json=data,
                headers={
                    'Authorization': 'Basic YWRtaW46YWRtaW4=',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            )
            if response.status_code == 201:
                ticket_id = response.json().get('id')
                return render(request, 'support/success.html', {'ticket_id': ticket_id})
            else:
                context = {
                    'error': 'Произошла ошибка при создании тикета',
                    'status_code': response.status_code,
                }
                return render(request, 'support/error.html', context)
    else:
        form = TicketForm()

    return render(request, 'support/create_ticket.html', {'form': form})
