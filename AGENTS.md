# Repository Guidelines

## Structure and Sources of Truth

`Informes/` contains EspaciGo's academic reports. `ES1PT/` inside it is a closed historical delivery: preserve every source and generated document. Do not rewrite ES1 to match later decisions.

The immutable academic baseline is ES1's final report (`Informes/ES1PT/docx/build/Informe_Final.docx`) and its `Anexo_*.docx` files. New research belongs in the active delivery, such as `Informes/ES2PT/investigacion/`, and must distinguish what ES1 proposed from what later evidence verifies.

The shared entry point is `Informes/generar.py`; reusable Python modules live in `herramientas/`, APA resources and institutional profiles in `recursos/`, and new-delivery scaffolding in `plantillas/nueva_entrega/`. The ignored root `espaciGo/` directory is outside this documentation workflow.

## Context and Authoring

Read `Informes/contexto/README.md` and `decisiones.md`, then the active delivery's `contexto.md`, `pendientes.md`, `informe.json`, rubric, and relevant sections. Follow evidence links into ES1 when needed. Treat proposed architecture and integrations as proposals until implementation evidence is recorded.

For ES2, apply Law 21.719 as a design criterion from the first development increment, using the treatment matrix in `Informes/ES2PT/anexos/B_diccionario_datos.md` and planned test PT-16. Its effective date is 1 December 2026; distinguish design work from legal applicability and proven compliance.

ES2 retains all rental-space categories from ES1. Investigate pricing, duration, capacity, demand, and transaction costs by category; `INV-011_muestra_precios_y_demanda.md` records the current evidence. The single-ticket bootstrap simulation is provisional, not a market average or a decision to restrict the product to one pilot category.

Edit Markdown under each delivery's `secciones/` and `anexos/`. `informe.json` orders sections and declares annexes. Keep image paths relative to the delivery root. Never maintain edits in `build/` artifacts. Do not invent academic requirements, citations, dates, approvals, or results. Mark missing evidence with `[[PENDIENTE: ...]]`.

Annex letters are data-driven: they come from the order of the `anexos` array in `informe.json`, which must follow the order of first reference in the body. ES2 was reordered to A = evaluación económica, B = diccionario de datos, C = catálogo de casos de prueba; when an annex moves, update its letter in every body and annex reference. Lowercase `anexo A/B/C/D/E` always points to the frozen ES1 annexes and must never be renumbered. The technical sample selects its annex by file name, not by letter.

Cite only primary sources in the report: never cite the internal `INV-*.md` registers or the frozen ES1 baseline as author–year sources. Mention the prior delivery in prose ("la entrega anterior") and cite the original sources it was based on. After any citation change, regenerate the Word and verify on the render that no `INV-0xx` mention and no ES1 self-citation remain (`INV-019` records the convention).

## Development and Validation

For parallel ES2 research, use `python Informes/coordinar.py contexto`, inspect `tablero`, and reserve a free task with `tomar --agente <unique-instance-name>` before editing its files. The versioned task list is `Informes/ES2PT/coordinacion/tareas.json`; `bitacora.md` records who took each task and progress, while the ignored SQLite database holds live reservations. Read the prior summary on takeover, record `avance`, and `finalizar` or `liberar` with a concrete handoff. Do not edit files reserved by another agent. Research tasks write distinct INV files; `ES2-INTEGRAR` owns shared body, bibliography, and pending-list edits after its dependencies finish. See [coordination guide](Informes/ES2PT/coordinacion/README.md). Agents in different worktrees must point `INFORMES_COORD_DB` to the same local database to coordinate live claims.

For ES2, prioritize research, body text and annexes. By user instruction, defer all Word/PDF rendering, APA field experiments, profile approval and visual checks until the content is complete, or the user explicitly requests them. Do not repeat these checks after each writing task. Keep `perfil_es2.json` unapproved until the user explicitly requests the Word closure; it was approved on 24-09-2026 by express user decision, with the render review recorded in `INV-020`. During drafting, use lightweight Markdown/source checks and focused arithmetic checks when calculations change.

Economic analysis follows `Informes/ES2PT/investigacion/INV-009_evaluacion_economica.md` and its editable assumptions. Preserve commission revenue versus third-party funds, cash versus opportunity cost, and hypothetical scenarios versus quotations. The reusable personal skill is `$evaluacion-proyectos-chile`; the repository calculator is `Informes/herramientas/evaluacion_economica.py` and needs no Word or external packages.

Use Python 3.10+; `Informes/requirements.txt` lists external prerequisites without PyPI dependencies. Word generation requires Pandoc 3.x; PlantUML requires Java and `PLANTUML_JAR`, while SVG diagrams require Inkscape. Recreate relocated virtual environments rather than trusting stale paths.

```powershell
python Informes/generar.py nuevo ES3PT
python Informes/generar.py ensamblar ES2PT
python Informes/generar.py generar ES2PT
python Informes/generar.py validar ES2PT --final
python -m unittest discover -s Informes/tests -v
```

ES2 has an institutional template and a Markdown draft; its Word profile remains disabled pending the final visual review. Follow `Informes/ES2PT/investigacion/matriz_trazabilidad_es2.md` for actual progress. Do not bypass missing or unreviewed Word profiles. Errors must return nonzero status. Test pipeline changes with focused `unittest` cases; reserve isolated ES1 compatibility and visual Word checks for the final validation phase. Final validation blocks unresolved content and bibliography tasks; it does not replace rubric review.

## Style and Contributions

Use four-space Python indentation, `snake_case`, and uppercase constants. Preserve Spanish prose, UTF-8 accents, bibliography keys, and RQF/RNF/CU/HU identifiers. No global formatter or coverage threshold is configured.

Recent commits use concise Spanish descriptions. Keep commits focused; PRs describe affected behavior, task links, checks, unresolved warnings, and screenshots for layout changes. Never force-add ignored outputs or credentials. Notion configuration uses OAuth; see `NOTION_MCP.md`.
