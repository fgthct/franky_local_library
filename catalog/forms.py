from django import forms


from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Inserisci una data compresa tra adesso e 4 settimane (default 3.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Controlla la data che non sia nel passato
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Controlla che la data da cambiare è nell'intervallo consentito dal bibliotecario
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Ricorda di ritornare sempre la data pulita
        return data
