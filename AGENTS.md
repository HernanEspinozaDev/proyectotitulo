# Repository Guidelines

## Structure and Sources of Truth

`Informes/` contains EspaciGo's academic reports. `ES1PT/` inside it is a closed historical delivery: preserve every source and generated document. Do not rewrite ES1 to match later decisions.

The immutable academic baseline is ES1's final report (`Informes/ES1PT/docx/build/Informe_Final.docx`) and its `Anexo_*.docx` files. New research belongs in the active delivery, such as `Informes/ES2PT/investigacion/`, and must distinguish what ES1 proposed from what later evidence verifies.

The shared entry point is `Informes/generar.py`; reusable Python modules live in `herramientas/`, APA resources and institutional profiles in `recursos/`, and new-delivery scaffolding in `plantillas/nueva_entrega/`. The ignored root `espaciGo/` directory is outside this documentation workflow.

## Context and Authoring

Read `Informes/contexto/README.md` and `decisiones.md`, then the active delivery's `contexto.md`, `pendientes.md`, `informe.json`, rubric, and relevant sections. Follow evidence links into ES1 when needed. Treat proposed architecture and integrations as proposals until implementation evidence is recorded.

Edit Markdown under each delivery's `secciones/` and `anexos/`. `informe.json` orders sections and declares annexes. Keep image paths relative to the delivery root. Never maintain edits in `build/` artifacts. Do not invent academic requirements, citations, dates, approvals, or results. Mark missing evidence with `[[PENDIENTE: ...]]`.

## Development and Validation

Use Python 3.10+; `Informes/requirements.txt` lists external prerequisites without PyPI dependencies. Word generation requires Pandoc 3.x; diagrams require Java and `PLANTUML_JAR`. Recreate relocated virtual environments rather than trusting stale paths.

```powershell
python Informes/generar.py nuevo ES3PT
python Informes/generar.py ensamblar ES2PT
python Informes/generar.py generar ES2PT
python Informes/generar.py validar ES2PT --final
python -m unittest discover -s Informes/tests -v
```

ES2 has an institutional template and an initial Markdown draft; its Word profile still needs adaptation. Follow `Informes/ES2PT/investigacion/matriz_trazabilidad_es2.md` for actual progress. Do not bypass missing or unreviewed Word profiles. Errors must return nonzero status. Test pipeline changes with focused `unittest` cases and the isolated ES1 compatibility configuration; review representative Word pages visually. Final validation blocks unresolved content and bibliography tasks; it does not replace rubric review.

## Style and Contributions

Use four-space Python indentation, `snake_case`, and uppercase constants. Preserve Spanish prose, UTF-8 accents, bibliography keys, and RQF/RNF/CU/HU identifiers. No global formatter or coverage threshold is configured.

Recent commits use concise Spanish descriptions. Keep commits focused; PRs describe affected behavior, task links, checks, unresolved warnings, and screenshots for layout changes. Never force-add ignored outputs or credentials. Notion configuration uses OAuth; see `NOTION_MCP.md`.
