#Email:dazhuang_python@sina.com

#引入wtforms对request参数进行校验
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


#继承wtforms的Form
class SearchForm(Form):
    #validators使用列表是因为可以创建多个校验器
    q = StringField(validators=[Length(min=1,max=30)])
    #如果不传page，则为默认值1
    page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)