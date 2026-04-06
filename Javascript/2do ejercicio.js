const nombreProducto = "Tablet 10 pulgadas";

let precio = 450.99;
let stock = 25;

const envioGratis = true;

let cantidad = 2
const subtotal = precio * cantidad;
const total = (subtotal + (subtotal*= 0.07));
total = parseFloat(total.toFixed(2));
console.log("El subtotal de la compra son: ", subtotal, "dolares, el precio total sumando el impuesto es: ", total)