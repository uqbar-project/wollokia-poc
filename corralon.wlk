class Pedido {
  const distancia
  const items

  method puedeEntregarse() {
    return items.all({ item => item.alcanza() })
  }
}

class Item {
  const cantidad
  const producto

  method alcanza() {
    return producto.tieneStock(cantidad)
  }
}

class Producto {
  const stock

  method tieneStock(cantidad) {
    return stock >= cantidad
  }
}
