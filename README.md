1. 프로젝트 구조

   ```bash
   $ django-admin startproject django_pjt2
   $ python manage.py startapp community
   ```

   project와 application 디렉토리를 구성하고 기타 기본 설정을 진행한다.

   * settings.py

   ```python
   STATIC_URL = '/static/'
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'static')
   ]
   ```

   `static/`폴더를 활용하기 위해 경로를 settings.py에서 설정해주어야 한다. 

   

2. Model

   ```python
   from django.db import models
   from django.core.validators import MinValueValidator, MaxValueValidator
   
   # Create your models here.
   class Review(models.Model):
       title = models.CharField(max_length=100)
       movie_title = models.CharField(max_length=30)
       rank = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10)])
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

   * 이 때 평점을 0부터 10까지만 입력할 수 있도록 min, max value를 설정해준다.

     * `MaxValueValidator`, `MinValueValidator`

     

3. Form

   ```python
   from django import forms
   from .models import Review
   
   class ReviewForm(forms.ModelForm):
       class Meta:
           model = Review
           fields = '__all__'
   ```

   

4. Admin

   ```bash
   $ python manage.py createsuperuser
   ```

   admin.py

   ```python
   from django.contrib import admin
   
   # Register your models here.
   from .models import Review
   admin.site.register(Review)
   ```

   

5. URL

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'community'
   
   urlpatterns = [
       path('', views.review_list, name='index'),
       path('create/', views.create_review, name='create'),
       path('<int:review_pk>/', views.review_detail, name='detail'),
       path('<int:review_pk>/update/', views.update_review, name='update'),
       path('<int:review_pk>/delete/', views.delete_review, name='delete'),
   ]
   ```

   

6. View & Template

   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>MOVIE REVIEW</title>
       <!--<link rel="stylesheet" href="{% static 'articles/stylesheets/style.css' %}">-->
       <link rel="stylesheet" href="{% static 'bootstrap/bootstrap.min.css' %}">
       {% block css %}
       {% endblock %}
   </head>
   ```

   * Bootstrap을 활용하여 스타일링할 때 `static/` 폴더를 활용하기 위해 `{% load static %}`를 써주어야 한다.



​		form.html

```html
{% extends 'base.html' %}

{% block body %}
    {% if request.resolver_match.url_name == 'create' %}
        <h2 class='d-flex justify-content-center my-3 font-weight-bold'>새 글쓰기</h2>
    {% else %}
        <h2 class='d-flex justify-content-center my-3 font-weight-bold'>수정하기</h2>
    {% endif %}

    <!--<form action="" method="POST">-->
    <!--    {% csrf_token %}-->
    <!--    {{ form.as_ul }}-->
    <!--    <input type="submit" value="제출">-->
    <!--</form>-->

    <!--<form action="" method="POST">-->
    <!--    {% csrf_token %}-->
    <!--    {% for field in form %}-->
    <!--        <div class="fieldWrapper">-->
    <!--            {{ field.errors }}-->
    <!--            {{ field.label_tag }} <br> {{ field }}-->
    <!--            {% if field.help_text %}-->
    <!--            <p class="help">{{ field.help_text|safe }}</p>-->
    <!--            {% endif %}-->
    <!--        </div>-->
    <!--    {% endfor %}-->
    <!--    <input type="submit" value="제출">-->
    <!--</form>-->

    <form method="post" novalidate>
      {% csrf_token %}

      {{ form.non_field_errors }}

      {% for hidden_field in form.hidden_fields %}
        {{ hidden_field.errors }}
        {{ hidden_field }}
      {% endfor %}

      <table border="1" class='mx-auto'>
        {% for field in form.visible_fields %}
          <tr>
            <th>{{ field.label_tag }}</th>
            <td>
              {{ field.errors }}
              {{ field }}
              {{ field.help_text }}
            </td>
          </tr>
        {% endfor %}
      </table>

      <button class='btn btn-secondary my-3 d-flex justify-content-center mx-auto' type="submit">Submit</button>
    </form>
{% endblock %}
```

* form 형식의 데이터를 가지고 폼 디자인을 할 때 많이 어려웠습니다. 그래서 인터넷 검색을 통해 원하는 디자인의 코드를 가져와 구성했습니다.

