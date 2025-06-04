from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

from .models import Kit, Drug
from .forms import DrugForm, KitForm


from django.core.paginator import Paginator
from .models import DrugTake

@login_required
def dashboard(request):
    kits = Kit.objects.filter(user=request.user)
    show_form = request.GET.get('add_kit') == '1'
    form = KitForm() if show_form else None

    if request.method == 'POST':
        form = KitForm(request.POST)
        if form.is_valid():
            kit = form.save(commit=False)
            kit.user = request.user
            kit.save()
            return redirect('dashboard')

    # Sorting and paginating DrugTake records
    take_sort = request.GET.get('take_sort', 'taken_at')
    take_page = request.GET.get('take_page', 1)

    if take_sort == 'drug':
        takes = DrugTake.objects.filter(user=request.user).select_related('drug').order_by('drug__name')
    else:
        takes = DrugTake.objects.filter(user=request.user).select_related('drug').order_by('-taken_at')

    paginator = Paginator(takes, 5)
    take_page_obj = paginator.get_page(take_page)

    return render(request, 'app_med_kit/dashboard.html', {
        'kits': kits,
        'form': form,
        'show_form': show_form,
        'take_page_obj': take_page_obj,
        'take_sort': take_sort,
    })

from datetime import date

from django.urls import reverse
@login_required
def manage_kit(request, kit_id):
    # 1) Fetch the Kit (ensuring it belongs to the logged‐in user)
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)

    # 2) Determine sort order (default = 'name')
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by == 'expiration_date':
        # Order by expiration_date ascending
        drug_list = kit.drugs.all().order_by('expiration_date')
    else:
        # Default: order by name (alphabetical)
        drug_list = kit.drugs.all().order_by('name')

    # 3) Paginate the results, 5 drugs per page
    paginator = Paginator(drug_list, 5)
    page_number = request.GET.get('page')  # `None` if not provided → first page
    page_obj = paginator.get_page(page_number)

    # 4) “Add Drug” form logic (unchanged)
    show_form = request.GET.get('add_drug') == '1'
    form = DrugForm() if show_form else None

    if request.method == 'POST':
        # If user is submitting the “Add Drug” form (POST)
        form = DrugForm(request.POST)
        if form.is_valid():
            drug = form.save(commit=False)
            drug.kit = kit
            drug.save()
            # After adding, redirect back (to page=1, preserve sort_by)
            return redirect(f"{reverse('manage_kit', args=[kit.id])}?sort_by=name")
    # 5) Render template with context
    return render(request, 'app_med_kit/manage_kit.html', {
        'kit': kit,
        'page_obj': page_obj,
        'sort_by': sort_by,
        'form': form,
        'show_form': show_form,
        'today': date.today(),  # ← add this line
    })

@require_POST
@login_required
def edit_drug(request, kit_id, drug_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drug = get_object_or_404(Drug, id=drug_id, kit=kit)
    form = DrugForm(request.POST, instance=drug)
    if form.is_valid():
        form.save()
    # After editing, redirect back to the same manage_kit page, preserving sort_by & page=1
    sort_by = request.GET.get('sort_by', 'name')
    return redirect(f"{reverse('manage_kit', args=[kit.id])}?sort_by=name")


from .models import DrugTake

@require_POST
@login_required
def take_drug(request, kit_id, drug_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drug = get_object_or_404(Drug, id=drug_id, kit=kit)

    if drug.number > 0:
        drug.number -= 1
        drug.save()
        DrugTake.objects.create(user=request.user, drug=drug)

    sort_by = request.GET.get('sort_by', 'name')
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('manage_kit', args=[kit.id])}?sort_by={sort_by}&page={page}")


@require_POST
@login_required
def delete_drug(request, kit_id, drug_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    drug = get_object_or_404(Drug, id=drug_id, kit=kit)
    drug.delete()
    sort_by = request.GET.get('sort_by', 'name')
    page = request.GET.get('page', '1')
    return redirect(f"{reverse('manage_kit', args=[kit.id])}?sort_by=name")

from django.views.decorators.http import require_POST

@require_POST
@login_required
def delete_kit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id, user=request.user)
    kit.delete()
    return redirect('dashboard')