from django.shortcuts import render
from userreview.models import Review


# this is the feedback form page for users...
def review(request, username, password):
    n = ''
    cname = ''
    bool = False
    url = '/dashboard/?name={}&pw={}'.format(username, password)
    data = {'un': username, 'n': n, 'cname': cname, 'url': url, 'bool': bool}

    if request.method == "POST":
        name = request.POST.get('username')
        review = request.POST.get('review')
        ratings = request.POST.get('ratings')
        data = Review(username=name, user_review=review, ratings=ratings)
        data.save()
        n = 'your review is added successfully'
        cname = 'alert-success'
        url = '/dashboard/?name={}&pw={}'.format(username, password)
        bool = True
        data = {'un': username, 'n': n,
                'cname': cname, 'url': url, 'bool': bool}

    return render(request, 'reviewform.html', data)

# this is the blog page here we display the review of our customers ....


def blog(request):
    data = Review.objects.all()
    datamain = {'data': data}
    return render(request, 'blogs.html', datamain)
