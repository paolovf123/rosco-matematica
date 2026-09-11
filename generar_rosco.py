# -*- coding: utf-8 -*-
import re, sys, io, unicodedata
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial", boldItalic="Arial-Bold")

OUT_DIR = "C:/Users/USER/Documents/project/frank"
SECONDS = 180

# ---------- ORIGINAL (para comparar) ----------
ORIG = {
 1: [
  ("A","Empieza con A","operación que consiste en juntar dos o más cantidades.","Adición"),
  ("B","Contiene la B","sistema numérico que solo usa los dígitos 0 y 1.","Binario"),
  ("C","Empieza con C","figura geométrica formada por todos los puntos que están a la misma distancia de un centro.","Circunferencia"),
  ("D","Empieza con D","resultado que se obtiene al restar dos cantidades.","Diferencia"),
  ("E","Empieza con E","expresión matemática que tiene una igualdad y una incógnita por resolver.","Ecuación"),
  ("F","Empieza con F","producto de multiplicar un número por todos los enteros positivos menores que él (por ejemplo, 5×4×3×2×1).","Factorial"),
  ("G","Empieza con G","elemento químico metálico, de símbolo Ga, que se funde casi con el simple calor de la mano.","Galio"),
  ("H","Empieza con H","lado más largo de un triángulo rectángulo, ubicado frente al ángulo recto.","Hipotenusa"),
  ("I","Contiene la I","número que no se puede escribir como una fracción exacta, como π o √2.","Irracional"),
  ("J","Contiene la J","unidad de energía en el Sistema Internacional.","Joule"),
  ("K","Contiene la K","unidad que se utiliza para medir la masa de un objeto.","Kilogramo"),
  ("L","Empieza con L","cada uno de los segmentos que forman los bordes de un polígono.","Lado"),
  ("M","Empieza con M","valor que queda justo en el centro de un conjunto de datos ordenados.","Mediana"),
  ("N","Empieza con N","conjunto de números que usamos para contar.","Naturales"),
  ("Ñ","Contiene la Ñ","año que tiene 366 días debido a que febrero cuenta con un día adicional. (La respuesta tiene dos palabras).","Año bisiesto"),
  ("O","Empieza con O","nombre general que se le da a la suma, resta, multiplicación o división.","Operación"),
  ("P","Empieza con P","relación constante entre la longitud de una circunferencia y su diámetro.","Pi"),
  ("Q","Representada por la Q","propiedad física fundamental de la materia que provoca que las partículas se atraigan o se repelan entre sí. (La respuesta tiene dos palabras).","Carga eléctrica"),
  ("R","Empieza con R","en una raíz, es el número o expresión que se encuentra dentro del símbolo radical.","Radicando"),
  ("S","Empieza con S","sistema de medición angular que utiliza como base el número 60, expresado en grados, minutos y segundos.","Sexagesimal"),
  ("T","Empieza con T","línea recta que toca una curva o circunferencia en un solo punto.","Tangente"),
  ("U","Empieza con U","cifra que ocupa el primer lugar de la derecha en un número.","Unidad"),
  ("V","Empieza con V","letra o símbolo que se usa para representar un valor desconocido.","Variable"),
  ("W","Contiene la W","unidad de potencia en el Sistema Internacional.","Watt"),
  ("X","Empieza con X","elemento químico gaseoso y noble que se utiliza en algunas lámparas y faros de vehículos.","Xenón"),
  ("Y","Representada por la Y","Conector lógico que vincula 2 proposiciones, cuyo resultado es falso si ambas proposiciones son falsas.","Disyunción"),
  ("Z","Representada por la Z","Conjunto de números formado por los positivos, negativos y el cero sin partes decimales ni fraccionarias.","Enteros"),
 ],
 2: [
  ("A","Empieza con A","espacio que se forma entre dos rectas o segmentos que se cruzan en un punto.","Ángulo"),
  ("B","Empieza con B","recta que divide un ángulo en dos partes exactamente iguales.","Bisectriz"),
  ("C","Empieza con C","resultado que se obtiene al dividir una cantidad entre otra.","Cociente"),
  ("D","Empieza con D","segmento que atraviesa una circunferencia pasando por su centro y une dos puntos de ella.","Diámetro"),
  ("E","Empieza con E","número pequeño ubicado arriba de otro, que indica cuántas veces se multiplica una base por sí misma.","Exponente"),
  ("F","Empieza con F","número de veces que se repite un dato dentro de un conjunto de valores estadísticos.","Frecuencia"),
  ("G","Empieza con G","unidad que se usa para medir el tamaño de un ángulo.","Grado"),
  ("H","Empieza con H","polígono que tiene siete lados.","Heptágono"),
  ("I","Empieza con I","número entero que no se puede dividir exactamente entre 2.","Impar"),
  ("J","Representada por la J","Conector lógico que vincula 2 proposiciones, cuyo resultado es verdadero si ambas proposiciones son verdaderas.","Conjunción"),
  ("K","Contiene la K","unidad de longitud equivalente a mil metros.","Kilómetro"),
  ("L","Empieza con L","unidad que se usa para medir el volumen de los líquidos.","Litro"),
  ("M","Empieza con M","valor que aparece con más frecuencia en un conjunto de datos.","Moda"),
  ("N","Empieza con N","número que se ubica en la parte de arriba de una fracción.","Numerador"),
  ("Ñ","Contiene la Ñ","unidad de distancia usada en astronomía, equivalente a la distancia que recorre la luz en un año. (La respuesta tiene dos palabras).","Año luz"),
  ("O","Empieza con O","polígono que tiene ocho lados.","Octógono"),
  ("P","Empieza con P","número natural mayor que 1 que solo tiene dos divisores positivos distintos: él mismo y el 1.","Primo"),
  ("Q","Representada por la Q","energía que se transfiere de un sistema a otro debido a una diferencia de temperatura, y que se mide en joules o calorías.","Calor"),
  ("R","Empieza con R","unidad angular del Sistema Internacional; una vuelta completa equivale a 2π de esta unidad.","Radián"),
  ("S","Empieza con S","propiedad de una figura que puede dividirse en dos partes iguales que se reflejan entre sí.","Simetría"),
  ("T","Empieza con T","proposición matemática que se demuestra como verdadera a partir de axiomas o de otras verdades ya establecidas.","Teorema"),
  ("U","Empieza con U","operación entre conjuntos que junta todos los elementos de ambos.","Unión"),
  ("V","Empieza con V","punto donde se encuentran dos lados de una figura o dos aristas de un cuerpo.","Vértice"),
  ("W","Representada por la W","magnitud física que resulta de aplicar una fuerza sobre un cuerpo provocando su desplazamiento; se mide en joules.","Trabajo"),
  ("X","Representada por la X","eje horizontal del plano cartesiano.","Abscisas"),
  ("Y","Contiene la Y","se dice de dos ángulos que comparten el vértice y un lado, sin superponerse entre sí.","Adyacentes"),
  ("Z","Representada por la Z","en química, es el número que indica la cantidad de protones que tiene el núcleo de un átomo. (La respuesta tiene dos palabras).","Número atómico"),
 ],
}

# ---------- VERSIÓN CORREGIDA ----------
# (letra, tipo de pista, pista, respuesta, nota para el moderador)
NEW = {
 1: [
  ("A","Con la A","Operación de juntar dos o más cantidades.","Adición",""),
  ("B","Con la B","Sistema numérico que usa solo los dígitos 0 y 1.","Binario",""),
  ("C","Con la C","Línea curva cerrada cuyos puntos equidistan del centro.","Circunferencia","No aceptar «círculo»."),
  ("D","Con la D","Resultado de restar dos cantidades.","Diferencia",""),
  ("E","Con la E","Aquello que tiene igual valor, función, peso o significado que otra cosa.","Equivalente",""),
  ("F","Con la F","Producto de un número natural por todos los anteriores hasta el 1 (ejemplo: 5×4×3×2×1).","Factorial",""),
  ("G","Con la G","Metal de símbolo Ga que se funde en la mano.","Galio",""),
  ("H","Con la H","Lado mayor de un triángulo rectángulo.","Hipotenusa",""),
  ("I","Con la I","Número que no puede escribirse como fracción, como π.","Irracional","Aceptar «irracionales»."),
  ("J","Con la J","Unidad de energía en el Sistema Internacional.","Joule","Aceptar «julio»."),
  ("K","Con la K","Unidad básica de masa en el Sistema Internacional.","Kilogramo",""),
  ("L","Con la L","Cada segmento que forma el contorno de un polígono.","Lado",""),
  ("M","Con la M","Valor central de un conjunto de datos ordenados.","Mediana",""),
  ("N","Con la N","Números que usamos para contar.","Naturales",""),
  ("Ñ","Contiene la Ñ","Año de 366 días. (Palabra compuesta.)","Año bisiesto",""),
  ("O","Con la O","Nombre general de la suma, resta, multiplicación y división.","Operación",""),
  ("P","Con la P","Razón entre la longitud de una circunferencia y su diámetro.","Pi","Aceptar «número pi»."),
  ("Q","Representada por la Q","Propiedad física por la que los cuerpos se atraen o se repelen. (Palabra compuesta.)","Carga eléctrica",""),
  ("R","Con la R","Número o expresión que está dentro del signo radical.","Radicando",""),
  ("S","Con la S","Sistema angular de base 60: grados, minutos y segundos.","Sexagesimal",""),
  ("T","Con la T","Recta que toca a una circunferencia en un solo punto.","Tangente",""),
  ("U","Con la U","Cifra que ocupa el primer lugar desde la derecha.","Unidad",""),
  ("V","Con la V","Letra o símbolo que representa un valor desconocido.","Variable",""),
  ("W","Con la W","Unidad de potencia en el Sistema Internacional.","Watt","Aceptar «vatio»."),
  ("X","Con la X","Gas noble usado en lámparas y faros de vehículos.","Xenón",""),
  ("Y","Contiene la Y","Conector lógico que solo es falso si ambas proposiciones son falsas.","Disyunción",""),
  ("Z","Representada por la Z","Números positivos, negativos y el cero, sin parte decimal.","Enteros",""),
 ],
 2: [
  ("A","Con la A","Abertura entre dos semirrectas con un origen común.","Ángulo",""),
  ("B","Con la B","Recta que divide un ángulo en dos partes iguales.","Bisectriz",""),
  ("C","Con la C","Resultado de dividir una cantidad entre otra.","Cociente",""),
  ("D","Con la D","Segmento que cruza la circunferencia pasando por su centro.","Diámetro",""),
  ("E","Con la E","Igualdad matemática con una o más incógnitas.","Ecuación",""),
  ("F","Con la F","Número de veces que se repite un dato estadístico.","Frecuencia",""),
  ("G","Con la G","Unidad para medir ángulos; una vuelta completa tiene 360.","Grado",""),
  ("H","Con la H","Polígono de siete lados.","Heptágono",""),
  ("I","Con la I","Número entero que no es divisible entre 2.","Impar",""),
  ("J","Contiene la J","Conector lógico que solo es verdadero si ambas proposiciones son verdaderas.","Conjunción",""),
  ("K","Con la K","Unidad de longitud equivalente a mil metros.","Kilómetro",""),
  ("L","Con la L","Unidad para medir el volumen de los líquidos.","Litro",""),
  ("M","Con la M","Valor que más se repite en un conjunto de datos.","Moda",""),
  ("N","Con la N","Número que va arriba en una fracción.","Numerador",""),
  ("Ñ","Contiene la Ñ","Distancia que recorre la luz en un año. (Palabra compuesta.)","Año luz",""),
  ("O","Con la O","Polígono de ocho lados.","Octógono","Aceptar «octágono»."),
  ("P","Con la P","Número con solo dos divisores: el 1 y él mismo.","Primo",""),
  ("Q","Representada por la Q","Energía transferida entre cuerpos por diferencia de temperatura.","Calor",""),
  ("R","Con la R","Unidad angular del Sistema Internacional; una vuelta completa mide 2π.","Radián",""),
  ("S","Con la S","Propiedad de una figura cuyas mitades son reflejo una de otra.","Simetría",""),
  ("T","Con la T","Proposición que se demuestra a partir de axiomas.","Teorema",""),
  ("U","Con la U","Operación entre conjuntos que reúne los elementos de ambos.","Unión",""),
  ("V","Con la V","Punto donde se encuentran dos lados de una figura.","Vértice",""),
  ("W","Representada por la W","Fuerza por desplazamiento; se mide en joules.","Trabajo",""),
  ("X","Contiene la X","Indica la cantidad de veces que se multiplica una base por sí misma.","Exponente",""),
  ("Y","Contiene la Y","Ángulos que comparten vértice y un lado, sin superponerse.","Adyacentes",""),
  ("Z","Representada por la Z","Cantidad de protones en el núcleo de un átomo. (Palabra compuesta.)","Número atómico",""),
 ],
}

# ---------- ROSCO DEMO (10 letras por equipo, cultura general, para explicar el juego) ----------
DEMO_SECONDS = 60
DEMO = {
 1: [
  ("A","Con la A","Continente donde están China y Japón.","Asia",""),
  ("C","Con la C","Lugar donde se proyectan películas en pantalla grande.","Cine",""),
  ("E","Con la E","Animal terrestre más grande; tiene trompa.","Elefante",""),
  ("G","Con la G","Animal doméstico que maúlla.","Gato",""),
  ("L","Con la L","Capital del Perú.","Lima",""),
  ("Ñ","Contiene la Ñ","Fiesta que se celebra el primero de enero. (Palabra compuesta.)","Año Nuevo",""),
  ("P","Con la P","Ave blanca y negra que vive en el hielo y no vuela.","Pingüino",""),
  ("S","Con la S","Estrella que da luz y calor a la Tierra.","Sol",""),
  ("V","Representada por la V","Número que vale esta letra en números romanos.","Cinco",""),
  ("Z","Con la Z","Calzado que cubre el pie.","Zapato",""),
 ],
 2: [
  ("B","Con la B","Deporte en el que se encesta un balón en un aro.","Baloncesto","Aceptar «básquet»."),
  ("D","Con la D","Animal marino muy inteligente que salta sobre las olas.","Delfín",""),
  ("F","Con la F","Deporte más popular del mundo; se juega con los pies.","Fútbol",""),
  ("H","Con la H","Insecto pequeño que vive en colonias y carga hojas.","Hormiga",""),
  ("J","Con la J","Animal africano de cuello muy largo.","Jirafa",""),
  ("L","Con la L","Fase en la que la Luna se ve como un círculo completo. (Palabra compuesta.)","Luna llena",""),
  ("M","Con la M","Planeta conocido como el planeta rojo.","Marte",""),
  ("O","Contiene la O","Instrumento musical de teclas blancas y negras.","Piano",""),
  ("T","Con la T","Reptil lento que lleva un caparazón.","Tortuga",""),
  ("X","Representada por la X","Número que vale esta letra en números romanos.","Diez",""),
 ],
}

# ---------- VALIDACIÓN AUTOMÁTICA ----------
def strip_acc(s):
    # quita tildes pero conserva la Ñ
    out = []
    for c in s:
        if c in "ñÑ":
            out.append(c); continue
        out.append("".join(ch for ch in unicodedata.normalize("NFD", c) if unicodedata.category(ch) != "Mn"))
    return "".join(out)

def check(data, label):
    problems = []
    for letra, tipo, pista, resp, *_ in data:
        r = strip_acc(resp).upper()
        L = letra.upper()
        if tipo.startswith(("Empieza","Con la")) and not r.startswith(L):
            problems.append(f"{label} {letra}: '{tipo}' pero '{resp}' no empieza con {L}")
        if tipo.startswith("Contiene"):
            if L not in r:
                problems.append(f"{label} {letra}: '{tipo}' pero '{resp}' no contiene {L}")
            elif r.startswith(L):
                problems.append(f"{label} {letra}: '{tipo}' pero '{resp}' EMPIEZA con {L} (debería ser 'Empieza con')")
    return problems

def words(s): return len(re.findall(r"[\wπ√×0-9!]+", s))

WPS = 2.8       # palabras por segundo leyendo en voz alta (~170 ppm)
ANSWER_S = 2.0  # segundos promedio para que el equipo conteste

def stats(data):
    ws = [words(p) + words(t) for _, t, p, *_ in data]
    read = sum(ws) / WPS
    return dict(total_words=sum(ws), avg=sum(ws)/len(ws), mx=max(ws),
                read_s=read, pass_s=read + ANSWER_S*len(ws))

print("=== Problemas en ORIGINAL ===")
for k in (1,2):
    for p in check(ORIG[k], f"R{k}"): print("  ", p)
print("=== Problemas en NUEVO ===")
bad = []
for k in (1,2):
    bad += check(NEW[k], f"R{k}")
    bad += check(DEMO[k], f"DEMO{k}")
for p in bad: print("  ", p)
if not bad: print("   ninguno")

print("\n=== Tiempo estimado de una vuelta completa (27 letras) ===")
for k in (1,2):
    o, n = stats(ORIG[k]), stats(NEW[k])
    print(f"R{k} original: {o['total_words']} palabras, media {o['avg']:.1f}, máx {o['mx']} -> lectura {o['read_s']:.0f}s, vuelta {o['pass_s']:.0f}s")
    print(f"R{k} nuevo   : {n['total_words']} palabras, media {n['avg']:.1f}, máx {n['mx']} -> lectura {n['read_s']:.0f}s, vuelta {n['pass_s']:.0f}s")

# ---------- PDF ----------
BLUE = colors.HexColor("#2F6FD0"); LIGHT = colors.HexColor("#DCE7F7"); DARK = colors.HexColor("#2B2B2B")
GREEN = colors.HexColor("#1E7B34"); GREY = colors.HexColor("#666666"); ZEBRA = colors.HexColor("#F5F7FB")

s_title = ParagraphStyle("t", fontName="Arial-Bold", fontSize=15, leading=18, alignment=1, spaceAfter=2)
s_sub   = ParagraphStyle("s", fontName="Arial", fontSize=8.5, leading=11, textColor=GREY, alignment=1)
s_tip   = ParagraphStyle("tip", fontName="Arial", fontSize=8, leading=10, textColor=colors.HexColor("#8A4B00"), alignment=1, spaceBefore=1, spaceAfter=5)
s_band  = ParagraphStyle("b", fontName="Arial-Bold", fontSize=13, leading=16, textColor=colors.white, alignment=1)
s_hdr   = ParagraphStyle("h", fontName="Arial-Bold", fontSize=8, leading=10, textColor=colors.white, alignment=1)
s_let   = ParagraphStyle("l", fontName="Arial-Bold", fontSize=11, leading=12, textColor=BLUE, alignment=1)
s_q     = ParagraphStyle("q", fontName="Arial", fontSize=8.6, leading=10.5)
s_ans   = ParagraphStyle("a", fontName="Arial-Bold", fontSize=8.6, leading=10.5, textColor=GREEN)
s_note  = ParagraphStyle("n", fontName="Arial", fontSize=7, leading=8.5, textColor=GREY)

W = 10.0*inch
def _banda(texto):
    band = Table([[Paragraph(texto, s_band)]], colWidths=[W])
    band.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),BLUE), ("TOPPADDING",(0,0),(-1,-1),6), ("BOTTOMPADDING",(0,0),(-1,-1),6)]))
    return band

def _tabla(data):
    rows = [[Paragraph("Letra", s_hdr), Paragraph("Pista (leer al equipo)", s_hdr), Paragraph("Respuesta correcta", s_hdr), Paragraph("Nota", s_hdr)]]
    for letra, tipo, pista, resp, nota in data:
        rows.append([Paragraph(letra, s_let),
                     Paragraph(f"<b>{tipo}:</b> {pista}", s_q),
                     Paragraph(resp, s_ans),
                     Paragraph(nota, s_note)])
    t = Table(rows, colWidths=[0.55*inch, W-0.55*inch-1.55*inch-1.75*inch, 1.55*inch, 1.75*inch], repeatRows=1)
    st = [("BACKGROUND",(0,0),(-1,0),DARK), ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
          ("BACKGROUND",(0,1),(0,-1),LIGHT), ("LINEBELOW",(0,0),(-1,-1),0.4,colors.HexColor("#C9D3E3")),
          ("BOX",(0,0),(-1,-1),0.6,colors.HexColor("#9FB0CC")), ("TOPPADDING",(0,0),(-1,-1),1.5), ("BOTTOMPADDING",(0,0),(-1,-1),1.5),
          ("LEFTPADDING",(0,0),(-1,-1),5), ("RIGHTPADDING",(0,0),(-1,-1),5)]
    for i in range(1, len(rows)):
        if i % 2 == 0: st.append(("BACKGROUND",(1,i),(-1,i),ZEBRA))
    t.setStyle(TableStyle(st))
    return t

def rosco_page(k):
    t = _tabla(NEW[k])
    band = _banda(f"ROSCO {k} — Equipo {k}")
    return [Paragraph("Rosco de Matemática — Guía del Moderador", s_title),
            Paragraph(f"Duelo por equipos · <b>{SECONDS} segundos por equipo</b> · Teclas: <b>1</b> Correcto · <b>2</b> Pasapalabra · <b>3</b> Incorrecto", s_sub),
            Paragraph("Lectura: <b>«Con la A»</b> = empieza con A · <b>«Contiene la A»</b> = la lleva dentro · "
                      "<b>«Representada por la A»</b> = es su símbolo · <b>(Palabra compuesta)</b> = dos palabras.", s_sub),
            Paragraph(f"Ritmo: 27 letras en {SECONDS} s ≈ 6,5 s por letra. Lea la pista una sola vez, a ritmo normal; repítala solo si el equipo lo pide. "
                      "Si el equipo duda más de 3 s, recuérdele que puede decir «pasapalabra». "
                      "Gana el equipo con más aciertos; si empatan, gana el que haya usado menos tiempo.", s_tip),
            band, Spacer(1, 3), t]

out = f"{OUT_DIR}/rosco_moderador_v2.pdf"
doc = SimpleDocTemplate(out, pagesize=landscape(letter), leftMargin=0.5*inch, rightMargin=0.5*inch, topMargin=0.35*inch, bottomMargin=0.3*inch,
                        title="Rosco de Matemática — Guía del Moderador (v2)", author="")
def demo_page():
    return [Paragraph("Rosco DEMO — para explicar el juego", s_title),
            Paragraph(f"Cultura general · <b>10 letras y {DEMO_SECONDS} segundos por equipo</b> · en el juego, elija «Demo» en la pantalla inicial", s_sub),
            Paragraph("Úselo para mostrar las teclas (1 correcta · 2 pasapalabra · 3 error), cómo vuelven las letras pasadas, "
                      "los tres tipos de pista, el fin del tiempo y el desempate. No cuenta para la competencia.", s_tip),
            _banda("ROSCO DEMO 1 — Equipo 1"), Spacer(1, 3), _tabla(DEMO[1]), Spacer(1, 8),
            _banda("ROSCO DEMO 2 — Equipo 2"), Spacer(1, 3), _tabla(DEMO[2])]

story = rosco_page(1) + [PageBreak()] + rosco_page(2) + [PageBreak()] + demo_page()
doc.build(story)
print("\nPDF ->", out)

# ---------- CHANGELOG ----------
lines = ["# Rosco de Matemática — Registro de cambios (v2)", "",
         f"- Tiempo por equipo: el PDF original decía **120 s**; se actualizó a **{SECONDS} s** según lo indicado.",
         "- Convención de lectura: cuando la respuesta empieza con la letra se lee solo **«Con la A: …»** (sin «empieza»); «Contiene la…» y «Representada por la…» sí se especifican.",
         "- Las respuestas de dos palabras se anuncian como **(Palabra compuesta.)** en lugar de «(Dos palabras)».",
         "- Regla de desempate: si ambos equipos igualan en aciertos, gana el que haya usado menos tiempo de su reloj.",
         "- Se añadió una línea de ritmo para el moderador (≈ 6,5 s por letra) y una columna **Nota** con respuestas alternativas aceptadas.",
         "- Todas las pistas se acortaron para que una vuelta completa quepa holgadamente en el tiempo (ver tabla de tiempos al final).",
         "- Ajustes del 10 de septiembre de 2026: la X del Rosco 2 pasa a **«Contiene la X: Exponente»** (antes «Representada por la X: Abscisas»); "
         "se incorporó la pista de **Equivalente** para la E y se intercambiaron las E de ambos roscos (Rosco 1: Equivalente · Rosco 2: Ecuación).", ""]
for k in (1,2):
    lines += [f"## Rosco {k}", "", "| Letra | Tipo de pista | Cambio principal | Pista nueva | Respuesta |", "|---|---|---|---|---|"]
    for (l, t0, p0, r0), (_, t1, p1, r1, nota) in zip(ORIG[k], NEW[k]):
        cat = lambda t: "E" if t.startswith(("Empieza","Con la")) else ("C" if t.startswith("Contiene") else "R")
        nueva = strip_acc(r0).lower() != strip_acc(r1).lower()
        tipo = f"~~{t0}~~ → **{t1}**" if cat(t0) != cat(t1) and not nueva else t1
        if nueva: cambio = f"**Pregunta nueva** (antes: {r0})"
        elif cat(t0) != cat(t1): cambio = "**Tipo de pista corregido**"
        elif words(p1) < words(p0): cambio = f"Acortada ({words(p0)}→{words(p1)} palabras)"
        else: cambio = "Redacción"
        lines.append(f"| {l} | {tipo} | {cambio} | {p1} | {r1}{(' · _' + nota + '_') if nota else ''} |")
    lines.append("")
lines += ["## Tiempo estimado de una vuelta completa (27 letras)", "",
          f"Supuestos: lectura en voz alta a {WPS} palabras/s (~170 ppm) y {ANSWER_S:.0f} s de respuesta por letra.", "",
          "| Rosco | Versión | Palabras totales | Media por pista | Pista más larga | Solo lectura | Vuelta completa |", "|---|---|---|---|---|---|---|"]
for k in (1,2):
    for name, d in (("original", stats(ORIG[k])), ("v2", stats(NEW[k]))):
        lines.append(f"| {k} | {name} | {d['total_words']} | {d['avg']:.1f} | {d['mx']} | {d['read_s']:.0f} s | {d['pass_s']:.0f} s |")
lines += ["", f"Con {SECONDS} s por equipo, la v2 deja ~{SECONDS - stats(NEW[1])['pass_s']:.0f}–{SECONDS - stats(NEW[2])['pass_s']:.0f} s de margen para los pasapalabra.", ""]
open(f"{OUT_DIR}/rosco_moderador_cambios.md", "w", encoding="utf-8").write("\n".join(lines))
print("MD  ->", f"{OUT_DIR}/rosco_moderador_cambios.md")

# ---------- JUEGO HTML: juego/deploy/rosco-preguntas.js ----------
import json, os
def tipo_de(t):
    return "contiene" if t.startswith("Contiene") else ("representada" if t.startswith("Representada") else "con")
def js_equipo(nombre, data):
    j = lambda x: json.dumps(x, ensure_ascii=False)
    out = [f"export const {nombre} = ["]
    for letra, tipo, pista, resp, nota in data:
        out.append(f"  {{ l:{j(letra)}, t:{j(tipo_de(tipo))}, r:{j(resp)}, d:{j(pista)} }},")
    out.append("];")
    return "\n".join(out)
JS_PATH = f"{OUT_DIR}/juego/deploy/rosco-preguntas.js"
if os.path.isdir(os.path.dirname(JS_PATH)):
    letras = json.dumps([x[0] for x in NEW[1]], ensure_ascii=False)
    js = "\n".join([
        "// Generado por generar_rosco.py — edita las pistas allí (o aquí, si prefieres) y vuelve a ejecutarlo.",
        "// Cada equipo tiene 27 entradas (A–Z con Ñ). Campos:",
        "//   l: letra · r: respuesta · d: definición (se lee al equipo)",
        "//   t: tipo de pista → \"con\" = la respuesta empieza con la letra (se muestra «Con la X»)",
        "//                       \"contiene\" = la lleva en otra posición («Contiene la X»)",
        "//                       \"representada\" = la letra es su símbolo («Representada por la X»)",
        f"export const LETRAS = {letras};",
        "",
        js_equipo("EQUIPO_A", NEW[1]),
        "",
        js_equipo("EQUIPO_B", NEW[2]),
        "",
    ])
    open(JS_PATH, "w", encoding="utf-8").write(js)
    print("JS  ->", JS_PATH)
    DEMO_PATH = f"{OUT_DIR}/juego/deploy/rosco-demo.js"
    js_demo = "\n".join([
        "// Generado por generar_rosco.py — rosco DEMO de cultura general (10 letras por equipo) para explicar el juego.",
        "// Se usa al elegir «Demo» en la pantalla inicial. Mismos campos que rosco-preguntas.js (l, t, r, d).",
        f"export const TIEMPO = {DEMO_SECONDS}; // segundos por equipo en modo demo (informativo; el juego usa DEMO_TIEMPO en index.html)",
        "",
        js_equipo("EQUIPO_A", DEMO[1]),
        "",
        js_equipo("EQUIPO_B", DEMO[2]),
        "",
    ])
    open(DEMO_PATH, "w", encoding="utf-8").write(js_demo)
    print("JS  ->", DEMO_PATH)
