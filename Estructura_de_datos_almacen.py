class Producto:
  def __init__(self,id,descripcion,marca,stock,precio):
    self.id = id
    self.descripcion = descripcion
    self.marca = marca
    self.stock = stock
    self.precio = precio

def agregarProducto(inventario):
  id=input('Codigo de producto: ')
  descripcion=input('Descripcion: ')
  marca=input('Marca: ')
  stock=input('Cantidad en stock: ')
  precio=input('Precio: ')
  prod=Producto(id,descripcion,marca,stock,precio)
  inventario[id]=prod

def actualizarExistencia(inventario):
    id=input('Codigo de producto: ')
    cantidad=input('Cantidad en stock: ')
    prod=inventario.get(id)
    if prod:
      prod.stock = cantidad
      print('Stock del producuto actualizado con éxito')
    else:  
      print('No existe el producto')

def actualizarPrecio(inventario):
  id=input('Codigo de producto: ')
  precio=input('Precio de producto: ')
  prod=inventario.get(id)
  if prod:
    prod.precio=precio
    print('Precio del producto actualizado con éxito')
  else:
    print('No existe el producto')

def mostrarInventario(inventario):
    

def main():
  inventario={}
  while True:
    eleccion = input(str("Menu:\n a: Agregar productos\n b: Actualizar existencias\n c: Actualizar precio\n d: Mostrar inventario\n e: Salir\n"))
    if eleccion == 'a':
        agregarProducto(inventario)
        main()
    elif eleccion == 'b':
      actualizarExistencia(inventario)
      main()
    elif eleccion == 'c':
      actualizarPrecio(inventario)
      main()
    elif eleccion == 'd':
      mostrarInventario(inventario)
      main()
    elif eleccion == 'e':
      break

main()