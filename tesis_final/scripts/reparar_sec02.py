#!/usr/bin/env python3
"""Script de reparacion de sections/02-modelamiento.md"""
from pathlib import Path

workspace = Path('/home/nandev/Documentos/projects/espaciGo/ES2/informe_docskill')
sec02_p = workspace / 'sections/02-modelamiento.md'

backup_p = Path('/home/nandev/Documentos/projects/espaciGo/ES2/Informe_Desarrollo_e_Implementacion_espaciGo_ES2.backup_pre_h01_h25.md')
backup_text = backup_p.read_text(encoding='utf-8')
backup_lines = backup_text.splitlines()

idx_start_21 = -1
idx_end_212 = -1
for i, l in enumerate(backup_lines):
    if '### 2.1 Modelamiento de procesos de negocio' in l:
        idx_start_21 = i
    if '#### 2.1.3 Proceso BPMN 3' in l and idx_start_21 != -1:
        idx_end_212 = i
        break

print(f'Backup 2.1 lines: {idx_start_21} to {idx_end_212}')
bpmn_text_part1 = '\n'.join(backup_lines[idx_start_21:idx_end_212])

bpmn_text_part1 = bpmn_text_part1.replace('### 2.1 Modelamiento de procesos de negocio', '## 2.1 Modelamiento de procesos de negocio (BPMN)')
bpmn_text_part1 = bpmn_text_part1.replace('#### 2.1.1 Proceso BPMN 1: Reserva, custodia financiera (Escrow), firma contractual y operación del arriendo', '### 2.1.1 Proceso BPMN 1: Flujo de Reserva, Custodia Financiera (Escrow), Firma Contractual y Operación de Arriendo')
bpmn_text_part1 = bpmn_text_part1.replace('#### 2.1.2 Proceso BPMN 2: Acreditación de identidad (KYC/KYB), publicación multimedia WebP y moderación global', '### 2.1.2 Proceso BPMN 2: Acreditación de Identidad (KYC/KYB), Publicación Multimedia WebP y Moderación Global')
bpmn_text_part1 = bpmn_text_part1.replace('figuras/fig01_bpmn_reserva_escrow_operacion.png', 'assets/figuras/fig01_bpmn_reserva_escrow_operacion.png')
bpmn_text_part1 = bpmn_text_part1.replace('figuras/fig02_bpmn_publicacion_kyc_moderacion.png', 'assets/figuras/fig02_bpmn_publicacion_kyc_moderacion.png')

current_text = sec02_p.read_text(encoding='utf-8')
current_lines = current_text.splitlines()

idx_proc3 = -1
for i, l in enumerate(current_lines):
    if '### 2.1.3 Proceso BPMN 3' in l:
        idx_proc3 = i
        break

print(f'Current 2.1.3 starts at line: {idx_proc3}')

idx_first_22 = -1
idx_second_22 = -1
for i, l in enumerate(current_lines):
    if l.strip() == '## 2.2 Especificación de los casos de uso':
        if idx_first_22 == -1:
            idx_first_22 = i
        else:
            idx_second_22 = i
            break

print(f'Current 2.2 occurrences at: {idx_first_22} and {idx_second_22}')

new_parts = []
new_parts.append('# 2. Modelamiento de la solución')
new_parts.append(bpmn_text_part1.strip())

proc3_block = '\n'.join(current_lines[idx_proc3:idx_first_22]).strip()
new_parts.append(proc3_block)

rest_block = '\n'.join(current_lines[idx_second_22:])

triple_header = '''### B. Diccionario de Datos de Entidades Transaccionales Principales

### B. Diccionario de Datos de Entidades Transaccionales Principales

### B. Diccionario de Datos de Entidades Transaccionales Principales'''
clean_header = '### B. Diccionario de Datos de Entidades Transaccionales Principales'
rest_block = rest_block.replace(triple_header, clean_header)

rest_block = rest_block.replace(
    '`uq_espacio_periodo_gist`',
    '`EXCLUDE USING gist (espacio_id WITH =, intervalo WITH &&) WHERE (activo)`'
)

new_parts.append(rest_block)

final_sec02 = '\n\n'.join(new_parts) + '\n'
sec02_p.write_text(final_sec02, encoding='utf-8')
print(f'sections/02-modelamiento.md reescrito con exito. Total lineas: {len(final_sec02.splitlines())}')
