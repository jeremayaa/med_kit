from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Kit, Drug
from .forms import KitForm

@login_required
def dashboard(request):
    kits = Kit.objects.filter(user=request.user)
    show_form = request.GET.get('add_kit') == '1'  # check URL param
    form = KitForm() if show_form else None

    if request.method == 'POST':
        form = KitForm(request.POST)
        if form.is_valid():
            kit = form.save(commit=False)
            kit.user = request.user
            kit.save()
            return redirect('dashboard')  # clean reload with form hidden

    return render(request, 'app_med_kit/dashboard.html', {
        'kits': kits,
        'form': form,
        'show_form': show_form,
    })

from django.shortcuts import get_object_or_404
from .forms import DrugForm

@login_required
def manage_kit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drugs = kit.drugs.all()
    show_form = request.GET.get('add_drug') == '1'
    form = DrugForm() if show_form else None

    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            drug = form.save(commit=False)
            drug.kit = kit
            drug.save()
            return redirect('manage_kit', kit_id=kit.id)

    return render(request, 'app_med_kit/manage_kit.html', {
        'kit': kit,
        'drugs': drugs,
        'form': form,
        'show_form': show_form,
    })

from django.views.decorators.http import require_POST

@require_POST
@login_required
def edit_drug(request, kit_id, drug_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drug = get_object_or_404(Drug, id=drug_id, kit=kit)

    form = DrugForm(request.POST, instance=drug)
    if form.is_valid():
        form.save()

    return redirect('manage_kit', kit_id=kit.id)


@require_POST
@login_required
def take_drug(request, kit_id, drug_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drug = get_object_or_404(Drug, id=drug_id, kit=kit)

    if drug.number > 0:
        drug.number -= 1
        drug.save()

    return redirect('manage_kit', kit_id=kit.id)


@require_POST
@login_required
def delete_drug(request, kit_id, drug_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drug = get_object_or_404(Drug, id=drug_id, kit=kit)
    drug.delete()
    return redirect('manage_kit', kit_id=kit.id)