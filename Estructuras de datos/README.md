Programa para llevar el inventario de un almacén. El programa permitirá agregar productos al inventario, actualizar las existencias y precios de productos existentes y mostrar el inventario completo.
Cada producto tendrá un código de identificación único, una descripción, una marca, una cantidad en stock y un precio.
El usuario puede agregar productos, actualizar sus existencias y precio y ver el inventario completo mientras no elija salir del programa.
Para ello, se le solicita implemente un menú que le permita elegir entre las diferentes operaciones a realizar. El menú podría verse así:
````
Menú:
a.	Agregar producto
b.	Actualizar existencias
c.	Actualizar precio
d.	Mostrar inventario
e.	Salir
````
### Explicación de cada una de las opciones del menú:

a. La opción Agregar producto debe invocar a una función de nombre AgregarProducto que permita al usuario agregar un nuevo producto al inventario.
b. La opción Actualizar existencias debe invocar a una función de nombre actualizarExistencias que permita al usuario actualizar las existencias de un producto existente en el inventario. El usuario ingresa el código del producto y la nueva cantidad en stock. Si el producto existe en el inventario, se actualizan sus existencias.
c. La opción Actualizar precio debe invocar a una función de nombre actualizarPrecio que permita al usuario actualizar el precio de un producto existente en el inventario. El usuario ingresa el código del producto y el nuevo precio. Si el producto existe en el inventario, se actualiza su precio.
d. La opción Mostrar inventario que invoque a una función de nombre mostrarInventario que imprima en pantalla el inventario completo, mostrando el código, la descripción, la marca, la cantidad de stock y el precio de cada producto en el inventario.
El programa se implementará en una función llamada Main. El programa presentara el menú con todas las opciones recién descriptas y dependiendo de la opción elegida invocara a la función necesaria. El programa terminara su ejecución solo cuando se elija la opción de salir.
