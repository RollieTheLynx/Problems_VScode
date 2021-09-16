from django.shortcuts import render, redirect
import re
from .forms import RegexForm, GraphsForm
import requests
import json
import os
from django.conf import settings
import base64
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "mainpage.html", {})


def css_view(request, *args, **kwargs):
    context = {}
    return render(request, "css.html", context)


def regex_view(request, *args, **kwargs):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegexForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            results = re.findall(r'\S*@\S*', form.cleaned_data["input_text"])
            context = {'results': results, 'form': form}
            return render(request, "regex.html", context)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegexForm()
        return render(request, 'regex.html', {'form': form})


def chuck_view(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            api_request = requests.get("http://api.icndb.com/jokes/random")
            joke = json.loads(api_request.content)
        except Exception:
            joke = "Error..."
        return render(request, 'chuck_norris.html',
                      {'text': joke["value"]["joke"]})
    else:
        return render(request, 'chuck_norris.html', {'text': ""})


def estonia_view(request, *args, **kwargs):
    context = {}
    if request.user_agent.is_mobile:
        return render(request, "estonia_cluster.html", context)
    else:
        return render(request, "estonia.html", context)


def germany_view(request, *args, **kwargs):
    context = {}
    if request.user_agent.is_mobile:
        return render(request, "germany_cluster.html", context)
    else:
        return render(request, "germany.html", context)


def russia_view(request, *args, **kwargs):
    context = {}
    if request.user_agent.is_mobile:
        return render(request, "russia_cluster.html", context)
    else:
        return render(request, "russia.html", context)


def library_view(request, *args, **kwargs):
    # #преобразовываем датасет в формат {"игра": {"тайтл" : ""}}
    # with open('static/imperial_library_20200626b.json') as f:
    #     data = json.load(f)

    # book_text = data['https://www.imperial-library.info/content/dying-mans-last-words']
    # games = ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim', 'TES: Online']
    # book_db = {}

    # for game in games:
    #     books_in_game = {}
    #     for key in data:
    #         if game in data[key]["game"]:
    #             books_in_game[data[key]["title"]] = ""
    #     book_db[game] = books_in_game
    #     print(book_db)
    # with open('short_library.json', 'w') as f:
    #     json.dump(book_db, f)

    # вручную удалить символы \"
    with open(os.path.join(settings.BASE_DIR, 'pages/static/pages/imperial_library2.json')) as f:
        short_library = json.load(f)
    selected_game = request.GET.get('game')
    selected_book = request.GET.get('book')

    with open(os.path.join(settings.BASE_DIR, 'pages/static/pages/imperial_library_20200626b.json')) as orig:
        text_db = json.load(orig)

    if (selected_game is None) or (selected_book is None):
        book_text = ""
    else:
        for book in text_db:
            if selected_game in text_db[book]["game"] and selected_book == text_db[book]["title"]:
                book_text = text_db[book]["text"]
                break

    context = {'short_library': short_library, 'book_text': book_text}
    return render(request, "imperial_library.html", context)


def graphs_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = GraphsForm(request.POST)
        if form.is_valid():
            return redirect(f'/graphs?amplitude={form.cleaned_data["amplitude"]}&period={form.cleaned_data["period"]}&ph_shift={form.cleaned_data["ph_shift"]}&ver_shift={form.cleaned_data["ver_shift"]}')
        else:
            print("Form invalid")

    # if a GET (or any other method) we'll create a blank form
    else:
        a = request.GET.get('amplitude', 1)  # читаем url arguments, даем значения по умолчанию, если их нет
        b = request.GET.get('period', 1)
        c = request.GET.get('ph_shift', 0)
        d = request.GET.get('ver_shift', 0)
        a, b, c, d = float(a), float(b), float(c), float(d)
        fig = Figure()   # Generate the figure **without using pyplot**
        ax = fig.subplots()
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.set_title('a sine wave')
        x = np.arange(0, 10, 0.01)  # start,stop,step
        y = a*np.sin(b*(x+c))+d
        ax.plot(x, y)
        ax.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        buf = BytesIO()  # Save it to a temporary buffer.
        fig.savefig(buf, format="png")
        # Embed the result in the html output.
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        form = GraphsForm(auto_id=True, initial={'amplitude': a, 'period': b, 'ph_shift': c, 'ver_shift': d})
        context = {'data': data, 'form': form}
        return render(request, "graphs.html", context)
