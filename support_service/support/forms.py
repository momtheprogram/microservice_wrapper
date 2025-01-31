from django import forms


class TicketForm(forms.Form):
    queue = forms.IntegerField()
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    submitter_email = forms.EmailField()
    priority = forms.ChoiceField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Medium'), (4, 'Low'), (5, 'Very Low')])
