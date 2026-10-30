# Documentación del proyecto · Aprender a cambiar (historia y práctica de la TCC)

Registro de qué se construyó, con qué criterios, qué decisiones se tomaron y cómo seguir editándolo. Pensado para retomar el trabajo en otra sesión (humana o con Claude) sin reconstruir el contexto.

---

## 1. Qué es

Un sitio de una sola página (`index.html`) con un **scrollytelling** pedagógico sobre la historia y, sobre todo, la práctica clínica de la terapia cognitivo-conductual. Lector previsto: estudiante de psicología o persona interesada sin formación previa en TCC. Español rioplatense; el término técnico original en inglés aparece entre paréntesis la primera vez.

Plantilla de diseño y de mecánica: el proyecto equivalente sobre psicoanálisis (`~/Projects/sandbox/clinica1_fund_PsA`, publicado en `https://pasquinell.github.io/clinica1_fund_PsA/`). Se reutilizó su arquitectura (scrollies con `data-s`, barra de tiempo, índice automático, recuadros) con paleta, tipografía y contenido propios.

URL prevista: `https://pasquinell.github.io/tcc_terapia/` (repo `Pasquinell/tcc_terapia`, Pages desde `main` / `(root)`). Si el repo se llama distinto, cambia la URL.

## 2. Archivos

| Ruta | Qué es |
|---|---|
| `index.html` | **Fuente única de verdad.** HTML, CSS y JS inline, ~460 KB. |
| `img/` | Ocho retratos con licencia libre; detalle y créditos en `../README.md`. |
| `.nojekyll` | Evita que GitHub Pages procese el sitio con Jekyll. |
| `.gitignore` | Excluye `doc/tools/out/` (salidas de prueba). |
| `README.md` | Presentación del repo y créditos de imágenes. |
| `doc/README.md` | Este archivo. |
| `doc/tools/check.py` | Chequeos estáticos: balance de etiquetas, `data-s` vs. pasos, ids duplicados, enlaces internos rotos, imágenes ausentes. |
| `doc/tools/figs_preview.py` | Genera páginas con los 33 diagramas en estado final (claro u oscuro) para revisar solapamientos. |
| `doc/tools/cdp.mjs` | Chrome headless por DevTools: scroll real, capturas, errores de JS y desborde horizontal. |

Durante la construcción el HTML se armó concatenando partes en un directorio temporal (cabecera, introducción, una o dos partes por ola, cierre, script). Esas partes **ya no existen**: desde ahora se edita `index.html` directamente.

## 3. Pedido original (resumen)

- Archivo local para GitHub Pages, no artefacto de Claude. Autonomía máxima.
- Recorrido: Parte 0 (qué es la TCC, las «tres olas» y su crítica, cómo usar el sitio, línea de tiempo), Parte 1 (bases experimentales), Parte 2 (primera ola), Parte 3 (segunda ola), Parte 4 (tercera ola), Parte 5 (cierre: hilos, tabla comparativa, evidencia y críticas, cómo reconocer un modelo, árbol genealógico).
- **Requisito central:** cada modelo terapéutico, desde Wolpe, explica su cura con seis puntos (malestar, mejoría, mecanismo propuesto frente a investigación posterior, técnicas y sesión típica, caso, evidencia y límites).
- Todo sale de la web: sin datos, fechas ni citas inventadas; ⚑ literal verificada, ≈ paráfrasis; fuentes con enlace por bloque y bibliografía general.
- Temporalidad: no usar vocabulario posterior para explicar etapas anteriores; «Anticipación» con fecha y «Recontextualización» al volver atrás o cambiar de ola.
- Sólo imágenes de dominio público o con licencia libre, con crédito.
- Casos históricos con problemas éticos (Albert, terapias aversivas) con su crítica; ninguna terapia como panacea; aviso visible de material educativo y cómo buscar ayuda sin números locales.

## 4. Estructura del contenido

26 bloques numerados (ids semánticos), más secciones de apoyo:

**Parte 0 · Introducción** (`hero`, `como-usar`, `que-es`, `olas` con línea de tiempo en scrolly).

**Parte 1 · Bases experimentales**: 1 `pavlov` (dos scrollies: EI/RI/EC/RC y generalización; curva de adquisición, extinción y recuperación espontánea), 2 `thorndike`, 3 `watson` (Albert, con recuadro ético y debate sobre su identidad), 4 `jones` (Peter, escala de 17 pasos), 5 `skinner` (contingencia A-B-C y moldeamiento; cuatro cuadrantes; programas de refuerzo), repaso `r1` (tabla concepto de laboratorio → técnica clínica, como anticipación).

**Parte 2 · Primera ola**: 6 `eysenck` (1952 y el rótulo «terapia de conducta»), 7 `wolpe`, 8 `mowrer` (con recontextualización: es anterior a Wolpe), 9 `exposicion` (EPR, Meyer 1966, curva de ansiedad, jerarquía para TOC, Foa y Kozak, Craske), 10 `aba` (análisis funcional de un caso, fichas, contingencias), 11 `bandura`, 12 `aversivas` (cronología crítica hasta la resolución APA 2021), repaso `r2`.

**Parte 3 · Segunda ola**: 13 `kelly`, 14 `ellis` (ABCDE, hoja ficticia), 15 `beck` (modelo cognitivo en 7 pasos, estructura de sesión, diálogo publicado con «Abe», registro de pensamientos), 16 `meichenbaum`, 17 `clark` (síntesis TCC y modelos por trastorno; círculo del pánico; hoja de experimento), 18 `esquemas` (Young y Protocolo Unificado, presentados como herederos fuera del período), repaso `r3`.

**Parte 4 · Tercera ola**: 19 `terceraola`, 20 `act` (hexaflex en 8 pasos, diálogo ficticio), 21 `dbt` (teoría biosocial y módulos; análisis en cadena), 22 `mbct`, 23 `ba`, 24 `fap`, 25 `mct` (terapia metacognitiva y terapia centrada en la compasión, dos scrollies), 26 `pbt` (terapia basada en procesos y TCC digital), repaso `r4`.

**Parte 5 · Cierre**: `hilos` (cinco hilos), `comparativa` (tabla de 16 modelos), `evidencia` (scrolly de tamaños de efecto, Dodo, alianza, críticas, cómo leer la División 12), `arbol` (árbol genealógico en scrolly), `reconocer` (pistas observables), `ayuda`, `bibliografia`, pie.

### Anatomía de cada bloque

1. Encabezado: número, chips (años, lugar o autores, tema), título.
2. **Dónde estamos** (contexto) y **El problema** (la pregunta que el autor resuelve).
3. **Scrollytelling**: pasos a un lado, diagrama SVG fijo al otro.
4. Material clínico: caso publicado o ilustrativo (`.call.caso`, con `.ficticio` cuando es inventado), diálogo (`.dialogo`), hoja de registro (`table.tb`), jerarquía (`ul.jer`), secuencia de sesión (`.sesion`).
5. **Ficha del modelo** (`.ficha`): los seis puntos, con «Lo que mostró la investigación» separado del mecanismo propuesto.
6. Recuadros **Anticipación** (`.call.ant`), **Recontextualización** (`.call.rec`), **Nota**, **Ética** (`.call.etica`).
7. Citas (`blockquote`): traducción propia, original en inglés (`p.orig`), referencia y marca ⚑ o ≈.
8. **Errores frecuentes** (`.errores`).
9. **Autoevaluación** con respuesta desplegable (`details.preg`).
10. **Fuentes de este bloque** (`details.fuentes`).

Cifras: 26 bloques, 33 scrollies con diagrama, 26 preguntas de autoevaluación, 19 fichas de modelo (incluida una ficha crítica de las terapias aversivas) más una ficha breve de la terapia basada en procesos, 8 anticipaciones, 9 recontextualizaciones, 29 citas ⚑ y 5 ≈.

## 5. Decisiones de contenido

- **«Olas» como mapa discutido.** Se presentan como herramienta didáctica propuesta por Hayes (2004) y discutida (Hofmann y Asmundson 2008, Öst 2008, Hayes y Hofmann 2017). La regla de tiempo muestra las tres franjas superpuestas.
- **Orden pedido vs. cronología.** Se respetó el orden del pedido. Mowrer (1939-1960) va después de Wolpe (1958) con un recuadro de recontextualización; la terapia de esquemas y el Protocolo Unificado (posteriores a 1990) se presentan en la Parte 3 como herederos, con aviso explícito.
- **Temporalidad.** Ejemplos de anticipaciones marcadas: exposición y aprendizaje inhibitorio en la Parte 1; creencias nucleares e intermedias (J. Beck, 1995) dentro del bloque de Beck; diálogo socrático como «descubrimiento guiado» (Padesky, 1993); habituación como indicador (Foa y Kozak, 1986) y aprendizaje inhibitorio (Craske, 2008/2014) en el bloque de exposición; el estudio de componentes de Jacobson (1996) como recontextualización en Beck.
- **Casos.** Publicados: Albert, Peter, Meyer (1966), Ayllon y Azrin (1965), Iwata (1982), Öst (1989), Higgins (1993), «Abe» (transcripción del Beck Institute), ensayos citados con cifras. Ilustrativos y rotulados ficticios: Martín (REBT), registro de pensamientos, Sofía (exámenes), hoja de experimento de pánico, esquema de abandono, Tomás (análisis funcional), Lucía (modelado y ACT), Camila (análisis en cadena), Marcos (MBCT), Sofía (activación), Pablo (FAP), Ana (metacognitiva), Julián (compasión).
- **Correcciones encontradas al verificar** (no repetir los errores):
  - El artículo de Hofmann y Asmundson (2008) se titula «Acceptance and mindfulness-based therapy: New wave or old hat?».
  - El párrafo de Hayes (2004) que define la tercera ola no está en el resumen de PubMed: se cita como texto del artículo, reproducido por el propio Hayes en la FAQ de la ACBS.
  - Ellis cita a Epicteto con «People are disturbed…» (no «Men»).
  - Nobel de Pávlov (1904): por la fisiología de la digestión. La «campana» es mayormente folclore; en sus protocolos predominan metrónomos y tonos.
  - Albert: siete emparejamientos; nunca descondicionado; los autores sabían con un mes de anticipación que se iba. Identidad disputada (Merritte o Barger).
  - MBSR duraba 10 semanas en 1982; el formato de 8 es posterior. MBCT no redujo recaídas con sólo dos episodios previos (Teasdale 2000).
  - Ehlers y otros (2003): TEPT en el seguimiento 11 % con terapia cognitiva, 61 % con folleto, 55 % con evaluaciones repetidas.
  - División 12 (revisado en octubre de 2026): sólo la EPR para TOC conserva «Strong» con el criterio de 2015; el resto de las fichas citadas tiene «Strong» con el de 1998 y figura pendiente de reevaluación.
- **Imágenes.** Sin retratos de Skinner, Wolpe, Linehan ni Hayes: no hay imágenes con licencia clara en Commons. El retrato de Beck es de 1942 (21 años): es el único de dominio público disponible.

## 6. Diseño

- Paleta «cuaderno de laboratorio»: papel frío `#f2f1ec` con cuadrícula en la portada, tinta azul noche `#141b26`. Acentos: cobalto `--cob` (primera ola), ámbar `--amb` (segunda), verde mar `--sea` (tercera), bermellón `--ver` (alertas, errores, riesgos), violeta `--vio` (cierre, procesos), pizarra `--sla` (laboratorio). Variables `--w0`…`--w5` por parte.
- Tipografías (Google Fonts): **Instrument Serif** (títulos), **Literata** (cuerpo), **Space Grotesk** (etiquetas y diagramas). Sin conexión caen a Georgia / system-ui.
- Modo oscuro automático por `prefers-color-scheme` y botón (se guarda en `localStorage` con try/catch).
- Responsive: en ≤ 900 px el diagrama queda fijo arriba (máx. 50 vh) y los pasos pasan por debajo; en ≤ 820 px se ocultan la regla y el aviso «avanza N años».

## 7. Cómo funciona el código

Todo inline en `index.html`.

**Scrollytelling** (`.scrolly`, o `.scrolly flip` para el diagrama a la izquierda):

```html
<div class="scrolly">
  <div class="steps">
    <div class="step"><div class="sc"><h5>1 · Título</h5><p>…</p></div></div>
  </div>
  <div class="fig"><div class="frame">
    <svg viewBox="0 0 600 430" role="img" aria-label="Descripción del diagrama">
      <g data-s="1">…aparece en el paso 1…</g>
      <path pathLength="1" class="lv draw" data-s="3" d="…"/>   <!-- se dibuja en el paso 3 -->
      <g data-s="2" data-off="3" class="fade">…se atenúa desde el paso 3…</g>
    </svg>
    <div class="cap">Pie</div>
  </div></div>
</div>
```

- Un `IntersectionObserver` por scrolly dispara el recálculo cuando una tarjeta cruza la franja de lectura; el paso activo es **el último cuyo borde superior ya pasó la línea** (58 % de la altura en escritorio, 78 % en móvil). Se calcula así, y no con la entrada del observador, porque con scroll rápido las entradas llegan en lote y desordenadas (se detectó en la prueba móvil).
- Todo elemento con `data-s ≤ paso activo` recibe `.on`. Con `data-off="N"` y `class="fade"`, se atenúa desde el paso N.
- **Regla:** el `data-s` máximo no puede superar la cantidad de `.step` (lo verifica `check.py`).
- Vocabulario SVG: cajas `.box .boxs .bk .ba .bs .bv .bi .bl`; líneas `.ln .lnd .lk .la .ls .lv .li .lg`; rellenos `.fk .fa .fs .fv .fvi .fi .fi2 .fl`; texto `.ti .sm .xs .ser` y colores `.tK .tA .tS .tV .tI .tC`; flechas `marker-end="url(#ar|#ark|#ara|#ars|#arv|#ari|#arg)"` (definidas una vez al inicio del `<body>`). Un `<g class="xs">` achica todos sus textos.

**Barra de tiempo:** cada sección con `data-title`, `data-parte` (0-5) y opcionalmente `data-year` actualiza el año (el rótulo sale del primer `.chip.yr`), mueve el punto sobre la regla 1890-2025 (con las tres franjas de olas), deja un fantasma en la posición anterior y muestra «→ avanza / ↩ vuelve N años». El mapa `PARTES` del script define color, rótulo corto y nombre de cada parte.

**Índice:** se genera con los elementos que tienen `data-toc`, agrupados por `data-parte`.

**Agregar un bloque:** copiar una `<section class="bloque" id="…" data-year="…" data-title="…" data-parte="…" data-toc="…">` y respetar la anatomía del punto 4. Después correr las verificaciones.

## 8. Verificación realizada

- `check.py`: balance de etiquetas OK; 33 scrollies sin desajustes de `data-s`; sin ids duplicados, enlaces internos rotos ni imágenes ausentes.
- `figs_preview.py` (claro y oscuro): revisados los 33 diagramas en estado final; se corrigieron unos 25 solapamientos (textos sobre líneas o cajas, flechas que cruzaban etiquetas, un bucle recortado por el borde) y un error general de CSS (los textos dentro de `<g class="xs">` no se achicaban).
- `cdp.mjs` con scroll real a 1400×900 y 390×844: 0 errores de JS, sin desborde horizontal (`scrollWidth` = ancho de ventana), diagrama fijo arriba en móvil, barra de tiempo y paso activo correctos. Se corrigió el cálculo del paso activo (ver punto 7).

Reproducir (desde la raíz):

```bash
python3 -I doc/tools/check.py
python3 -I doc/tools/figs_preview.py            # o: ... figs_preview.py dark
google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=1360,1700 \
  --virtual-time-budget=4000 --screenshot=figs_0.png "file://$PWD/doc/tools/out/figs_0.html"
node doc/tools/cdp.mjs "file://$PWD/index.html" shot 1400 900 "beck:2600" "act:5000"
node doc/tools/cdp.mjs "file://$PWD/index.html" mob 390 844 "dbt:3600"
```

(`cdp.mjs` necesita Node ≥ 22 y `google-chrome`; cada argumento es `idDeSección:desplazamientoEnPx`.)

## 9. Datos no confirmados o con fuentes en conflicto

Se presentan con matiz en el texto o se dejaron fuera:

- Cifras de Wolpe (≈ 90 % de mejoría): sólo fuentes secundarias; se aclara que son series sin control.
- Rango de la escala SUDS (0-100 o 0-10): las fuentes difieren; se mencionan ambos.
- Definición literal de inhibición recíproca: vista en una tesis de 1967 que la reproduce, no en el libro (marcada ≈).
- Porcentajes del ensayo de Bandura, Blanchard y Ritter (1969): de un manual universitario (aviso en el pie del diagrama).
- Fecha del experimento de Shenger-Krestovnikova (publicado en 1921; algunas fuentes dicen 1914).
- Cambios de nombre de la terapia de Ellis (RET hacia 1961; REBT 1992 o 1993).
- Lista exacta de distorsiones de Beck por año; origen exacto de «empirismo colaborativo»; columnas del registro de 1979 (por eso el registro se rotula «formato habitual en los manuales actuales»).
- Nombres exactos de los módulos del Protocolo Unificado (se aclara que varían entre ediciones).
- Fases del entrenamiento autoinstruccional de Meichenbaum y Goodman: descripción estándar de la literatura, no cotejada con el artículo de 1971.
- Redacción original de las cinco reglas de FAP y niveles de validación de DBT (no se citan literalmente).
- Duración de sesiones de MBCT y de grupos de DBT (no se dan cifras salvo las de NICE y Behavioral Tech).
- Influencia directa de Kelly sobre Beck o Ellis: no documentada; se presenta como paralelo.

## 10. Pendientes y límites conocidos

- Las citas ≈ conviene cotejarlas con los originales antes de reutilizarlas entre comillas.
- Tamaño de letra de los diagramas en móvil: legible pero chico (igual que en el proyecto de psicoanálisis).
- Las fuentes dependen de Google Fonts.
- No hay retratos de Skinner, Wolpe, Linehan ni Hayes.
- La revisión de calificaciones de la División 12 es de octubre de 2026 y puede cambiar.

## 11. Publicación en GitHub Pages

Configuración de la máquina (ya hecha, no tocar): `github.com` usa la cuenta de trabajo; el alias SSH `github-pasquinell` usa la cuenta personal **Pasquinell**; un `includeIf` global firma como `Pasquinell <purbanir@gmail.com>` en repos con ese remoto.

1. En Brave, logueado como **Pasquinell**, crear en github.com un repo **vacío** (sin README ni licencia), por ejemplo `tcc_terapia`.
2. En esta carpeta:

```bash
git init -b main
git remote add origin git@github-pasquinell:Pasquinell/tcc_terapia.git
git config user.email          # debe mostrar purbanir@gmail.com; si no, parar
git add .
git commit -m "Sitio inicial: historia y práctica de la TCC"
git push -u origin main
```

3. En GitHub: *Settings → Pages → Build and deployment → Source: Deploy from a branch → main / (root) → Save*. En 1-2 minutos queda en `https://pasquinell.github.io/tcc_terapia/`.

No usar `git@github.com:Pasquinell/...` ni `https://github.com/Pasquinell/...`: fallan o entran con la cuenta equivocada. Comprobar cuentas: `ssh -T git@github-pasquinell` → «Hi Pasquinell!».

`doc/` se publica junto con el sitio. Si no se quiere público, agregarlo a `.gitignore` antes del primer commit.
