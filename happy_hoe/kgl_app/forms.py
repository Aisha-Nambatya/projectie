
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django import forms
from .models import *
from .models import Deffered_payments
from django.core.validators import MinValueValidator, RegexValidator
from django.utils import timezone



# Validator for names (letters and spaces only)
name_validator = RegexValidator(regex=r'^[a-zA-Z\s]+$', message="Enter a valid name. Only letters and spaces are allowed.")

# Validator for alphanumeric branch names
branch_name_validator = RegexValidator(regex=r'^[a-zA-Z0-9\s]+$', message="Enter a valid branch name. Only letters, numbers, and spaces are allowed.")

# Validator for numeric fields
numeric_validator = RegexValidator(regex=r'^\d+(\.\d{1,2})?$', message="Enter a valid number.")

class SaleForm(ModelForm):
    branch_name = forms.CharField(validators=[branch_name_validator])  # Regex for branch name allowing letters, numbers, and spaces
    issued_to = forms.CharField(validators=[name_validator])  # Regex validator for issued_to (letters and spaces)
    quantity = forms.CharField(validators=[numeric_validator])  # Ensure quantity is a valid number
    unit_price = forms.CharField(validators=[numeric_validator])  # Ensure unit_price is a valid number
    
    class Meta:
        model = Sales
        fields = ['branch_name', 'issued_to', 'quantity', 'unit_price', 'amount_received']


#class Deffered_paymentsForm(ModelForm):
    #class Meta:
        #model = Deffered_payments
        #fields = '__all__'






"""class Deffered_paymentsForm(forms.ModelForm):
    class Meta:
        model = Deffered_payments
        fields = '__all__'  # List the fields you want in the form

    # Custom validation for a specific field (e.g., amount must be positive)
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount

    # General validation method for the entire form
    def clean(self):
        cleaned_data = super().clean()
        balance = cleaned_data.get('balance')
        due_date = cleaned_data.get('due_date')

        if balance is not None and balance < 0:
            raise forms.ValidationError("Balance cannot be negative.")

        if due_date is not None and due_date < cleaned_data.get('payment_date'):
            raise forms.ValidationError("Due date cannot be earlier than the payment date.")

        return cleaned_data
        """


class Deffered_paymentsForm(forms.ModelForm):
    # Existing validators
    name = forms.CharField(
        max_length=100,
        validators=[RegexValidator(regex='^[a-zA-Z ]*$', message='Name must contain only letters and spaces')]
    )
    amount = forms.DecimalField(
        validators=[MinValueValidator(0, message="Amount must be positive")]
    )
    nin = forms.CharField(
    max_length=14,
    validators=[RegexValidator(regex='^[A-Za-z0-9]{14}$', message='NIN must be 14 characters, including only letters and digits')]
)

    
    # New validations
    contact = forms.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='Contact must be exactly 10 digits')]
    )
    address = forms.CharField(
        max_length=200,
        validators=[RegexValidator(regex='^[a-zA-Z0-9\s,.-]+$', message='Address can only contain letters, numbers, spaces, commas, and periods')]
    )
    item_bought_on_credit = forms.CharField(
        max_length=100,
        validators=[RegexValidator(regex='^[a-zA-Z\s]+$', message='Item name must contain only letters and spaces')]
    )
    balance = forms.DecimalField(
        validators=[MinValueValidator(0, message="Balance must be a positive value")]
    )
    date_of_payment = forms.DateField(
        validators=[],
        widget=forms.DateInput(attrs={'type': 'date'}),
        initial=timezone.now
    )
    branch_agent = forms.CharField(
        max_length=100,
        validators=[RegexValidator(regex='^[a-zA-Z ]*$', message='Branch agent name must contain only letters and spaces')]
    )

    class Meta:
        model = Deffered_payments
        fields = ['name', 'amount', 'nin', 'contact', 'address', 'item_bought_on_credit', 'balance', 'date_of_payment', 'branch_agent']





class StockxForm(ModelForm):
    total_quantity = forms.CharField(validators=[numeric_validator])  # Ensure total_quantity is a valid number
    
    class Meta:
        model = Stockx
        fields = '__all__'


class AddForm(ModelForm):
    total_quantity = forms.CharField(validators=[numeric_validator])  # Ensure total_quantity is a valid number
    
    class Meta:
        model = Stockx
        fields = ['total_quantity']
