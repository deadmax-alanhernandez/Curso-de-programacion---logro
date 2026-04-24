using System;

namespace numerosPares 
{    
    class contadorNumerosPares
    {
        static void Main(string [] args) 
        {Console.WriteLine("Impresor de numeros pares");
        
        contadorPares();
        }

        
        public static void contadorPares(){
            for (int it = 1; it <= 50; it++) {
            if (it % 2 == 0) {
            Console.WriteLine(it);
        }
        }
        }
    }
} 
