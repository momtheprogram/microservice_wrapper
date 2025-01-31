from django.http import JsonResponse
from rest_framework.decorators import api_view
from .forms import TicketForm
import requests


@api_view(['POST'])
def create_ticket(request):
    form = TicketForm(request.data)
    if form.is_valid():
        data = {
            'subject': form.cleaned_data['subject'],
            'message': form.cleaned_data['message'],
            'email': form.cleaned_data['email'],
        }
        response = requests.post('http://your-helpdesk-url/api/tickets/', json=data)

        if response.status_code == 201:
            return JsonResponse({'ticket_number': response.json().get('ticket_number')}, status=201)
        else:
            return JsonResponse({'error': 'Failed to create ticket'}, status=response.status_code)
    else:
        return JsonResponse({'errors': form.errors}, status=400)
