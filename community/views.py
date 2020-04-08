from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()[::-1]
    context = {
        'reviews' : reviews
    }
    return render(request, 'community/review_list.html', context)

def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form
    }
    return render(request, 'community/form.html', context)

def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    context = {
        'review' : review
    }
    return render(request, 'community/review_detail.html', context)

def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'community/form.html', context)

@require_POST
def delete_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return redirect('community:index')