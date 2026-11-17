"""Ajusta las tablas de evidencia y procedimientos sin partir su última fila."""
from format_economic_tables import W,child,text

def format_review_tables(body):
    section=body.find(W+'sectPr');m=section.find(W+'pgMar');width=int(section.find(W+'pgSz').get(W+'w'))-int(m.get(W+'left'))-int(m.get(W+'right'))
    count=0
    for node in body:
        if node.tag!=W+'tbl':continue
        caption=node.getprevious()
        if caption is None or not text(caption).startswith(('Tabla 11','Tabla 13')):continue
        label=text(caption)
        weights=[.10,.43,.47] if label.startswith('Tabla 11') else [.13,.42,.45]
        sizes=[round(width*x) for x in weights];sizes[-1]+=width-sum(sizes)
        rows=node.findall(W+'tr');assert len(rows[0].findall(W+'tc'))==3
        for col,size in zip(node.find(W+'tblGrid'),sizes):col.set(W+'w',str(size))
        pr=child(node,'tblPr');child(pr,'tblW').attrib.update({W+'w':str(width),W+'type':'dxa'})
        padding=child(pr,'tblCellMar')
        for edge,size in [('top',35),('bottom',35),('left',65),('right',65)]:child(padding,edge).attrib.update({W+'w':str(size),W+'type':'dxa'})
        for row in rows:
            child(child(row,'trPr'),'cantSplit')
            for cell,size in zip(row.findall(W+'tc'),sizes):
                child(child(cell,'tcPr'),'tcW').attrib.update({W+'w':str(size),W+'type':'dxa'})
                for paragraph in cell.iter(W+'p'):
                    pp=child(paragraph,'pPr');child(pp,'keepNext');child(pp,'spacing').attrib.update({W+'before':'0',W+'after':'0',W+'line':'240',W+'lineRule':'auto'})
                for run in cell.iter(W+'r'):
                    rp=child(run,'rPr');child(rp,'sz').set(W+'val','19');child(rp,'szCs').set(W+'val','19')
        count+=1
    assert count==2,count
    return count
