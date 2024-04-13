import pandas as pd
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, AddRecordForm, UploadExcel, AvatarForm
from .models import Record


def homepage(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Entrando al CRM')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'homepage.html', {'records': records})


def login_page(request):
    pass


def logout_page(request):
    logout(request)
    messages.success(request, 'Ahora estás saliendo del CRM...')
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Usuario registrado con éxito')
                return redirect('home')
        else:
            messages.error(request, 'Algo está mal, reinténtalo')
            form = CustomUserCreationForm(request.POST)
            return render(request, 'register.html', {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {"form": form})


def customer_page(request, pk):
    if request.user.is_authenticated:
        customer_id = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer': customer_id})
    else:
        messages.error(request, 'Debes iniciar sesión para ver datos del CRM')
        return redirect('home')


def delete_customer_page(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, 'Registro eliminado exitosamente')
        return redirect('home')
    else:
        messages.error(request, 'Debes iniciar sesión para eliminar registros')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                record = form.save(commit=False)
                record.user = request.user
                record.save()
                messages.success(request, 'Registro agregado exitosamente')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error('Debes iniciar sesión para ver datos del CRM')
        return redirect('home')


def edit_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Registro actualizado exitosamente')
                return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, 'Debes iniciar sesión para editar registros')
        return redirect('home')


def excel_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UploadExcel(request.POST, request.FILES)
            if form.is_valid():
                excel_file = request.FILES['excel_file']
                data_frame = pd.read_excel(excel_file.read(), engine='openpyxl')
                file = request.FILES['file']
                for index, row in data_frame.iterrows():
                    record = Record(
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        email=row['Email'],
                        phone_number=row['Phone Number'],
                        city=row['City'],
                        state=row['State'],
                        rut=row[('rut' or 'RUT')],
                        user=request.user
                    )
                    record.save()
                messages.success(request, 'Archivo cargado exitosamente')
                return redirect('home')
        else:
            form = UploadExcel()
    return render(request, 'excel_upload.html', {'form': form})


def avatar_upload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AvatarForm(request.POST, request.FILES)
            if form.is_valid():
                record = Record.objects.get(user=request.user)
                record.avatar = form.cleaned_data.get('avatar')
                record.save()
                messages.success(request, 'Avatar actualizado exitosamente')
                return redirect('home')
        else:
            form = AvatarForm()
        return render(request, 'register.html', {'form': form})
    else:
        messages.error(request, 'Debes iniciar sesión para subir un avatar')
        return redirect('home')
