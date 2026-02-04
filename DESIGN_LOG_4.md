# DESIGN LOG 4 – BiciSegura

## Decisión de UX: Vista Dual Mapa + Lista de Lugares

Se implementó una vista dividida en dos secciones: un mapa interactivo y una
lista textual de lugares. Esta decisión se tomó para ofrecer una alternativa
accesible al mapa, permitiendo que usuarios que tengan dificultades visuales
o motrices puedan interactuar con la información sin depender únicamente
de la navegación gráfica.

La lista de lugares muestra cada punto agregado con una descripción clara
y legible, reforzando la accesibilidad mediante contenido textual.

---

## Decisión de UX: Sincronización entre Lista y Mapa

Cada vez que el usuario agrega un punto en el mapa, este se refleja
automáticamente en la lista lateral con su nombre y coordenadas.

Al hacer clic sobre un elemento de la lista, el mapa utiliza la animación
`flyTo` para centrar la vista en el marcador correspondiente, proporcionando
feedback visual inmediato y manteniendo la coherencia entre ambas vistas.

Esta sincronización reduce la carga cognitiva del usuario y facilita la
orientación espacial.

---

## Decisión de UX: Contraste y Claridad Visual

Se utilizaron íconos y marcadores con colores de alto contraste (verde, azul
y rojo) para diferenciar tipos de puntos de interés como estacionamientos,
talleres y zonas de peligro.

Esto mejora la legibilidad sobre los tiles del mapa y evita confusión,
especialmente en zonas con vegetación o alta densidad visual.

---

## Accesibilidad (A11y) Implementada

- Vista de lista como alternativa textual al mapa
- Sincronización mapa ↔ lista para navegación asistida
- Uso de íconos claros y colores contrastantes
- Controles del mapa con etiquetas descriptivas (`aria-label`)
- Mensajes claros y legibles en popups y tarjetas

---

## Heurísticas de Usabilidad Aplicadas

- Accesibilidad y flexibilidad de uso
- Visibilidad del estado del sistema
- Correspondencia entre el sistema y el mundo real
- Consistencia y estándares
- Reducción de carga cognitiva

---

## Prompt Utilizado (IA – Gemini Canvas)

"Modifica una aplicación web con Leaflet para tener una vista dividida entre
un mapa interactivo y una lista de lugares. Cada marcador agregado al mapa
debe aparecer como un elemento textual en la lista y, al hacer clic en dicho
elemento, el mapa debe centrar la vista usando flyTo. Asegura contraste visual
adecuado y agrega atributos aria-label a los controles del mapa."
