<?php
$pares = 0;
$impares = 0;

for ($it = 1; $it<=50; $it++) {
    
   if ($it % 2 == 0){
       $pares++;}
   else
   $impares++;
}
echo "\nCantidad de numeros pares: ". $pares."\n";
echo "\nCantidad de numeros impares: ". $impares."\n";

    
?>