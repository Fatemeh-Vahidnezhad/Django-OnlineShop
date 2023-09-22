from django import forms


class AddToCartForm(forms.Form):
    quantity_choice = [(i, str(i)) for i in range(1, 31)]
    quantity = forms.TypedChoiceField(choices=quantity_choice, coerce=int)

