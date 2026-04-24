<?php
$numero = 8;
$intento = 0;
$contador = 0;

while ($intento != $numero) {
    $intento++; 
    $contador++;
    echo "Intento $contador: ¿Es el $intento?\n";
        if ($intento != $numero) {
            echo "el numero $intento no era el numero secreto\n";
        }
}

echo "El número era $numero. Total de intentos: $contador.";
?>