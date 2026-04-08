FLUJOS CONVERSACIONALES
--------------------------

Para hosteleria lo montaria con el flujo:

* Hola  < somos (nombre restaurante), que desea? >
* ver si quiere una reserva (para cuantas personas, horario (si hay disponibilidad en ese horario y si no ofrecer que horario esta disponible) , en caso de que no le interese (despedida y disculpar las molestias)
 en caso de que si le interese o cuadre un horario disponible (a nombre de quien se realiza la reserva, para cuantas personas, personas con alergias?, si hay niños? (se te ocurre alguna mas?)) 
* si tiene interes por el horario de apertura y ya preguntarle si quiere realizar un pedido o una reserva.
* Si quiere saber algo sobre la carta (por ejemplo a la hora de hacer el pedido o reserva, tambien ofrecerle si tiene interes sobre la carta durante la llamada).
* Opcion de realizar pedidos a domicilio y preguntas parecidas a la de reserva.

(Se te ocurre alguno mas?)

Dejaria en verdad esta fase dedicada solo a este sector en realidad el resto ingeniaria un mismo flujo para su llamada, verdad? 

dime que opinas y tu lógica primero antes de que diseñemos nada

-----------------------------

HOSTELERIA:

RESERVA

Es la principal.

Campos razonables:

nombre de la reserva
número de personas
fecha
hora
alergias o restricciones
niños o necesidad especial (carrito?)
terraza o interior
teléfono de contacto, 
si más adelante queréis confirmación real de la reserva (llamada de que lo confirman).

tambien:

A. Cancelar o modificar reserva

Esto me parece bastante útil.

Porque en hostelería pasa mucho:

“tenía una reserva”
“quiero cambiar la hora”
“quiero cancelar”

Esto da valor real.

B. Consultar disponibilidad sin reservar todavía

Ejemplo:

“¿tenéis sitio para esta noche?”

Esto es parecido a reserva, pero no igual.

C. Eventos / grupos grandes

Ejemplo:

cumpleaños
grupo grande
comida de empresa

Esto probablemente no lo automatizaría completo aún, pero sí detectaría el caso y lo marcaría como:

“caso especial”
“derivar”

Muy útil.

ESQUEMA:

Núcleo del flujo hostelería:
saludo
detección de intención
subflujo
confirmación
cierre

Subflujos prioritarios:
reserva
horario
carta básica
pedido simple
cancelar/modificar reserva
consulta general / derivación

---------------------------------

HORARIO

interes por el horario de apertura

Y aquí tiene sentido enlazar después con:

“¿quieres hacer una reserva?”
“¿quieres consultar carta?”
“¿quieres hacer un pedido?”

----------------------------------

Carta / menú

carta general
menú del día
opciones vegetarianas
alérgenos
platos destacados

----------------------------------

Pedido a domicilio o recogida

nombre
tipo de pedido
dirección o recogida
hora estimada
alergias / observaciones

----------------------------------
Consulta general

Siempre conviene tener un cajón de:

“otra consulta”
“hablar con alguien”
“no he entendido bien”

Esto evita que el flujo se rompa.