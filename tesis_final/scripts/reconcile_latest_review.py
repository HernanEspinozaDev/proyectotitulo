#!/usr/bin/env python3
"""Aplica correcciones editoriales reproducibles de la revisión del 03-11-2026."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT.parent / 'docskill'))
from docskill import DocSkillProject

project = DocSkillProject.open(ROOT)

path = 'appendices/c-anexo.md'
text = project.read_markdown(path)
text = text.replace('Este anexo documenta la especificación formal de los 16 casos de prueba técnicos', 'Este anexo documenta la especificación de los 16 casos de prueba técnicos')
text = text.replace('Para cada ejecución se mantiene un registro con identificador de caso, versión de código y datos sintéticos, entorno, ejecutor y evidencia.', 'Cada ejecución debería registrar identificador de caso, versión de código, datos sintéticos, entorno, ejecutor y evidencia. Esta entrega no adjunta los registros de ejecución de las pruebas descritas; por ello las fichas se presentan como casos y criterios, no como resultados certificados.')
text = text.replace('Estado: Verificado en suite local.', 'Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.')
text = text.replace('Estado: Verificado en mock.', 'Estado: Escenario de mock definido; no se adjunta un registro de ejecución reproducible en esta entrega.')
text = text.replace('Estado: Verificado en mock local.', 'Estado: Escenario de mock local definido; no se adjunta un registro de ejecución reproducible en esta entrega.')
text = text.replace('`RF-01, RF-02, UC-01 a UC-13, Flujo Crítico`', '`RF-02, RF-03, RF-05 a RF-22, UC-02 a UC-13, Flujo Crítico`')
text = text.replace('`UC-01 a UC-13, Flujo Crítico`', '`RF-02, UC-02 a UC-13, Flujo Crítico`')
text = text.replace('**Pasos:** Ejecutar el ciclo completo: registro de usuario, autenticación, exploración en catálogo, cotización, solicitud de reserva con bloqueo GiST, pago en custodia mock, aprobación, firma bilateral de contrato y check-in.', '**Pasos:** Iniciar sesión con dos cuentas sintéticas autorizadas; consultar la sesión, rehidratarla tras una recarga y comprobar que la segunda cuenta no accede a un recurso de la primera. Completar el recorrido local de publicación y sus operaciones de catálogo, y cerrar ambas sesiones. El código revisado no comprueba el rechazo de una cookie reutilizada después del cierre; esa verificación de revocación queda pendiente.')
text = text.replace('**Resultado Esperado y Aprobación:** Todas las etapas del flujo transaccional se completan de forma consistente con persistencia de estados verificable.', '**Resultado Esperado y Aprobación:** El flujo local mantiene sesión durante la rehidratación, limita los recursos a su propietario y cierra con respuesta satisfactoria. La revocación efectiva de una credencial reutilizada después del cierre debe verificarse con un paso adicional antes de declarar cumplimiento de sesión.')
text = text.replace('**Entorno y Evidencia:** Suite de pruebas Playwright automatizadas. Estado: Verificado en suite local.', '**Entorno y Evidencia:** Se identificó código de prueba en `frontend/tests/phase7-native.spec.ts` para inicio de sesión, rehidratación, aislamiento entre dos cuentas y cierre. Se inspeccionó el código, pero no se ejecutó ni se adjunta salida identificable en esta revisión; no demuestra revocación posterior al cierre.')
text = text.replace('`RNF-04, RNF-05, RNF-06, OWASP Top 10`', '`RNF-04, RNF-05, OWASP Top 10`')
text = text.replace('Estado: Verificado en suite local.', 'Estado: Procedimiento descrito; resultado de ejecución no adjunto en esta entrega.')
text = text.replace('Este catálogo integral de 16 casos de prueba (`PT-01` a `PT-16` / `CP-01` a `CP-16`) proporciona la cobertura metódica requerida para garantizar la calidad, seguridad, desempeño y conformidad regulatoria de **espaciGo**.', 'Este catálogo contiene 16 casos y criterios de prueba (`PT-01` a `PT-16` / `CP-01` a `CP-16`). Su inclusión especifica cobertura prevista; no acredita por sí sola ejecución, calidad, desempeño ni conformidad regulatoria.')
text = text.replace('## PT-13 — Prueba de Recorrido Crítico Integral (Humo E2E)', '## PT-13 — Sesión, aislamiento de cuenta y cierre (E2E local)')
text = text.replace('**Entorno y Evidencia:** Suite de pruebas Playwright automatizadas. Estado: Caso y suite de referencia identificados; no se adjunta un registro de ejecución reproducible en esta entrega.', '**Entorno y Evidencia:** Se identificó código en `frontend/tests/phase7-native.spec.ts` para login, rehidratación, aislamiento entre dos cuentas y cierre. El código inspeccionado no comprueba reutilización de la cookie después del cierre. No se ejecutó ni se adjunta salida de esta prueba; la revocación poscierre queda pendiente.')
text = text.replace('`RF-22, RF-25, UC-13, UC-14, RNF-06`', '`RF-22, RF-25, UC-13, UC-14`')
project.write_markdown(path, text)

path = 'appendices/h-anexo.md'
text = project.read_markdown(path)
text = text.replace('La matriz permite auditar el ciclo de vida del software, garantizando que cada requerimiento de negocio cuente con una materialización arquitectónica específica y un criterio de verificación ejecutable.', 'La matriz relaciona requisitos, componentes y casos de prueba propuestos o identificados. La presencia de un vínculo no acredita ejecución ni aceptación; los resultados requieren registros con versión, entorno, datos y salida.')
text = text.replace('| **RF-01** | Registro de usuarios y aceptación de términos versionados | `UC-01` | `IdentityService (Go) / Next.js Auth` | `CP-14` | Verificado en suite de autenticación local con datos sintéticos. |', '| **RF-01** | Registro de usuarios y aceptación de términos versionados | `UC-01` | `IdentityService (Go) / Next.js Auth` | — | La prueba UI identificada usa respuestas controladas; no se adjunta evidencia de registro integrado con el backend. |')
text = text.replace('| **RF-02** | Autenticación mediante sesiones seguras HttpOnly | `UC-02` | `SessionMiddleware (Go) / Cookies HttpOnly` | `CP-14` | Verificado contra secuestro de sesión y tokens SameSite en cookies. |', '| **RF-02** | Autenticación mediante sesiones seguras HttpOnly | `UC-02` | `SessionMiddleware (Go) / Cookies HttpOnly` | `CP-13` | El código E2E identificado cubre login, rehidratación, aislamiento entre cuentas y cierre; no se adjunta resultado de ejecución ni se comprueba reutilización de la cookie tras el cierre. |')
text = text.replace('La matriz permite auditar el ciclo de vida del software, garantizando que cada requerimiento de negocio cuente con una materialización arquitectónica específica y un criterio de verificación ejecutable.', 'La matriz relaciona requisitos, componentes y casos de prueba propuestos o identificados. La presencia de un vínculo no acredita ejecución ni aceptación; los resultados requieren registros con versión, entorno, datos y salida.')
text = text.replace('Establece la correspondencia biunívoca entre', 'Relaciona')
text = text.replace('| **RF-04** | Verificación de identidad KYC de arrendadores | `UC-05` | `VerificationAdapter / public.verificacion` | `CP-13, CP-14` |', '| **RF-04** | Verificación de identidad KYC de arrendadores | `UC-05` | `VerificationAdapter / public.verificacion` | `CP-13` |')
text = text.replace('| **RF-07** | Tratamiento asíncrono de imágenes WebP | `UC-09` | `MediaProcessor / deepteams/webp` | `CP-13` |', '| **RF-07** | Tratamiento asíncrono de imágenes WebP | `UC-09` | `MediaProcessor / deepteams/webp` | — |')
text = text.replace('| **RF-25** | Panel de moderación, gobierno y auditoría global GADM | `UC-14` | `GlobalAdminHandler / public.administrador_global` | `CP-07, CP-14` |', '| **RF-25** | Panel de moderación, gobierno y auditoría global GADM | `UC-14` | `GlobalAdminHandler / public.administrador_global` | `CP-07` |')
import re
text = re.sub(r'\| \*\*RF-(\d+)\*\*([^\n]*?)\| Verificado[^|]*\|', r'| **RF-\1**\2| Caso/cobertura documentado; no se adjunta registro de ejecución con versión, entorno y resultado. |', text)
text = text.replace('| **RNF-06** | Seguridad | Sesiones seguras protegidas contra secuestro | Cookies con banderas HttpOnly, Secure y SameSite=Lax | `CP-14` | Verificado: Tokens inaccesibles desde JavaScript en el DOM. |', '| **RNF-06** | Seguridad | Sesiones seguras protegidas contra secuestro | Cookies con banderas HttpOnly, Secure y SameSite=Lax | `CP-13` | La inspección estática CP-14 no prueba sesiones. La prueba E2E identificada revisa sesión, aislamiento y cierre; no aporta salida de ejecución ni prueba revocación poscierre. |')
text = text.replace('| **RNF-07** | Seguridad | Trazabilidad e inmutabilidad de eventos críticos | Tabla append-only `public.evento_auditoria_local` | `CP-07, CP-14` |', '| **RNF-07** | Seguridad | Trazabilidad e inmutabilidad de eventos críticos | Tabla append-only `public.evento_auditoria_local` | `CP-07` |')
text = text.replace('| **RNF-11** | Mantenibilidad | Arquitectura desacoplada en capas independientes | Patrón Arquitectura Hexagonal (Ports & Adapters) | `CP-01, CP-14` |', '| **RNF-11** | Mantenibilidad | Arquitectura desacoplada en capas independientes | Patrón Arquitectura Hexagonal (Ports & Adapters) | — |')
text = re.sub(r'\| \*\*RNF-(\d+)\*\*([^\n]*?)\| Verificado[^|]*\|', r'| **RNF-\1**\2| Mecanismo o criterio documentado; resultado de ejecución no adjunto. |', text)
project.write_markdown(path, text)

print('Actualizados Anexo C y Anexo H mediante DocSkillProject.')
