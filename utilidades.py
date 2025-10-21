import json
import functools


def calcular_frecuencia(texto):
    tiempos = (365*24*3600,30*24*3600,7*24*3600,24*3600,3600,60,1)
    partes = map(lambda x: int(x[:-1]), texto.split(":"))
    total_seg = functools.reduce(lambda acc,x: acc+x[0]*x[1],zip(tiempos,partes))
    return total_seg


def leer_jobs(path):
    trabajos_json = []
    with open(path, "r") as f:
        trabajos_json = json.loads(f.read())

    trabajos = []
    for i,j in enumerate(trabajos_json):
        trabajos.append({
            "id": i,
            "run": j["run"],
            "frecuencia":calcular_frecuencia(j["frecuencia"]) 
        })

    return trabajos