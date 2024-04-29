<?php

$edad = 25;

// Inicio del bloque condicional
if ($edad < 18) {
    echo "Eres menor de edad.";
} elseif ($edad >= 18 && $edad <= 65) {
    echo "Eres un adulto.";
} else {
    echo "Eres un adulto mayor.";
}

?>

