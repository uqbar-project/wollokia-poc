class Pedido {
  const distancia
  const items

  method puedeEntregarse() {
  }
}

class Item {
  const cantidad
  const producto

  method alcanza() {
  }
}

class Producto {
  const stock

  method tieneStock(cantidad) {
  }
}
