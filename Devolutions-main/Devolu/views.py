from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#from Devolu.forms import FormRegistro
from Devolu.models import Cliente, Devolucion, Producto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

def registrarse(request):
    cli_username = request.POST['txt_username']
    cli_email = request.POST['txt_email']
    cli_password = request.POST['txt_contrasena']

    user = User.objects.create_user(cli_username, cli_email, cli_password)
    user.save()
    grupo, created = Group.objects.get_or_create(name ='admin')
    user.groups.add(grupo)

    return redirect('/inicio/login')
    
def registrar(request):
    if request.user.is_authenticated:
        redirect('/menu/')
    return render(request,'registrarse.html')

def crearVend(request):
    v_username = request.POST['txt_usernamev']
    v_email = request.POST['txt_emailv']
    v_password = request.POST['txt_password']

    use = User.objects.create_user(v_username,v_email,v_password)
    use.save
    
@login_required
def listadev(request):
    devolucion = Devolucion.objects.all()
    data = {'devolucion':devolucion}
    return render(request,'listarDevolucion.html', data)

@login_required
def registrard(request):
    return render(request,'FormularioDev.html')    

@login_required
def registrardevo(request):
    dev_producto = request.POST['sel_producto']
    dev_cliente = request.POST['sel_cliente']
    dev_distribuidor = request.POST['txt_distribuidor']
    dev_nombre_vendedor = request.POST['txt_nombrevendedor']
    dev_comentario = request.POST['txt_comentario']
 

    devolucion = Devolucion(Producto = dev_producto, Cliente=dev_cliente,distribuidor=dev_distribuidor,nombre_vendedor=dev_nombre_vendedor, comentario = dev_comentario )
    
    devolucion.save()
    

    return redirect('/')

@login_required
def eliminardev(request, id):
    elemidev = Devolucion.objects.get(id=id)
    elemidev.delete()

    return redirect(registrardevo)

@login_required
def devoluActualizar(request,id):
    dev = Devolucion.objects.get(id=id)
    return render(request,'Actualizardev.html',{"dev":dev})    

@login_required
def editarDev(request):
    dev_producto = request.POST['sel_producto']
    dev_cliente = request.POST['sel_cliente']
    dev_distribuidor = request.POST['txt_distribuidor']
    dev_nombre_vendedor = request.POST['txt_nombrevendedor']
    dev_comentario = request.POST['txt_comentario']
 
    devolu = Devolucion.objects.get(Cliente = dev_cliente)
    
    devolu.Producto = dev_producto
    devolu.nombre_vendedor = dev_nombre_vendedor
    devolu.Distribuidor = dev_distribuidor
    devolu.comentario = dev_comentario

    devolu.save()
    return redirect('/')


@login_required
def menu(request):
    return render(request,'menu.html')  

@login_required
def listaclient(request):
    cliente = Cliente.objects.all()
    data = {'cliente':cliente}
    return render(request,'listarClient.html', data)

@login_required
def registrarc(request):
    return render(request,'FormularioClient.html')

@login_required
def registrarclient(request):
    client_rut = request.POST['txt_rut']
    client_nombre = request.POST['txt_nombre']
  
    cliente = Cliente(rut = client_rut, nombre = client_nombre)
    cliente.save()
    return redirect('/menu/')

@login_required
def eliminarClient(request, id):
    elemiclient = Cliente.objects.get(id=id)
    elemiclient.delete()

    return redirect('/')

@login_required
def clientActualizar(request,id):
    client = Cliente.objects.get(id=id)
    return render(request,'ActualizarClient.html',{"client":client})    

@login_required
def editarClient(request):
    client_rut = request.POST['txt_rut']
    client_nombre = request.POST['txt_nombre']

    client = Cliente.objects.get(rut = client_rut)
    client.nombre = client_nombre


    client.save()
    return redirect('/')




@login_required
def listaproduct(request):
    producto = Producto.objects.all()
    data = {'producto':producto}
    return render(request,'listarProduct.html', data)

@login_required
def registrarp(request):
    return render(request,'FormularioProduct.html')

@login_required
def registrarproduct(request):
    product_nombre = request.POST['txt_producto']
    product_cantidad = request.POST['txt_cantidad']
    product_costo = request.POST['txt_costo']
    producto = Producto(nomproduct = product_nombre, cantidad = product_cantidad, costo = product_costo)
    producto.save()
    return redirect(listaproduct)

@login_required
def eliminarProduct(request, id):
    elemiproduct = Producto.objects.get(id=id)
    elemiproduct.delete()
    return redirect(request,'listarProduct.html')

@login_required
def productActualizar(request,id):
    product = Producto.objects.get(id=id)
    return render(request,'ActualizarProduct.html',{"product":product})    

@login_required
def editarProduct(request):
    product_nombre = request.POST['txt_producto']
    product_cantidad = request.POST['txt_cantidad']
    product_costo = request.POST['txt_costo']

    product = Producto.objects.get(nomproduct = product_nombre)
    product.nomproduct =product_nombre
    product.cantidad = product_cantidad
    product.costo = product_costo

    product.save()
    return redirect('/')