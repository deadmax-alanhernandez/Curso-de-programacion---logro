using System;

namespace CuentaRegresiva
{    
    class CuentaRegresiva10
    {
        static void Main(string[] args) 
        {
            Console.WriteLine("Cuenta regresiva");
            Regresiva();

        }

        public static void Regresiva()
        {
            int contador = 10;
            while (contador >= 1) 
            {
                Console.WriteLine(contador);
                contador--;
            }
            Console.WriteLine("¡Despegue! ");
        }
    }
} 