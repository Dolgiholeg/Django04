from django import  forms

class UserformComment(forms.Form):
    name = forms.CharField(max_length=10)#максимальное количество знаков 10
    email = forms.EmailField(required=False)#необезательный
    com = forms.CharField(widget=forms.Textarea)#разрешено изменение на большое поле

class UserformErrors(forms.Form):
    name = forms.CharField(error_messages={'required':'надо заполнить'})
    num = forms.IntegerField(error_messages={'invalid':'надо целое число','required':'надо заполнить'})
    agree = forms.BooleanField(error_messages={'required':'поставьте галочку'})

from django.core.validators import ValidationError, RegexValidator, validate_email

def p1(value):
    if value[0] != 'A':
        raise forms.ValidationError('должно начинаться на А')

def p2(value):
    if value[-1] != 'Z':
        raise forms.ValidationError('должно заканчиваться на Z')


class UserformValidator(forms.Form):
    name = forms.CharField(error_messages={'required':'надо заполнить'})
    code = forms.CharField(validators=[p1, p2])
    tel = forms.CharField(validators=[RegexValidator('[+7][0-9]{9}', message='неправильный номер телефона')])

def p3(value):
    if value[0].istitle() != True:
        raise forms.ValidationError('слово должно начинаться с прописной буквы')

def p4(value):
    if value.isalpha() !=True:
        raise forms.ValidationError('допускаются только буквенные символы')

class Water(forms.Form):
    name = forms.CharField(label='Ваше имя', validators=[p3, p4])
    surname = forms.CharField(label='Ваша фамилия', validators=[p3, p4])
    email = forms.EmailField(label='Ваш электронный адрес', error_messages={'required': 'неправильный электронный адрес'})
    tel = forms.CharField(label='Номер Вашего контактного телефона', validators=[RegexValidator('[+7][0-9]{9}', message='неправильный номер телефона')])
    adres = forms.CharField(label='Ваш адрес', error_messages={'required':'надо заполнить'})
    kol = (('1 месяц', '1 месяц'), ('3 месяца', '3 месяца'), ('6 месяцев', '6 месяцев'), ('12 месяцев', '12 месяцев'))
    period = forms.TypedChoiceField(label='Количество месяцев доставки', choices=kol, error_messages={'required':'надо заполнить'})
    vol = (('5 литров', '5 литров'), ('10 литров', '10 литров'), ('15 литров', '15 литров'))
    volume = forms.TypedChoiceField(label='Объём воды', choices=vol, error_messages={'required':'надо заполнить'})


