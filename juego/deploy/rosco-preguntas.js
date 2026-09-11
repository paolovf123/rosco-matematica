// Generado por generar_rosco.py — edita las pistas allí (o aquí, si prefieres) y vuelve a ejecutarlo.
// Cada equipo tiene 27 entradas (A–Z con Ñ). Campos:
//   l: letra · r: respuesta · d: definición (se lee al equipo)
//   t: tipo de pista → "con" = la respuesta empieza con la letra (se muestra «Con la X»)
//                       "contiene" = la lleva en otra posición («Contiene la X»)
//                       "representada" = la letra es su símbolo («Representada por la X»)
export const LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

export const EQUIPO_A = [
  { l:"A", t:"con", r:"Adición", d:"Operación de juntar dos o más cantidades." },
  { l:"B", t:"con", r:"Binario", d:"Sistema numérico que usa solo los dígitos 0 y 1." },
  { l:"C", t:"con", r:"Circunferencia", d:"Línea curva cerrada cuyos puntos equidistan del centro." },
  { l:"D", t:"con", r:"Diferencia", d:"Resultado de restar dos cantidades." },
  { l:"E", t:"con", r:"Equivalente", d:"Aquello que tiene igual valor, función, peso o significado que otra cosa." },
  { l:"F", t:"con", r:"Factorial", d:"Producto de un número natural por todos los anteriores hasta el 1 (ejemplo: 5×4×3×2×1)." },
  { l:"G", t:"con", r:"Galio", d:"Metal de símbolo Ga que se funde en la mano." },
  { l:"H", t:"con", r:"Hipotenusa", d:"Lado mayor de un triángulo rectángulo." },
  { l:"I", t:"con", r:"Irracional", d:"Número que no puede escribirse como fracción, como π." },
  { l:"J", t:"con", r:"Joule", d:"Unidad de energía en el Sistema Internacional." },
  { l:"K", t:"con", r:"Kilogramo", d:"Unidad básica de masa en el Sistema Internacional." },
  { l:"L", t:"con", r:"Lado", d:"Cada segmento que forma el contorno de un polígono." },
  { l:"M", t:"con", r:"Mediana", d:"Valor central de un conjunto de datos ordenados." },
  { l:"N", t:"con", r:"Naturales", d:"Números que usamos para contar." },
  { l:"Ñ", t:"contiene", r:"Año bisiesto", d:"Año de 366 días. (Palabra compuesta.)" },
  { l:"O", t:"con", r:"Operación", d:"Nombre general de la suma, resta, multiplicación y división." },
  { l:"P", t:"con", r:"Pi", d:"Razón entre la longitud de una circunferencia y su diámetro." },
  { l:"Q", t:"representada", r:"Carga eléctrica", d:"Propiedad física por la que los cuerpos se atraen o se repelen. (Palabra compuesta.)" },
  { l:"R", t:"con", r:"Radicando", d:"Número o expresión que está dentro del signo radical." },
  { l:"S", t:"con", r:"Sexagesimal", d:"Sistema angular de base 60: grados, minutos y segundos." },
  { l:"T", t:"con", r:"Tangente", d:"Recta que toca a una circunferencia en un solo punto." },
  { l:"U", t:"con", r:"Unidad", d:"Cifra que ocupa el primer lugar desde la derecha." },
  { l:"V", t:"con", r:"Variable", d:"Letra o símbolo que representa un valor desconocido." },
  { l:"W", t:"con", r:"Watt", d:"Unidad de potencia en el Sistema Internacional." },
  { l:"X", t:"con", r:"Xenón", d:"Gas noble usado en lámparas y faros de vehículos." },
  { l:"Y", t:"contiene", r:"Disyunción", d:"Conector lógico que solo es falso si ambas proposiciones son falsas." },
  { l:"Z", t:"representada", r:"Enteros", d:"Números positivos, negativos y el cero, sin parte decimal." },
];

export const EQUIPO_B = [
  { l:"A", t:"con", r:"Ángulo", d:"Abertura entre dos semirrectas con un origen común." },
  { l:"B", t:"con", r:"Bisectriz", d:"Recta que divide un ángulo en dos partes iguales." },
  { l:"C", t:"con", r:"Cociente", d:"Resultado de dividir una cantidad entre otra." },
  { l:"D", t:"con", r:"Diámetro", d:"Segmento que cruza la circunferencia pasando por su centro." },
  { l:"E", t:"con", r:"Ecuación", d:"Igualdad matemática con una o más incógnitas." },
  { l:"F", t:"con", r:"Frecuencia", d:"Número de veces que se repite un dato estadístico." },
  { l:"G", t:"con", r:"Grado", d:"Unidad para medir ángulos; una vuelta completa tiene 360." },
  { l:"H", t:"con", r:"Heptágono", d:"Polígono de siete lados." },
  { l:"I", t:"con", r:"Impar", d:"Número entero que no es divisible entre 2." },
  { l:"J", t:"contiene", r:"Conjunción", d:"Conector lógico que solo es verdadero si ambas proposiciones son verdaderas." },
  { l:"K", t:"con", r:"Kilómetro", d:"Unidad de longitud equivalente a mil metros." },
  { l:"L", t:"con", r:"Litro", d:"Unidad para medir el volumen de los líquidos." },
  { l:"M", t:"con", r:"Moda", d:"Valor que más se repite en un conjunto de datos." },
  { l:"N", t:"con", r:"Numerador", d:"Número que va arriba en una fracción." },
  { l:"Ñ", t:"contiene", r:"Año luz", d:"Distancia que recorre la luz en un año. (Palabra compuesta.)" },
  { l:"O", t:"con", r:"Octógono", d:"Polígono de ocho lados." },
  { l:"P", t:"con", r:"Primo", d:"Número con solo dos divisores: el 1 y él mismo." },
  { l:"Q", t:"representada", r:"Calor", d:"Energía transferida entre cuerpos por diferencia de temperatura." },
  { l:"R", t:"con", r:"Radián", d:"Unidad angular del Sistema Internacional; una vuelta completa mide 2π." },
  { l:"S", t:"con", r:"Simetría", d:"Propiedad de una figura cuyas mitades son reflejo una de otra." },
  { l:"T", t:"con", r:"Teorema", d:"Proposición que se demuestra a partir de axiomas." },
  { l:"U", t:"con", r:"Unión", d:"Operación entre conjuntos que reúne los elementos de ambos." },
  { l:"V", t:"con", r:"Vértice", d:"Punto donde se encuentran dos lados de una figura." },
  { l:"W", t:"representada", r:"Trabajo", d:"Fuerza por desplazamiento; se mide en joules." },
  { l:"X", t:"contiene", r:"Exponente", d:"Indica la cantidad de veces que se multiplica una base por sí misma." },
  { l:"Y", t:"contiene", r:"Adyacentes", d:"Ángulos que comparten vértice y un lado, sin superponerse." },
  { l:"Z", t:"representada", r:"Número atómico", d:"Cantidad de protones en el núcleo de un átomo. (Palabra compuesta.)" },
];
