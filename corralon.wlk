class Producto {
  var stock = 0
  const precioBase = 0

  method stock() = stock

  method precioBase() = precioBase

  method hayStock(cantidad) = stock >= cantidad

  method descontarStock(cantidad) {
    stock = stock - cantidad
  }

  method puedeEntregarse(cantidad, distancia) = self.hayStock(cantidad)

  method costoAdicional(distancia) = 0

  method precioUnitario(distancia) = precioBase + self.costoAdicional(distancia)
}

class Material inherits Producto {
  const costoPorKm = 0

  override method puedeEntregarse(cantidad, distancia) =
    super(cantidad, distancia) && cantidad >= 2

  override method costoAdicional(distancia) = costoPorKm * distancia
}

class Herramienta inherits Producto {
  override method puedeEntregarse(cantidad, distancia) =
    super(cantidad, distancia) && distancia <= 50
}

class HerramientaElectronica inherits Herramienta {
  override method costoAdicional(distancia) = super(distancia) + 500
}

class ItemPedido {
  const producto
  const cantidad = 0

  method producto() = producto

  method cantidad() = cantidad

  method puedeEntregarse(distancia) = producto.puedeEntregarse(cantidad, distancia)

  method precio(distancia) = producto.precioUnitario(distancia) * cantidad

  method entregar() {
    producto.descontarStock(cantidad)
  }
}

class Pedido {
  const distancia = 0
  const items = []

  method distancia() = distancia

  method items() = items

  method agregarItem(producto, cantidad) {
    items.add(new ItemPedido(producto = producto, cantidad = cantidad))
    return self
  }

  method puedeEntregarse() = items.all { item => item.puedeEntregarse(distancia) }

  method precio() = items.sum { item => item.precio(distancia) }

  method confirmarEntrega() {
    items.forEach { item => item.entregar() }
  }
}

class Corralon {
  const pedidosEntregados = []

  method pedidosEntregados() = pedidosEntregados

  method cantidadPedidosEntregados() = pedidosEntregados.size()

  method entregar(pedido) {
    if (!pedido.puedeEntregarse()) {
      self.error("El pedido no puede entregarse")
    }
    pedido.confirmarEntrega()
    pedidosEntregados.add(pedido)
  }
}
