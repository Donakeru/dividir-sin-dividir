# Ejercicios de recursividad

En esos ejercicios se demuestra mediante recursividad como realizar programas sin el uso de estados ni variables, sino que de manera recursiva y directa.  


## Participantes del Proyecto

   - Luis Miguel Viuche Madroñero (20212020082)
   - Daniel Alejandro Chave Bustos (20212020109)
   - Dilan Stive Arboleda Zambrano (20212020105)

## Descripción del Programa

### Algoritmo de Dividir sin Dividir

Para este algoritmo 


## Requisitos del Lenguaje y Entorno

### Arquitectura

- **Registro AL**: Este programa está diseñado para ejecutarse en una arquitectura basada en el conjunto de instrucciones x86. Utiliza registros como `AL` y `BL`, que son registros de 8 bits comúnmente utilizados en microprocesadores x86 para operaciones básicas.
- **Instrucciones básicas**: El programa utiliza instrucciones simples como `MOV`, `INC`, `CMP`, `JZ`, `JMP`, y `CALL`, que son comunes en la mayoría de los ensambladores de la arquitectura x86.

### Simulador utilizado

- El código está diseñado para ejecutarse en el **Simulador de Ensamblador Online** disponible en [https://exuanbo.xyz/assembler-simulator](https://exuanbo.xyz/assembler-simulator).
- Este simulador es una herramienta basada en navegador que permite probar y ejecutar código en ensamblador con una sintaxis simplificada. Está orientado a la educación y permite ejecutar programas de manera visual sin necesidad de utilizar un entorno físico o emulador más complejo.

### Sintaxis específica

- No soporta secciones de código con `section .data` o `section .text` que son típicas en otros ensambladores.
- Las etiquetas de procedimientos y direcciones como `ORG` se utilizan para definir rutinas personalizadas, y las instrucciones como `CALL` permiten saltar a esas rutinas.

### Compatibilidad

- El programa es compatible con entornos de simulación educativos y no está orientado para ser ejecutado directamente en un procesador físico sin adaptación a un ensamblador de mayor nivel como NASM o MASM, que podrían requerir configuraciones adicionales.
