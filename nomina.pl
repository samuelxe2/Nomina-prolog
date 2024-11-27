% Declaración de predicados dinámicos
:- dynamic docente/2.

% Definición del salario mínimo
salario_minimo(1000000).

% Base de datos inicial de docentes
docente(juan_perez, auxiliar).
docente(maria_rodriguez, asociado).
docente(carlos_gomez, titular).

% Asignación de salario según el cargo
salario_por_cargo(auxiliar, Salario) :-
    salario_minimo(SalarioMinimo),
    Salario is SalarioMinimo * 1.

salario_por_cargo(asociado, Salario) :-
    salario_minimo(SalarioMinimo),
    Salario is SalarioMinimo * 2.

salario_por_cargo(titular, Salario) :-
    salario_minimo(SalarioMinimo),
    Salario is SalarioMinimo * 3.

% Cálculo de deducciones
deduccion_salud(SalarioBase, DeduccionSalud) :-
    DeduccionSalud is SalarioBase * 0.04.

deduccion_pension(SalarioBase, DeduccionPension) :-
    DeduccionPension is SalarioBase * 0.04.

% Cálculo de bonificaciones
bonificacion(auxiliar, SalarioBase, Bonificacion) :-
    Bonificacion is SalarioBase * 0.05.

bonificacion(asociado, SalarioBase, Bonificacion) :-
    Bonificacion is SalarioBase * 0.1.

bonificacion(titular, SalarioBase, Bonificacion) :-
    Bonificacion is SalarioBase * 0.15.

% Cálculo del salario neto
salario_neto(NombreDocente, SalarioNeto) :-
    docente(NombreDocente, Categoria),
    salario_por_cargo(Categoria, SalarioBase),
    deduccion_salud(SalarioBase, DeduccionSalud),
    deduccion_pension(SalarioBase, DeduccionPension),
    bonificacion(Categoria, SalarioBase, Bonificacion),
    SalarioNeto is SalarioBase - DeduccionSalud - DeduccionPension + Bonificacion.


% Validar si un docente existe
docente_existe(NombreDocente) :-
    docente(NombreDocente, _).


% Eliminar un docente
eliminar_docente(NombreOriginal) :-
    normalizar_nombre(NombreOriginal, NombreNormalizado),
    (   retract(docente(NombreNormalizado, _))
    ->  true
    ;   format('Error: El docente ~w no existe.~n', [NombreNormalizado])
    ).

