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
// Final del bloque condicional

// Ejemplo utilizando la sintaxis alternativa con endif
$temperatura = 30;

if ($temperatura < 20):
    echo "Hace bastante frío.";
elseif ($temperatura >= 20 && $temperatura <= 30):
    echo "La temperatura es agradable.";
else:
    echo "Hace calor.";
endif;

?>

