from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,PersonalInformation

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=30, required=True, help_text='Required', widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Email Address'
    }))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Username'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'First Name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Last Name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Email Address'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-user',
            'placeholder': 'Repeat Password'
        })

class PersonalInformationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    WARD_CHOICES = [
        ('Bunyala east', 'Bunyala East'),
        ('Bunyala central', 'Bunyala Central'),
        ('Bunyala west', 'Bunyala West'),
        ('Shinoyi shikomary', 'Shinoyi Shikomari'),
    ]

    VILLAGE_CHOICES = [
        ('Muregu', 'Muregu'),
        ('Musaga', 'Musaga'),
        ('Makhima', 'Makhima'),
        ('Lutaso', 'Lutaso'),
        ('Namirama', 'Namirama'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    ward = forms.ChoiceField(choices=WARD_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    village = forms.ChoiceField(choices=VILLAGE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = PersonalInformation
        fields = ['gender', 'date_of_birth', 'id_number', 'phone_number', 'ward', 'village']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
        }

class InstitutionInformationForm(forms.ModelForm):
    INSTITUTION_CATEGORY = [
            ('University', 'University'),
            ('TVET', 'TVET'),
            ('KMTC', 'KMTC'),
            ('County Polytechnic', 'County Polytechnic'),
    ]
        
    MODE_OF_STUDY = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
    ]
    COURSE_DURATION = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
    ]

    institution_category = forms.ChoiceField(choices=INSTITUTION_CATEGORY, widget=forms.Select(attrs={'class': 'form-control'}))
    mode_of_study = forms.ChoiceField(choices=MODE_OF_STUDY, widget=forms.Select(attrs={'class': 'form-control'}))
    year_of_study = forms.ChoiceField(choices=COURSE_DURATION, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = PersonalInformation
        fields = ['gender', 'date_of_birth', 'id_number', 'phone_number', 'ward', 'village']
        widgets = {
            'institution_name': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'admission_no': forms.TextInput(attrs={'type': 'tel', 'class': 'form-control'}),
            'course': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'year_of_study': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
            'year_of_completion': forms.TextInput(attrs={'type': 'number', 'class': 'form-control'}),
        }