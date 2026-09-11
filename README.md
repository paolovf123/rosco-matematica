# Rosco de Matemática

Juego tipo *pasapalabra* para un duelo entre dos equipos. Cada equipo tiene **180 segundos** para dar la vuelta a su rosco de 27 letras (A–Z con Ñ) respondiendo definiciones de matemática.

## Jugar

- **En línea (GitHub Pages):** https://paolovf123.github.io/rosco-matematica/
- **En local:** el juego usa módulos JS, así que debe servirse por http (no abrir `index.html` con doble clic).

  ```bash
  cd juego/deploy
  python -m http.server 8080
  # abrir http://localhost:8080/
  ```

  El motor carga React desde un CDN, por lo que necesita internet.

## Modo demo

En la pantalla inicial se puede elegir **Demo · 10 letras · 60 s**: un rosco corto de cultura general por equipo para explicar a los participantes cómo se juega antes de la competencia. Las preguntas están en `juego/deploy/rosco-demo.js` y en la tercera página del PDF del moderador.

## Reglas

| Tecla | Acción |
|---|---|
| `1` | Correcta |
| `2` | Pasapalabra (la letra vuelve al final) |
| `3` | Error |
| `Espacio` | Iniciar / pausar el reloj |

Antes de empezar, el moderador **asigna el Rosco 1 y el Rosco 2** a cada equipo (al elegir uno, el otro recibe el restante); empieza el equipo con el Rosco 1. La pista solo se muestra con el reloj en marcha y aparece con un fundido de 1,5 s.

Gana el equipo con más aciertos. **Desempate:** si igualan en aciertos, gana el que haya usado menos tiempo de su reloj.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `juego/deploy/` | El juego (HTML + JS). `rosco-preguntas.js` contiene las definiciones de cada equipo; `rosco-demo.js`, las del modo demo. |
| `rosco_moderador_v2.pdf` | Guía del moderador: pistas, respuestas correctas y respuestas alternativas aceptadas. **Imprimir para quien modera**, porque el juego no muestra las respuestas. |
| `rosco_moderador_cambios.md` | Registro de correcciones frente a la versión original y estimación de tiempos por vuelta. |
| `generar_rosco.py` | Fuente única de las preguntas. Genera el PDF, el registro de cambios, `rosco-preguntas.js` y `rosco-demo.js`. |
| `rosco_moderador.pdf` | Versión original, solo como referencia. |

## Editar las preguntas

1. Edita las pistas en `generar_rosco.py` (diccionario `NEW`). Cada entrada es `(letra, tipo de pista, pista, respuesta, nota)`.
2. Ejecuta `python generar_rosco.py`. El script valida que el tipo de pista coincida con la respuesta, recalcula los tiempos y regenera el PDF y el archivo del juego.
3. Requiere Python 3 con `reportlab` y `pymupdf` (`pip install reportlab pymupdf`). Usa la fuente Arial de Windows (`C:/Windows/Fonts/arial.ttf`); en otro sistema cambia esa ruta al inicio del script.

Tipos de pista que se muestran sobre la letra:

- **Con la A** → la respuesta empieza con esa letra.
- **Contiene la Ñ** → la lleva en otra posición.
- **Representada por la Q** → la letra es el símbolo del concepto (Q = carga eléctrica, Z = enteros).
- **(Palabra compuesta.)** → la respuesta tiene dos palabras.
