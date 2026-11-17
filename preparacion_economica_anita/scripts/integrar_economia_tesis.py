"""Integra la edición económica conservando la estructura TIHI84 de la tesis."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'preparacion_economica_anita/07_texto_para_tesis'
TESIS = ROOT / 'tesis_final'


def adapt(text):
    # El cuerpo de la tesis usa numeración correlativa de tablas (1–13 existentes).
    text = re.sub(r'\bTabla 14\.(\d+)\b', lambda m: 'Tabla ' + str(13 + int(m[1])), text)
    text = re.sub(r'\bTablas 14\.(\d+) y 14\.(\d+)\b', lambda m: 'Tablas '+str(13+int(m[1]))+' y '+str(13+int(m[2])), text)
    # Un párrafo de rótulo y título con salto de línea, como las otras tablas TIHI84.
    text = re.sub(r'(\*\*Tabla [\d.H]+\*\*)\n\n(\*[^\n]+\*)', r'\1\\\n\2', text)
    # La bibliografía general se produce desde el manifiesto y el Capítulo XVII.
    text = re.sub(r'\(Sapag Chain & Sapag Chain, 2008, (pp?\.[^)]+)\)', r'[@es2sapag2008, \1]', text)
    text = re.sub(r'Sapag Chain y Sapag Chain \(2008, (pp?\.[^)]+)\)', r'@es2sapag2008 [\1]', text)
    text = text.replace('Sapag Chain y Sapag Chain (2008)', '@es2sapag2008')
    text = text.replace('NIC Chile (2026)', '@es2nictarifas')
    return text


def main():
    body = (SOURCE / 'capitulo_xiv_evaluacion_economica.md').read_text()
    annex = (SOURCE / 'anexo_h_evaluacion_economica.md').read_text()
    body = body.replace('# Capítulo XIV Evaluación económica de espaciGo', '# CAPÍTULO XIV: Factibilidad Económica')
    headings = {
        '## 14. Factibilidad económica': '## 14. Factibilidad Económica',
        '### 14.1. Estudio de mercado y modelo de ingresos': '### 14.1. Estudio de Mercado',
        '### 14.2. Inversión y costos del proyecto': '### 14.2. Costos del Proyecto',
        '#### 14.2.1. Recursos e inversión preoperativa': '#### 14.2.1. Recursos',
        '#### 14.2.2. Presupuesto de operación': '#### 14.2.2. Adquisiciones',
        '### 14.3. Flujos de caja proyectados': '### 14.3. Flujo de Caja',
        '### 14.4. Indicadores de rentabilidad': '### 14.4. Indicadores de Rentabilidad Financiera (VAN, TIR y Payback)',
        '### 14.5. Sensibilidad y volumen de equilibrio': '### 14.5. Análisis de Sensibilidad y Escenarios',
    }
    for before, after in headings.items():
        body = body.replace(before, after)
    body = body.replace('### 14.1. Estudio de Mercado\n\n',
        '### 14.1. Estudio de Mercado\n\nEl Capítulo I contextualiza la vacancia del mercado de oficinas de Santiago. Su alcance corresponde a ese segmento y no se extrapola al conjunto de categorías de espaciGo. El Canvas del Capítulo V relaciona los segmentos, el servicio y su estructura de costos e ingresos.\n\n')
    body = body.replace('### 14.5. Análisis de Sensibilidad y Escenarios',
        'El escenario base no recupera la inversión dentro del horizonte evaluado. En los volúmenes de quiebre, el período de recuperación simple varía entre 2,708 y 4,006 años, y el descontado entre 4,017 y 4,018 años. La medición incluye la liquidación final cuando corresponde y utiliza interpolación entre los momentos financieros. La Tabla H.13.2 detalla cada meta de asignación.\n\n### 14.5. Análisis de Sensibilidad y Escenarios')
    annex = annex.replace('# Anexo H Evaluación económica detallada',
        '# ANEXO H: MEMORIA DE CÁLCULO ECONÓMICO Y EVALUACIÓN FINANCIERA DETALLADA')
    annex = annex.split('\n## Referencias\n', 1)[0]
    (TESIS / 'sections/14-capitulo-xiv.md').write_text(adapt(body).rstrip() + '\n')
    (TESIS / 'appendices/h-evaluacion-economica-detallada.md').write_text(adapt(annex).rstrip() + '\n')
    print('Capítulo XIV y Anexo H integrados; estructura TIHI84 y flujos conservados.')


if __name__ == '__main__':
    main()
