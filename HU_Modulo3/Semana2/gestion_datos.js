// Objeto que almacena productos usando el id como clave
const productos = {
  1: {
    id: 1,
    nombre: "Laptop",
    precio: 3500
  },
  2: {
    id: 2,
    nombre: "Mouse",
    precio: 80
  },
  3: {
    id: 3,
    nombre: "Teclado",
    precio: 150
  }
};

// Función para validar que un producto tenga datos correctos
const validarProducto = (producto) => {
  if (
    !producto.id ||
    typeof producto.nombre !== "string" ||
    typeof producto.precio !== "number" ||
    producto.precio <= 0
  ) {
    return false;
  }
  return true;
};

// Validación de todos los productos
for (const key in productos) {
  if (!validarProducto(productos[key])) {
    console.error(`Producto inválido con id ${key}`);
  }
}

// Set con números repetidos
const numeros = new Set([1, 2, 2, 3, 4, 4, 5]);

console.log("Set inicial (sin duplicados):", numeros);

// Agregar un nuevo número
numeros.add(6);

// Verificar si un número existe
console.log("¿Existe el número 3?", numeros.has(3));

// Eliminar un número
numeros.delete(2);

// Recorrer el Set con for...of
console.log("Recorriendo el Set:");
for (const numero of numeros) {
  console.log(numero);
}

// Map que relaciona categoría con nombre de producto
const categorias = new Map();

categorias.set("Tecnología", "Laptop");
categorias.set("Accesorios", "Mouse");
categorias.set("Periféricos", "Teclado");

// for...in para recorrer el objeto de productos
console.log("Productos (for...in):");
for (const key in productos) {
  console.log(`ID: ${key}`, productos[key]);
}

// Métodos de Object
console.log("Object.keys():", Object.keys(productos));
console.log("Object.values():", Object.values(productos));
console.log("Object.entries():", Object.entries(productos));

// forEach para recorrer el Map
console.log("Categorías y productos (Map):");
categorias.forEach((producto, categoria) => {
  console.log(`Categoría: ${categoria} → Producto: ${producto}`);
});

console.log("Lista completa de productos:", productos);
console.log("Lista de números únicos (Set):", numeros);
console.log("Categorías y nombres de productos (Map):", categorias);
