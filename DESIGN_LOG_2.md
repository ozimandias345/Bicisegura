# DESIGN LOG 2 – BiciSegura

## Decisión de UX: Botón "Mi Ubicación"

Se agregó un botón de geolocalización para permitir que el usuario
identifique rápidamente su posición actual dentro del mapa.

Esta decisión se tomó porque los ciclistas necesitan orientación
inmediata sin tener que buscar manualmente su ubicación, especialmente
en entornos urbanos.

El sistema solicita permiso de ubicación y ofrece feedback inmediato
mostrando un marcador con el mensaje “Estás aquí”, lo que cumple con la
heurística de visibilidad del estado del sistema.

En caso de que el usuario no conceda permisos, el sistema mantiene el
control en manos del usuario sin bloquear la aplicación.

## Decisión UX: Uso de geolocalización

Se decidió solicitar la ubicación del usuario para centrar el mapa automáticamente,
ya que en una app de ciclismo urbano la referencia principal es el punto de inicio
real del usuario.

Esto cumple con la heurística de Nielsen de correspondencia entre el sistema y el
mundo real, al mostrar el entorno inmediato del ciclista.

---

## Heurísticas de Usabilidad Aplicadas

- Visibilidad del estado del sistema
- Control y libertad del usuario
- Correspondencia entre el sistema y el mundo real
- Feedback inmediato

---

## Prompt Utilizado (IA – Gemini Canvas)

"Agrega a un mapa interactivo hecho con Leaflet un botón flotante visible
en la esquina inferior derecha que permita al usuario centrar el mapa en
su ubicación actual usando la API de geolocalización del navegador.
El botón debe usar un ícono claro de localización y manejar errores si el
usuario no concede permisos."
