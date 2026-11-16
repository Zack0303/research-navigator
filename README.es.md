# Research Navigator

**Un prompt de “director de tesis” para estudiantes de máster y doctorado.** Pégalo en cualquier chat de IA. Te ayuda a planificar un proyecto, revisar un borrador, preparar una revisión de literatura o planificar una sección, y revisa los errores que suelen costar meses.

[English](README.md) · [中文](README.zh-CN.md)

## Empieza en un minuto (sin programar)

1. Abre **[WEB-START.txt](WEB-START.txt)** ([texto sin formato para copiar](https://raw.githubusercontent.com/Zack0303/research-navigator/main/WEB-START.txt)).
2. Cópialo entero en un chat nuevo de ChatGPT, Claude, Gemini, DeepSeek u otro. Si admite archivos, súbelo. Un enlace no basta.
3. Explica lo que necesitas en tu idioma. Por ejemplo:

> Estudio un máster en Educación. Quiero investigar cómo usan los docentes las herramientas de corrección con IA, pero el tema es demasiado amplio. Tengo cuatro meses. Explícamelo en español.

Deberías recibir dos o tres preguntas clave, una dirección provisional y un siguiente paso claro. No necesitas las normas de tu universidad para empezar. Lo desconocido se marca como *desconocido*.

## Qué añade frente a preguntar a una IA sin más

Un chat normal ya detecta problemas evidentes. Research Navigator añade **seis comprobaciones** para problemas fáciles de pasar por alto, porque cada paso parece razonable por sí solo:

| Comprobación | Qué pregunta |
|---|---|
| **C1 Ancla** | ¿Se ha desviado el proyecto de lo que tú y tu director necesitáis? |
| **C2 Vecinos cercanos** | ¿Qué hacen ya los 3–5 trabajos más próximos y qué es realmente nuevo? |
| **C3 Fuerza de las afirmaciones** | ¿Alguna afirmación es más fuerte que su evidencia? |
| **C4 Criterio adecuado** | ¿Se juzga cada estudio por sus propios objetivos o con una escala única que no encaja? |
| **C5 Viabilidad con piloto** | ¿La carga de trabajo se mide con un piloto pequeño o se adivina? |
| **C6 Desconocido no es cero** | ¿Cada norma, cifra y estado tiene fuente? ¿Se separa “planificado” de “hecho”? |

**Usado en una revisión de literatura real.** El autor creó estas comprobaciones mientras escribía una revisión sistemática (2026, aún en curso) y las usó en ella. Antes, esa revisión se había ido desviando de los objetivos del grupo paso a paso, usaba una única escala de valor que juzgaba los estudios por metas que nunca tuvieron y casi presentó como novedad una clasificación ya usada. Con esta estructura le funcionó bien. La estructura incluye comprobaciones de ancla y de vecinos cercanos, búsqueda planificada con un piloto, codificación que describe antes de valorar y un guion por párrafos antes de escribir. Es la experiencia de un solo desarrollador, no un estudio independiente.

Salidas breves y compartibles: **resumen de investigación de una página**, **informe de revisión**, **hoja de preparación de revisión de literatura** y **guion por párrafos** (afirmación, evidencia, lo que no se debe decir) antes de escribir.

## Qué no hará

- Inventar artículos, citas, páginas, cifras o normas universitarias.
- Llamar “verificada” a una fuente que no ha leído en este chat.
- Redactar texto para entregar si la política de IA de tu institución es desconocida o lo prohíbe; en su lugar te dará estructura y comentarios.
- Afirmar novedad sin una búsqueda.

Prueba primero con material público o ficticio. No pegues información confidencial de empresas. Consulta las normas de IA de tu institución antes de usarla en trabajos evaluados.

## Para usuarios de agentes (Codex, Claude Code y otros)

Abre esta carpeta en tu agente y escribe: `Lee SKILL.md y sigue Research Navigator.` Ver [guía de Codex](docs/start-in-codex.md), [comprobaciones](references/checks.md), [plantillas](references/templates.md) y [guía de revisión de literatura](references/lit-review.md).

## Estado

Versión **v0.2.0-alpha**, experimental. Las pruebas con agentes están en [docs/v0.2-trial.md](docs/v0.2-trial.md). Muestran lo que las instrucciones hacen hacer a un modelo, no que sea útil para estudiantes reales. Aparte del uso del autor en una revisión real en curso, aún no hay piloto independiente con estudiantes. La calidad en español no ha sido revisada por una persona nativa. Licencia MIT.

**Se agradecen comentarios** mediante un issue, usando solo datos ficticios.
