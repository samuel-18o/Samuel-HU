// Selección de elementos
const inputNota = document.getElementById("inputNota");
const btnAgregar = document.querySelector("#btnAgregar");
const listaNotas = document.getElementById("listaNotas");

// Estado en memoria
let notas = [];

// Cargar notas al iniciar
const notasGuardadas = localStorage.getItem("notas");
if (notasGuardadas) {
  notas = JSON.parse(notasGuardadas);

  for (let i = 0; i < notas.length; i++) {
    crearLi(notas[i]);
  }

  console.log("Notas cargadas:", notas.length);
}

// Evento agregar
btnAgregar.addEventListener("click", function () {
  const texto = inputNota.value.trim();

  if (texto === "") {
    alert("La nota no puede estar vacía");
    return;
  }

  notas.push(texto);
  guardarNotas();
  crearLi(texto);

  inputNota.value = "";
  inputNota.focus();

  console.log("Nota agregada:", texto);
});

// Crear elemento li
function crearLi(texto) {
  const li = document.createElement("li");
  li.textContent = texto + " ";

  const btnEliminar = document.createElement("button");
  btnEliminar.textContent = "Eliminar";

  btnEliminar.addEventListener("click", function () {
    eliminarNota(texto, li);
  });

  li.appendChild(btnEliminar);
  listaNotas.appendChild(li);
}

// Eliminar nota
function eliminarNota(texto, li) {
  for (let i = 0; i < notas.length; i++) {
    if (notas[i] === texto) {
      notas.splice(i, 1);
      break;
    }
  }

  guardarNotas();
  listaNotas.removeChild(li);

  console.log("Nota eliminada:", texto);
}

// Guardar en Local Storage
function guardarNotas() {
  localStorage.setItem("notas", JSON.stringify(notas));
}
