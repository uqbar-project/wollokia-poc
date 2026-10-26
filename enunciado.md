# Sistema de gestión de pedidos para el corralón **Armando Paredes**

El corralón *Armando Paredes* vende distintos tipos de productos utilizados en la construcción. Suele recibir
pedidos para hacer entregas a domicilio. Este sistema sólo trata pedidos a domicilio, dejando fuera de su
alcance cualquier otro tipo de pedido; por lo tanto, se utiliza **"Pedido"** como sinónimo de **"Pedido a domicilio"**.

## Requerimientos

Los requerimientos principales del sistema son:
1. Saber si un pedido puede entregarse o no, para lo cual se consultará el stock de los productos solicitados
   y algunas otras condiciones que se detallarán a continuación.
2. Registrar la entrega de un pedido: lo que implica descontar del stock los productos solicitados
   y dejar el pedido registrado junto al resto de los pedidos entregados.
3. Saber el precio de un pedido.

### Pedidos

De un pedido se conoce la distancia al punto de entrega y una serie de **items de pedido**.
Un item de pedido relaciona una cantidad con un producto que se está solicitando.  
Por ejemplo, para el pedido:

```
    Entregar a 35 km:
    - 2 metros cúbicos de arena
    - 3 martillos
    - 1 soldadora
```

Existen 3 items:
- un item para indicar 2 de arena  
- un item para indicar 3 de martillos  
- un item para indicar 1 de soldadoras  

**NOTA**: Las unidades no se modelan. Es decir, no interesa si el “2” representa metros cúbicos o unidades.


## Requerimiento 1: Saber si se puede entregar un pedido

Para saber si un **pedido** puede entregarse, es necesario que puedan cumplirse las condiciones para **todos** los items que lo componen.  
Para que un **item** pueda ser entregado, hay que asegurarse de que haya suficiente stock del producto solicitado.

Por ejemplo: si la cantidad de martillos en stock es 5, un item que represente 3 martillos
podrá ser entregado, pero uno que indique 7 no, haciendo que el pedido entero no pueda entregarse.  

**Recomendamos modelar el stock como un atributo numérico del producto.**

**NOTA:** Se asume que un pedido no tendrá más de un item para el mismo producto. No se debe validar este caso!

**Además del stock**, hay que considerar lo siguiente:

- Los productos que son **Herramientas** pueden entregarse sólo si la distancia del pedido es de **hasta 50 km**.  
  En el ejemplo, los martillos y la soldadora son herramientas. No tendrían problema con los 35 km, pero
  los mismos items en un pedido de 70 km harían que el pedido no pueda entregarse.

- Los productos que son **Materiales** (como arena, piedra, etc.) sólo pueden entregarse si la cantidad solicitada es **2 o más**.  
  En el ejemplo, la arena puede entregarse, pero si se tratara de solo 1 ya no.


## Requerimiento 2: Entrega de un pedido

Cuando se realiza la entrega:

- Es importante que el sistema verifique que se cumplan las condiciones mencionadas anteriormente.  
- El stock de cada producto se descuenta según la cantidad indicada en el item.  
- Se guarda el pedido en algún lugar del sistema donde se almacenan todos los pedidos entregados.  

Por lo tanto, aquí estamos hablando de dos requerimientos:
- Registrar la entrega de un pedido.  
- Conocer todos los pedidos entregados.


## Requerimiento 3: Precio de un pedido

El precio total de un pedido es la suma de los precios de sus items.  
El precio de un item se calcula multiplicando el **precio del producto** por la **cantidad solicitada**, más los costos adicionales según corresponda.

Todos los productos tienen un **precio base**, que se indica para cada producto.
Los diferentes productos pueden tener costos adicionales que se suman al precio base:

- Los **materiales** tienen un costo extra por cada kilómetro de transporte.  
  El valor por kilómetro se indica para cada producto.  
  Por ejemplo, si para la arena se cobra 3 pesos por kilómetro y el precio base es 100, entonces el item del ejemplo  
  (2 de arena, a 35 km) vale:  
  `2 * (100 + 3 * 35) = 410`.

- Las **herramientas** no tienen costo extra.  
  Si el precio de cada martillo es 50, el item de 3 martillos vale:  
  `3 * 50 = 150`.

- Las **herramientas electrónicas** son herramientas con un costo adicional de **500 pesos** por garantía de transporte.  
  En el ejemplo, la soldadora es una herramienta electrónica, por lo que si su precio base es 1000, el item vale:  
  `1 * (1000 + 500) = 1500`.


