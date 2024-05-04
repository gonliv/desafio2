from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.prefetch_related('subtareas').all()
    return list(tareas)

def crear_nueva_tarea(descripcion, estado):
    tarea = Tarea.objects.create(descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id, descripcion, estado):
    tarea = Tarea.objects.get(id=tarea_id)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion, estado=estado)
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.get(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.get(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(arreglo):
    for tarea in arreglo:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for subtarea in tarea.subtareas.all():
            print(f".... [{subtarea.id}] {subtarea.descripcion}")