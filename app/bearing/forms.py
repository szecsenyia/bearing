from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "MY placeholder"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                "placeholder": "MY placeholder",
                                "class": "new-class-name two",
                                "rows": 10,
                                "cols": 30
                            }
                        )
                    )
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
                'title',
                'description',
                'price',
                'ingredients',
                'available'
        ]

    def valid_title(self, *arg, **kwargs): # Validation
        title = self.cleaned_data.get("title")
        if "beer" in title:
            return title
        else:
            raise forms.ValidationError("Please add a valid title")

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "MY placeholder"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                "placeholder": "MY placeholder",
                                "class": "new-class-name two",
                                "rows": 10,
                                "cols": 30
                            }
                        )
                    )
    price = forms.DecimalField()
