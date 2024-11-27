from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pyswip import Prolog



app = FastAPI()
prolog = Prolog()
prolog.consult("nomina.pl") 

# agregar o eliminar docentes
class NuevoDocente(BaseModel):
    nombre: str
    categoria: str

#  onsultar salario o verificar docentes
class Docente(BaseModel):
    nombre: str

@app.post("/agregar_docente/")

def agregar_docente(docente: NuevoDocente):
    nombre_docente = docente.nombre.lower()
    categoria = docente.categoria.lower()
    
    if categoria not in ["auxiliar", "asociado", "titular"]:
        raise HTTPException(
            status_code=400, 
            detail="Categoría inválida. Debe ser 'auxiliar', 'asociado' o 'titular'."
        )
    
    try:
        if list(prolog.query(f"docente_existe({nombre_docente})")):
            raise HTTPException(
                status_code=400, 
                detail=f"El docente '{nombre_docente}' ya existe."
            )
        prolog.assertz(f"docente({nombre_docente}, {categoria})")
        return {"message": f"Docente '{nombre_docente}' agregado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al agregar el docente: {e}")

# Endpoint para calcular el salario neto de un docente
@app.post("/calculo_nomina/")
def calculo_nomina(docente: Docente):
    nombre_docente = docente.nombre.lower()
    
    try:
        
        query = f"salario_neto({nombre_docente}, SalarioNeto)"
        result = list(prolog.query(query))
        
        if result:
            salario_neto = result[0]["SalarioNeto"]
            return {"nombre": nombre_docente, "salario_neto": salario_neto}
        else:
            raise HTTPException(
                status_code=404, 
                detail=f"Docente '{nombre_docente}' no encontrado."
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al calcular la nómina: {e}")

# Endpoint para eliminar un docente
@app.delete("/eliminar_docente/")
def eliminar_docente(docente: Docente):
    nombre_docente = docente.nombre.lower()
    try:
        prolog.consult("nomina.pl")  # Recargar Prolog
        consulta_verificacion = f"docente_existe({nombre_docente})"
        consulta_eliminacion = f"eliminar_docente({nombre_docente})"
        print(f"Consulta verificación: {consulta_verificacion}")
        print(f"Consulta eliminación: {consulta_eliminacion}")
        
        if not list(prolog.query(consulta_verificacion)):
            raise HTTPException(
                status_code=404, 
                detail=f"Docente '{nombre_docente}' no encontrado."
            )
        
        prolog.query(consulta_eliminacion)
        return {"message": f"Docente '{nombre_docente}' eliminado exitosamente."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el docente: {e}")


# Endpoint para verificar si un docente existe
@app.get("/verificar_docente/{nombre}")
def verificar_docente(nombre: str):
    nombre_docente = nombre.lower()
    
    try:
        
        if list(prolog.query(f"docente_existe({nombre_docente})")):
            return {"message": f"El docente '{nombre_docente}' existe en la base de datos."}
        else:
            return {"message": f"El docente '{nombre_docente}' no existe en la base de datos."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al verificar el docente: {e}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
