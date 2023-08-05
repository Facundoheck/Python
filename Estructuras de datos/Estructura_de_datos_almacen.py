class Producto:
  def __init__(self,id,descripcion,marca,stock,precio):
    self.id = id
    self.descripcion = descripcion
    self.marca = marca
    self.stock = stock
    self.precio = precio

def agregarProducto(inventario):
  id=int(input('Codigo de producto: '))
  descripcion=input('Descripcion: ')
  marca=input('Marca: ')
  stock=int(input('Cantidad en stock: '))
  precio=float(input('Precio: '))
  prod=Producto(id,descripcion,marca,stock,precio)
  inventario[id]=prod

def actualizarExistencia(inventario):
  id=int(input('Codigo de producto: '))
  cantidad=int(input('Cantidad en stock: '))
  prod=inventario.get(id)
  if prod:
    prod.stock=cantidad
    print('Stock del producuto actualizado con éxito')
  else:  
    print('No existe el producto')

def actualizarPrecio(inventario):
  id=int(input('Codigo de producto: '))
  precio=float(input('Precio de producto: '))
  prod=inventario.get(id)
  if prod:
    prod.precio=precio
    print('Precio del producto actualizado con éxito')
  else:
    print('No existe el producto')

def mostrarInventario(inventario):
  for id,producto in inventario.items():
    print('Codigo:',producto.id)
    print('Descripcion:',producto.descripcion)
    print('Marca:',producto.marca)
    print('Cantidad en stock:',producto.stock)
    print('Precio:',producto.precio)
    print('-'*30)

def main():
  inventario={}
  while True:
    eleccion = str(input("Menu:\n a: Agregar productos\n b: Actualizar existencias\n c: Actualizar precio\n d: Mostrar inventario\n e: Salir\n"))
    if eleccion == 'a':
      agregarProducto(inventario)
    elif eleccion == 'b':
      actualizarExistencia(inventario)
    elif eleccion == 'c':
      actualizarPrecio(inventario)
    elif eleccion == 'd':
      mostrarInventario(inventario)
    elif eleccion == 'e':
      break
    else:
      print('Opcion invalida, intente nuevamente')

main()