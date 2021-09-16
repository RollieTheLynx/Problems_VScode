from django import forms


class RegexForm(forms.Form):
    input_text = forms.CharField(
        label='Your text',
        max_length=1800,
        widget=forms.Textarea(attrs={"cols": 80}),
        initial="""wtgbbrtbertn 56 u4h4 67h 46h36 67h 47h 47h 56 hh@ergrt.ru
w5rg 54g 54g 36 365 5g54@4gt.lib h3656h 6yh ffferg[at]erg254g.t4""")


class GraphsForm(forms.Form):
    amplitude = forms.DecimalField(label='Амплитуда:', widget=forms.NumberInput(attrs={
    'type': 'range',
    'step': '0.1',
    'min': '0.1',
    'max': '30',
    }))
    period = forms.DecimalField(label='Период:', widget=forms.NumberInput(attrs={
    'type': 'range',
    'step': '0.1',
    'min': '0.1',
    'max': '30',
    }))
    ph_shift = forms.DecimalField(label='Смещение фазы:', widget=forms.NumberInput(attrs={
    'type': 'range',
    'step': '0.1',
    'min': '-5.0',
    'max': '5.0',
    }))
    ver_shift = forms.DecimalField(label='Вертикальное смещение:', widget=forms.NumberInput(attrs={
    'type': 'range',
    'step': '0.1',
    'min': '-5.0',
    'max': '5.0',
    }))
