
// Pedir al usuario que ingrese su nombre
const nombre = prompt("Digite su nombre");

// Pedir al usuario que ingrese su edad
let edad = prompt("Digite su edad");

// Convertir la edad a número
edad = Number(edad);  

// Validar
if (isNaN(edad)) {
    console.error("Error: Por favor, ingresa una edad válida en números.");
} else {
    if (edad < 18) {
        alert(`Hola ${nombre}, eres menor de edad.`);
    } 
    else {
        alert(`Hola ${nombre}, eres mayor de edad.`);
    }
}
