from django import forms
from .models import Auth


class AuthModelFrom(forms.ModelForm):

    class Meta:
        model = Auth

        fields = ['username', 'password']  # 如果要映射全部字段直接使用 __all__
        exclude = []  # 输入不需要映射成表单字段的 model 字段

        # 自定义 model 字段转换表单字段
        field_classes = {  # 定义字段类型，一般会按照 model 的类型自动转换
            'username': forms.CharField,
            'password': forms.CharField,
        }

        labels = {
            'username': '用户名',
            'password': '密码',
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': '请输入用户名'}),
            'password': forms.PasswordInput(render_value=True, attrs={'type': 'password', 'placeholder': '请输入密码'}),
        }

        error_messages = {
            'username': {'required': '用户名不可为空'},
            'password': {'min_length': '不得低于10个字符'}
        }

    submit = forms.CharField(widget=forms.TextInput(attrs={'type': 'submit'}))

    # 验证
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) > 10:
            raise forms.ValidationError('长度不能超过10个字符')

        return username


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", required=True)
    password = forms.CharField(
        label="密码",
        widget=forms.TextInput(attrs={'class': 'test-class', 'id': 'testID', 'type': 'password'}),
        error_messages={'max_length': "用户名不能超过 7 个字符"}
    )
    submit = forms.CharField(widget=forms.TextInput(attrs={'type': 'submit'}))

    # def clean(self):
    #     # username = self.cleaned_data.get('username', '')
    #     password = self.cleaned_data.get('password', '')
    #     # print(username)
    #
    #     # if not username:
    #     #     raise forms.ValidationError('用户名不能为空')
    #
    #     if not password:
    #         raise forms.ValidationError('密码不能为空')
    #
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) > 10:
            raise forms.ValidationError('用户名长度不能超过7')

        return username
