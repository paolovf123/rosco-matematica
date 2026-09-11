ROSCO · Noruega vs Portugal
Sube esta carpeta completa a cualquier hosting estático (Netlify, Vercel, GitHub Pages, un servidor web).
Debe servirse por http/https (no abrir index.html con doble clic: el navegador bloquea los módulos JS en file://).

Archivos:
- index.html            el juego
- support.js            motor de la página (carga React desde CDN, requiere internet)
- rosco-preguntas.js    definiciones de cada equipo (Rosco de Matemática). Campo t: "con" (empieza con la letra, se muestra «Con la X»),
                        "contiene" («Contiene la X») o "representada" («Representada por la X»).
                        Se genera desde ../../generar_rosco.py junto con el PDF del moderador; también puede editarse a mano.

Teclas: 1 correcta · 2 pasapalabra · 3 error · Espacio iniciar/pausa

Reglas: gana el equipo con más aciertos. Desempate: si igualan en aciertos, gana el que haya usado menos tiempo (segundos consumidos de su reloj).

Sorteo: tras «¡A jugar!» se sortea qué rosco (1 o 2) juega cada equipo; empieza el equipo que recibe el Rosco 1.
La pista aparece con un fundido de 1 s cada vez que cambia, para que nadie la lea antes que el moderador.
