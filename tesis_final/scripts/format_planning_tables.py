"""Tablas de planificación legibles sin alterar las tablas de otros capítulos."""
from format_economic_tables import child,text,W
import re

def format_planning_tables(body):
    section=body.find(W+'sectPr');m=section.find(W+'pgMar');width=int(section.find(W+'pgSz').get(W+'w'))-int(m.get(W+'left'))-int(m.get(W+'right'))
    active=False;count=0
    for node in body:
        if node.tag==W+'p':
            v=text(node)
            if active and re.match(r'^EDT 1\.\d\.\d',v):
                child(child(node,'pPr'),'keepNext')
                child(child(node,'pPr'),'keepLines')
                nxt=node.getnext()
                if nxt is not None and nxt.tag==W+'p':child(child(nxt,'pPr'),'keepNext')
            if v.startswith(('CAPÍTULO ','ANEXO ','Material Complementario')):active=v.startswith(('CAPÍTULO VI:','ANEXO G:'))
            continue
        if not active or node.tag!=W+'tbl':continue
        count+=1;rows=node.findall(W+'tr');cols=len(rows[0].findall(W+'tc'));first=text(rows[0].findall(W+'tc')[0])
        if cols==4:
            if first=='Criterio de selección':weights=[.28,.09,.25,.38]
            elif first=='ID / EDT':weights=[.17,.48,.20,.15]
            elif first=='ID':
                second=text(rows[0].findall(W+'tc')[1])
                weights=[.09,.26,.18,.47] if second=='Riesgo' else [.09,.29,.48,.14]
            elif first=='Frente':weights=[.32,.226,.227,.227]
            elif first=='Integrante':weights=[.32,.23,.26,.19]
            else:weights=[.10,.28,.18,.44]
        elif cols==3:weights=[.24,.33,.43]
        else:weights=[.28,.72]
        widths=[round(width*x) for x in weights];widths[-1]+=width-sum(widths)
        for col,size in zip(node.find(W+'tblGrid'),widths):col.set(W+'w',str(size))
        props=child(node,'tblPr');child(props,'tblW').attrib.update({W+'w':str(width),W+'type':'dxa'})
        padding=child(props,'tblCellMar')
        for edge,size in [('top',35),('bottom',35),('left',65),('right',65)]:child(padding,edge).attrib.update({W+'w':str(size),W+'type':'dxa'})
        for ix,row in enumerate(rows):
            child(child(row,'trPr'),'cantSplit')
            for cell,size in zip(row.findall(W+'tc'),widths):
                child(child(cell,'tcPr'),'tcW').attrib.update({W+'w':str(size),W+'type':'dxa'})
                for pp in cell.iter(W+'p'):
                    pr=child(pp,'pPr');child(pr,'spacing').attrib.update({W+'before':'0',W+'after':'0',W+'line':'240',W+'lineRule':'auto'})
                    # Tablas de hasta trece filas se conservan con su nota.
                    if len(rows)<=13:child(pr,'keepNext')
                for run in cell.iter(W+'r'):
                    rp=child(run,'rPr');child(rp,'sz').set(W+'val','19');child(rp,'szCs').set(W+'val','19')
    return count
