# Informe Académico (entrega 1)
## Integrantes del equipo: Antonio Caiafa, Mateo Nicodella, Juan Manuel Rial

## Repositorio Git

## Investigación

### Técnicas de elicitación: Entrevista

#### Entrevista 1:

El objetivo de esta entrevista es aprender de la experiencia de la entrevistada, sobre cual fue su experiencia al planificar un cumpleaños de 15 para su hija aca en Montevideo Uruguay. Nos interesa saber que cosas priorizar sobre otras, si la comida es lo mas importante o talves el lugar, entre otras muchas otras cosas, aparte nos interesa saber que dificultades se presentaron y como las resolvieron.

El plan consistia en hacerle preguntas a la entrevistada respecto a su experienca, para que sirvan como para empezar una converzacion con la entrevistada respecto al tema de la pregunta. En su mayoria los temas eran los invitados, como mandaban las invitaciones, como eran las respuestas, como se administraba todo, habia dificultades con algun invitado, etc. Tambien esta el manejo de la plata, como cual era el presupuesto, se hizo un gasto inecesario, hay algo que le hubiese comprar pero no lo hizo, etc.

Para resumir, lo que nos compartio la entrevistada fue que, hay que llevar un control sobre todo lo importante, ya sea sobre los invitados, si estos confirmaron su asistencia o no, si uno de ellos tiene una limitacion ya sea este vegetariano, celiaco, etc., ya sea sobre los gastos, si todo cabe dentro del presupuesto, si da lo suficiente talves darse un gusto. Otra cosa a destacar que la entrevistada menciona es que si es posible comprar el lugar, el servicio y la comida de un mismo paquete, ya que es mas confiable y al mismo tiempo mas eficiente.

#### Entrevista 2:



### Técnicas de elicitación: Ingieneria Inversa


## RN & RNF
Los requisitos funcionales son aquellas funciones que la aplicación debe cumplir, es decir, todo lo que el sistema tiene que hacer para resolver el problema planteado. Por ejemplo, permitir enviar invitaciones, confirmar asistencia o registrar restricciones alimentarias. Por otro lado, los requisitos no funcionales definen cómo debe comportarse la aplicación, como su facilidad de uso, la seguridad de los datos o que funcione bien desde el celular. Estos no indican nuevas funciones, sino que aseguran que el sistema funcione de manera eficiente y confiable.

La prioridad alta indica que es esencial para la funcionalidad del sistema. La prioridad media indica que el requisito es importante y mejora la experiencia del usuario, pero no es crítico para el funcionamiento básico. La prioridad baja es para funcionalidades que pueden ser opcionales que pueden implementarse en versiones posteriores.

El actor es quien realiza la acción principal de cada requisito. El actor puede ser el usuario, el organizador, el invitado o el sistema.

<h3 align="center">Requerimientos Funcionales:</h3>
<p align="center"><strong>#01: Registro de evento.</strong><br>
Descripción: El sistema debe permitir al usuario la creación de un evento indicando fecha, lugar, temática y datos de contacto.<br>
Prioridad: alta.<br>
Actor: Organizador</p>

<p align="center"><strong>#02: Envío de invitaciones digitales</strong><br>
El sistema debe permitir enviar invitaciones por medios digitales (WhatsApp, mail o enlace).<br>
Prioridad: alta.<br>
Actor: Sistema</p>

<p align="center"><strong>#03: Confirmación de asistencia</strong><br>
El sistema debe administrar la confirmación o rechazo de la invitación por parte del invitado.<br>
Prioridad: alta.<br>
Actor: Invitado</p>

<p align="center"><strong>#04: Registro de restricciones alimentarias</strong><br>
Cada invitado podrá informar si tiene alguna restricción (celíaco, vegetariano, alérgico, etc.).<br>
Prioridad: media.<br>
Actor: Invitado</p>

<p align="center"><strong>#05: Asignación de mesas</strong><br>
El organizador podrá asignar invitados a distintas mesas con una interfaz gráfica.<br>
Prioridad: alta.<br>
Actor: Organizador</p>

<p align="center"><strong>#06: Envío de recordatorios y notificaciones</strong><br>
El sistema enviará recordatorios automáticos antes del evento.<br>
Prioridad: media.<br>
Actor: Sistema</p>

<p align="center"><strong>#07: Cambios del Evento</strong><br>
El sistema le permitirá al organizador realizar cambios al evento.<br>
Prioridad: alta.<br>
Actor: Organizador</p>

<p align="center"><strong>#08: Gestión de cambios de último momento</strong><br>
El sistema podrá notificar a los invitados sobre cambios (clima, lugar, hora).<br>
Prioridad: alta.<br>
Actor: Sistema</p>

<p align="center"><strong>#09: Panel de control del evento</strong><br>
Vista resumen con cantidad de confirmaciones, pendientes, restricciones, etc.<br>
Prioridad: alta.<br>
Actor: Sistema</p>

<p align="center"><strong>#10: Personalización de invitaciones</strong><br>
Posibilidad de agregar fotos, textos, colores y temática personalizada.<br>
Prioridad: baja.<br>
Actor: Organizador</p>

<p align="center"><strong>#11: Gestión de presupuesto</strong><br>
El sistema permitirá al usuario cargar y gestionar el presupuesto registrando los gastos.<br>
Prioridad: media.<br>
Actor: Organizador</p>

<h3 align="center">Requerimientos No Funcionales:</h3>

<p align="center"><strong>#01: Usabilidad</strong><br>
La app debe ser fácil de usar incluso para personas con bajo nivel tecnológico.<br>
Prioridad: alta.</p>

<p align="center"><strong>#02: Accesibilidad</strong><br>
El sistema debe ser accesible para dispositivos celulares Android/iOS y navegador Chrome y Safari.<br>
Prioridad: alta.</p>

<p align="center"><strong>#03: Seguridad</strong><br>
El sistema debe otorgar protección y seguridad de datos, cumpliento los requisitos de la Ley N° 18.331 de protección de datos.<br>
Prioridad: alta.</p>

<p align="center"><strong>#04: Escalabilidad y Rendimiento</strong><br>
El sistema debe poder actualizarse para agregar nuevas funcionalidades y mayor capacidad de usuarios sin afectar los tiempos de ejecución y rendimiento.<br>
Prioridad: media.</p>

<p align="center"><strong>#05: Tiempos de Carga</strong><br>
Todas las visitas deben cargarse en menos de 2 segundos con conexión estándar, siendo capaz de manejar hasta 6000 usuarios interactuando simultáneamente sin afectar el rendimiento.<br>
Prioridad: media.</p>

<p align="center"><strong>#06: Diseño y Asistencia inicial</strong><br>
El sistema debe tener un diseño intuitivo, los menús deben ser claros y sencillos. Además, el sistema debe incluir un breve tutorial inicial que guíe al usuario en los primeros pasos del uso de la aplicación.<br>
Prioridad: alta.</p>

<p align="center"><strong>#07: Disponibilidad</strong><br>
El sistema debe estar disponible el 99% del tiempo.<br>
Prioridad: alta.</p>

<p align="center"><strong>#08: Idioma</strong><br>
La aplicación debe estar disponible en español.<br>
Prioridad: alta.</p>


## User Stories & Use Cases

## Modelo de dominio

## Verificación & Validación

## Descripción del Trabajo Individual

## Reflexión

## Anexo

- ¿Cómo fue la experiencia general de organizar el evento?
- ¿Qué es lo más complicado al momento de planear la fiesta?
- ¿Qué fue lo más difícil o estresante de organizar el cumpleaños?
- ¿Cuánto tiempo te llevó planificar todo?
- ¿Cómo enviaste las invitaciones?
- ¿Tuviste problemas para que la gente confirme asistencia?
- ¿Cómo llevaste el control de quién venía y quién no?
- ¿Hubo cambios de último momento? 
- ¿Cómo se los comunicaste a los invitados?
- ¿Alguien te avisó si tenía alguna restricción alimentaria? 
- ¿Cómo lo registraste?
- ¿Cómo organizaste la distribución de las mesas?
- ¿Utilizaste alguna aplicación o herramienta digital para ayudarte? Si usaste alguna, ¿qué te gustó y qué no?
- Si existiera una app que te ayudará a enviar invitaciones, llevar el control de invitados, mesas y gastos, ¿la habrías usado?
- Si pudieras repetir el evento, ¿qué harías diferente?
- ¿Sentís que pudiste disfrutar el evento o estuviste pendiente de la organización?
- ¿Tuviste algún presupuesto definido desde el inicio? ¿De cuanto era?
- ¿Hubo gastos inesperados o fuera de presupuesto? ¿Cuáles?
- ¿Qué cosas te hubiera gustado tener pero no pudiste por el precio?
- ¿En qué cosas gastaste más dinero?
- ¿Si tuvieras que organizar otro evento, como manejarias el presupuesto de manera diferente?
- ¿Cuáles eran tus prioridades al momento de elegir el salón para la fiesta?
- ¿Qué comodidades o servicios te parecían indispensables en un salón para que todo salga bien?
- ¿Preferiste un salón que ofreciera paquetes completos o contrataste servicios por separado? 