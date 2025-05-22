'''
Стилизувати сторінку логін з уроку
'''

'''
login.html

{% extends '_base.html' %}

{% block title %}
  Login
{% endblock %}

{% block content %}
    <div class="container">
        <h1>Login</h1>
        <form action="" method="post">
            {% csrf_token %}
            <div class="mb-3">
                <label for="exampleInputEmail1" class="form-label">Email address</label>
                {{ form.email }}
                <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
                <label for="exampleInputPassword1" class="form-label">Password</label>
                {{ form.password }}
            </div>
            <div class="mb-3">
                <label class="form-check-label" for="exampleCheck1">Remember me: </label>
                {{ form.remember_me }}
            </div>
            <div>
                <button type="submit" class="btn btn-primary">Login</button>
            </div>

        </form>
    </div>
{% endblock %}
'''

# Угу))