<?php

int $a[5][1] = 20 ;
float $b[5][1] = 20 ;
double $b[5][1] = 20 ;

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
final class Coche{
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

class CocheAzul implements Coche{
    
}

// Uso de métodos
echo $miCoche->obtenerDescripcion(); // Este coche es un Toyota Corolla de color Rojo.


// Definición de una función que suma dos números y devuelve el resultado
function sumar($a, $b) {
    // Calcula la suma
    $resultado =  ceil(9.4);
    
    // Devuelve el resultado de la suma
    return $resultado;
}

$pepe = clone $resultado;
print("ola");
echo ceil(2.1);
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

goto a;


$var1 = 5;
$var2 = 1;
echo "vaa2 es mayor a var1";

a: 

class ko extends Exception{}

try {
    throw new ko("a");
    print("Hello");
} catch (ko $a) {
    //throw $th;
}finally{
    //throw $x;
}


trait message1 {
    public function msgA() {
      echo "My favorite color is red. ";
    }
  
    public function msgB() {
      echo "My favorite number is 5. ";
    }
  }
  
  trait message2 {
    public function msgA() {
      echo "My favorite color is blue. ";
    }
  
    public function msgB() {
      echo "My favorite number is 7. ";
    }
  }
  
  class MyClass {
    use message1, message2 {
      message1::msgA insteadof message2;
      message2::msgB insteadof message1;
    }
  }



  $marks = 78; 
  
  $res = match (true) { 
      $marks < 33 => 'Fail', 
      $marks < 45 => 'Third Division', 
      $marks < 60 => 'Second Division', 
      $marks < 75 => 'First Division', 
      $marks <= 100 => 'Distinction',
  }; 

  declare(ticks = 1);
?>

