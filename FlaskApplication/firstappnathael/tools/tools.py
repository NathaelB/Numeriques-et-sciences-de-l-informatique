import traceback
def nom_fonction_en_cours():
    return traceback.format_stack()[-2].split("\n")[0].split('in ')[1]


def orderby(get_value : str)->str :
    """"""
    if get_value is not None:
        return f" ORDER BY {get_value}"
    else :
        return ""


def pagination(datas:list,page_en_cours,data_par_page,view,**kwargs):
    nb_pages = len(datas)//data_par_page
    if len(datas)%data_par_page>0:
        nb_pages+=1
    page_en_cours = max(page_en_cours,1)
    page_en_cours = min(page_en_cours,nb_pages)
    debut = (page_en_cours-1)*data_par_page
    fin=debut+data_par_page
    pagination ='<ul class ="pagination" >'
    previous = "Previous"
    next = "Next"
    col = len(datas[0])
    home = ""
    end = ""
    case = min(nb_pages,6)
    if kwargs.get("previous","")!="":
        previous = kwargs.get("previous")
    if kwargs.get("next","")!="":
        next = kwargs.get("next")
    if kwargs.get("case","")!="":
        case = kwargs.get("case")
    if kwargs.get("home","")!="":
        home = kwargs.get("home")
    if kwargs.get("end","")!="":
        end = kwargs.get("end")
    case = min(nb_pages, case)
    datas = list(datas)
    for i in range(nb_pages*data_par_page-len(datas)):
        datas.append(("" for i in range(col)))

    if home!="":
        disabled = " disabled" if page_en_cours<=1 else ""
        pagination += f'<li class ="page-item{disabled}"><a class ="page-link" href="{url_for(view,page=0)}">{home}</a > </li>'
    if page_en_cours<=1:
        pagination += f'<li class ="page-item disabled"><a class ="page-link" href="#">{previous}</a > </li>'
    else:
        pagination += f'<li class ="page-item"><a class ="page-link" href="{url_for(view,page=page_en_cours-1)}">{previous}</a > </li>'
    for i in range(1,case+1):
        if page_en_cours < case // 2+case%2 :
            active = " active" if i==page_en_cours else ""
            pagination += f'<li class ="page-item{active}"> <a class ="page-link" href="{url_for(view,page=i)}"> {i} </a > </li>\n'
        elif case//2+case%2<=page_en_cours<=nb_pages-case//2:
            active = " active" if i == case//2+case%2 else ""
            pagination +=f'<li class ="page-item{active}"> <a class ="page-link" href="{url_for(view,page=page_en_cours+i-case//2-case%2)}"> {page_en_cours+i-case//2-case%2} </a > </li>\n'
        else:
            active = " active" if i == case-(nb_pages-page_en_cours) else ""
            pagination +=f'<li class ="page-item{active}"> <a class ="page-link" href="{url_for(view,page=nb_pages-case+i)}"> {nb_pages-case+i} </a > </li>\n'
    if page_en_cours >= nb_pages:
        pagination += f'<li class ="page-item disabled"><a class ="page-link" href="#">{next}</a > </li>'
    else:
        pagination += f'<li class ="page-item"> <a class ="page-link" href="{url_for(view,page=page_en_cours+1)}">{next}</a> </li>'
    if end!="":
        disabled = " disabled" if page_en_cours >= nb_pages else ""
        pagination += f'<li class ="page-item{disabled}"><a class ="page-link" href="{url_for(view,page=nb_pages)}">{end}</a > </li>'
    pagination+="\n</ul>"
    print("nb page",nb_pages)
    return {"datas":datas[debut:fin],"pagination":pagination}