# Decisión de UX: Feedback al crear puntos en el mapa

Se implementó feedback visual inmediato cuando el usuario hace clic
en el mapa para crear un punto de ruta.

Al hacer clic, el sistema coloca un marcador temporal de forma instantánea,
indicando que la acción fue reconocida correctamente, evitando que el usuario
dude si el clic fue registrado o no.

Esta decisión se tomó porque en aplicaciones de mapas el usuario espera
respuestas inmediatas a sus acciones, especialmente cuando interactúa
directamente con el mapa.

# Decisión de UX: Manejo del estado de “Error”

Se consideró la posibilidad de errores de red o clics accidentales
durante la creación de puntos.

Para prevenir errores, el sistema solicita confirmación antes de guardar
un punto, permitiendo al usuario cancelar la acción si fue un clic
involuntario.

En caso de que ocurra un fallo en la comunicación con el servidor,
el sistema puede informar al usuario que el punto no fue guardado,
manteniendo el control en manos del usuario sin perder la interacción
con el mapa.