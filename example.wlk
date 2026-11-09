class Pedido {
  const distancia
  const items

  method puedeEntregarse() = items.all({ item => item.alcanza() })
}

class Item {
  const cantidad
  const producto

  method alcanza() = producto.tieneStock(cantidad)
}

class Producto {
  const descripcion
  var property stock

  method tieneStock(cantidad) = cantidad <= stock
}
