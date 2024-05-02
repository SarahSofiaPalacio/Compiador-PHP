<?php

interface MyInterface {
    public function myMethod();
}

trait MyTrait {
    public function myTraitMethod() {
        // Some code
    }
}

class UseTrait{
    use MyTrait;
}


$mensaje = "Esta es una cadena
multilínea";

// Definición de la clase
class Coche {
    // Propiedades
    public $marca;
    public $modelo;
    public $color;

    // Método Constructor
    public function __construct($marca, $modelo, $color) {
        $this->marca = $marca;
        $this->modelo = $modelo;
        $this->color = $color;
    }

    // Método
    public function obtenerDescripcion() {
        return "Este coche es un $this->marca $this->modelo de color $this->color.";
    }
}

// Instanciación de la clase
$miCoche = new Coche("Toyota", "Corolla", "Rojo");

// Uso de métodos
echo $miCoche->obtenerDescripcion(); // Este coche es un Toyota Corolla de color Rojo.


// Definición de una función que suma dos números y devuelve el resultado
function sumar($a, $b) {
    // Calcula la suma
    $resultado = $a + $b;

    // Devuelve el resultado de la suma
    return $resultado;
}

$b ? $a = 5 : $a = 3; 
// Llamada a la función y almacenamiento del valor devuelto en una variable
$suma = sumar(5, 3);

// Imprimir el valor devuelto
echo "La suma de 5 y 3 es: $suma\n";

$F = 5;
$hola = 3;
function factorial ()
{
    $hola=5;
}

if ($b>0)
{
    $p=1; 
    while($p<=100){
        $q=$q+1;

    }
}
else{
        for($p=0;$p<100; $p++){
            $c=$c+1;
        } 
 /* soy un comentario de varias lineas
  y no me creo mucho*/
    }

$numeros = [1,2,3,4,5];
foreach($numeros as $numero)
{
    echo $numero;
}
switch($a)
{
    case 1: 
        $a=$b;
        break;
    case 2: 
        $a=$c;
        break;
    case 3: 
        $c=$a+$b;
        break;
    default: 
        $a=0;
        break;            
}

function fibonaci($i)
{
   if($i == 0)
   {
      return 0;
   }
   if($i == 1)
   {
      return 1;
   }
   return fibonaci($i-1) ;
}

$var1 = 5;
$var2 = 1;
echo "vaa2 es mayor a var1";


class ko extends Exception{}

try {
    throw new ko("a");
    print("Hello");
} catch (ko $a) {
    //throw $th;
}finally{
    //throw $x;
}


?>
