from django import forms
from .models import customer,staff,Booking,Room


class CustRegForm(forms.ModelForm):
    class Meta:
        model = customer  

        fields = ('name','age','email','aadhaar','phone','password')
        
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'aadhaar':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }  

class staffRegForm(forms.ModelForm):
    class Meta:
        model = staff  

        fields = ('name','age','email','aadhaar','password','phone')
        
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'aadhaar':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }   
  

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer','room', 'check_in_date', 'check_out_date','approval']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }     

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'capacity', 'price_per_night', 'available']                    
