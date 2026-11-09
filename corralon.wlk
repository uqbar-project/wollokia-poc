class Pedido {
  const distancia
  const items

  method puedeEntregarse() {
    return items.all({ item => item.alcanza(self) })
  }
}

class Item {
  const cantidad
  const producto

  method alcanza(pedido) {
    return producto.tieneStock(cantidad, pedido)
  }
}

class Producto {
  const stock

  method tieneStock(cantidad, pedido) {
    return stock >= cantidad
  }
}

class Herramienta inherits Producto {
}

class Material inherits Producto {
}
