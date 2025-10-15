public class ProgramarConOperadores {
    public static void main(String[] args) {
/*
        // operadores aritmeticos
        int a = 5,b = 7;
        int suma = a+b;
        int resta = a-b;
        int multiplicacion = a*b;
        float division = (float)a / (float)b;
        int resto = a%b;
        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Multiplicacion: " + multiplicacion);
        System.out.println("Division: " + division);
        System.out.println("Resto: " + resto);


        // Operadores Aritmeticos de asignacion

        int i = 5;
        int j = i + 2;
        i += 2;
        System.out.println(i);
        i -= 4;
        System.out.println(i);
        i *= 3;
        System.out.println(i);


        // Operadores Unarios
        int i = -2;
        int j = -i;
        System.out.println(j);
        int k = -4;
        int m = +k;
        System.out.println(m);


        // Operadores aritmeticos de incremento y decremento
        int a = 5;
        // incrementa en uno y luego devuelve el numero
        int b = ++a;
        System.out.println(b);
        // devuelve el numero y luego incrementa en uno
        a = 5;
        int c = a++;
        System.out.println(c);

        // decrementa en uno y luego devuelve el numero
        a = 5;
        int d = --a;
        System.out.println(d);

        // devuelve el numero y luego decrementa en uno
        a = 5;
        int e = a--;
        System.out.println(e);


        // Operadores relacionales
        int a = 7, b = 5;
        boolean mentira= false;
        boolean r1 = (a==b);
        System.out.println(r1);
        boolean r2 = !r1;
        System.out.println(r2);
        boolean r3 = (a!=b);
        System.out.println(r3);
        boolean r4 = (true==mentira);
        System.out.println(r4);
        boolean r5 = true!=mentira;
        System.out.println(r5);
        boolean r6 = (a<b);
        System.out.println(r6);
        boolean r7 = a>b;
        System.out.println(r7);
        boolean r8 = a<=b;
        System.out.println(r8);
        boolean r9 = a>=b;
        System.out.println(r9);

        int a = 7, b = 5;
        boolean mentira = false;
        boolean r1 = a < b || a == b;
        System.out.println(r1);
        boolean r2 = a > b || a == b;
        System.out.println(r2);
        boolean r3 = a > b && a == b;
        System.out.println(r3);
        boolean r4 = a > b && mentira == false;
        System.out.println(r4);
*/
        int a = 7, b = 5;
        boolean mentira = false;
        boolean r1 = (a > b || a == b) || (mentira == false);
        System.out.println(r1);
        boolean r2 = ((a > b && mentira == true) || (a == b && a < b)) && (mentira == false);
        System.out.println(r2);


    }
}
