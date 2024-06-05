<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>

</table>
</div>

<div align="center">
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>05</td><td>AÑO LECTIVO:</td><td>2024 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>

<tr><td colspan="6">INTEGRANTES:
    <ul>
        <li><P>Luis Edgar Arocutipa Gutierrez</P></li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

#

## EJERCICIOS PROPUESTOS
-   En esta tarea usted pondrá en práctica sus conocimientos de programación en Python para dibujar un tablero de Ajedrez. 
-   La parte gráfica ya está programada, usted sólo tendrá que concentrarse en las estructuras de datos subyacentes.
-   Estos objetos estarán disponibles importando la biblioteca: [chessPictures](Tarea-del-Ajedrez/chessPictures.py) y estarán internamente representados con arreglos de strings que podrá revisar en el archivo [pieces.py](Tarea-del-Ajedrez/pieces.py)
-   La clase [Picture](Tarea-del-Ajedrez/picture.py) tiene un sólo atributo: el arreglo de strings img, el cual contendrá la representación en caracteres de la figura que se desea dibujar. 
-   La clase [Picture](Tarea-del-Ajedrez/picture.py) ya cuenta con una función implementada, no debe modificarla, pero si puede usarla para implementar sus otras funciones:
    -   _invColor: recibe un color como un caracter de texto y devuelve su color negativo, también como texto, deberá revisar el archivo [colors.py](Tarea-del-Ajedrez/colors.py) para conocer los valores negativos de cada caracter.

-   La clase [Picture](Tarea-del-Ajedrez/picture.py) contará además con varios métodos que usted deberá implementar:
    1.  verticalMirror: Devuelve el espejo vertical de la imagen
    2.  horizontalMirror: Devuelve el espejo horizontal de la imagen
    3.  negative: Devuelve un negativo de la imagen
    4.  join: Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual
    5.  up: Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual
    6.  under: Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual
    7.  horizontalRepeat, Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n
    8.  verticalRepeat Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de n

-   Tenga en cuenta que para implementar todos estos métodos, sólo deberá trabajar sobre la representación interna de un Picture, es decir su atributo img.

-   Para dibujar una objeto Picture bastará importar el método draw de la biblioteca interpreter y usarlo de la siguiente manera:
    ```sh
    $ python3
    Python 3.9.2 (default, Feb 28 2021, 17:03:44) 
    [GCC 10.2.1 20210110] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    ```
    ```sh
    >>> from chessPictures import *
    >>> from interpreter import draw
    pygame 1.9.6
    Hello from the pygame community. https://www.pygame.org/contribute.html
    >>> draw(rock)
    ```

-   Ejercicios:

    -   Para resolver los siguientes ejercicios sólo está permitido usar ciclos, condicionales, definición de listas por comprensión, sublistas, map, join, (+), lambda, zip, append, pop, range.

        1.  Implemente los métodos de la clase Picture. Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en la siguiente preguntas.
        2.  Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw)

#

## SOLUCIÓN DE LOS EJERCICIOS PROPUESTOS
- Para la resolución del segundo laboratorio se creó el siguiente repositoiro en GitHub:
https://github.com/LuisArocutipa/pw2-24a/tree/main/Lab05
- Primero implementamos los archivos necesarios (colors.py, interpreter.py, picture.py, pieces.py y chessPictures.py) a la carpeta donde vamos a trabajar.
 - Comenzamos completando las funciones de la clase Picture.py:
 <br><img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.1.PNG?raw=true" style="width:30%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.2.PNG?raw=true" style="width:40%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.3.PNG?raw=true" style="width:40%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.4.PNG?raw=true" style="width:60%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.5.PNG?raw=true" style="width:40%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.6.PNG?raw=true" style="width:50%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.7.PNG?raw=true" style="width:40%; height:auto"/><br>
 <img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4.8.PNG?raw=true" style="width:40%; height:auto"/><br>
 
- Luego se crearón archivos .py e importamos las funciones y objetos necesarios para cada ejercicio propuesto:

<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e1.PNG?raw=true" style="width:70%; height:auto"/><br>
<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e2.PNG?raw=true" style="width:70%; height:auto"/><br>
<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e3.PNG?raw=true" style="width:50%; height:auto"/><br>
<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e4.PNG?raw=true" style="width:70%; height:auto"/><br>
<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e5.PNG?raw=true" style="width:70%; height:auto"/><br>
<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e6.PNG?raw=true" style="width:70%; height:auto"/><br>
<img src="https://github.com/LuisArocutipa/Pweb-Lab4/blob/main/Imagenes/4e7.PNG?raw=true" style="width:70%; height:auto"/><br>

#

## PREGUNTA

- ¿Para qué sirve el directorio pycache?
    - La función principal del directorio "pycache" es proporcionar un lugar específico para almacenar los archivos de bytecode generados por el intérprete de Python. Almacenar estos archivos en un directorio separado ayuda a mantener organizado el árbol de directorios del proyecto y evita la saturación del directorio principal con archivos ".pyc".