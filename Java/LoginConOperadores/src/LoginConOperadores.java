import java.util.Scanner;

public class LoginConOperadores {
    public static void main(String[] args) {
/*
        String usuario = "Marco";
        String contrasenia = "12345";
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese su usuario: ");
        String u = entrada.nextLine();
        System.out.println("Ingrese su contraseña: ");
        String c = entrada.nextLine();

        if (usuario.equals(u) && contrasenia.equals(c)){
            System.out.println("Datos validos correctamente. Bienvenido");
        }
        else {
            System.out.println("Datos invalidos. Vuelva a intentarlo");
        }


        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduce tu calificación del parcial: ");
        double u = entrada.nextDouble();

        if (u < 6){
            System.out.println("Estas reprobado");
        }
        else {
            System.out.println("Estas aprobado");
        }


        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduce el primer numero: ");
        int a = entrada.nextInt();
        System.out.println("Introduce el segundo numero: ");
        int b = entrada.nextInt();
        System.out.println("Introduce el tercer numero: ");
        int c = entrada.nextInt();

        int max;
        max = (a>b)? a:b;
        max = (max>c)? max:c;
        System.out.println("El maximo entre los 3 es: "+max);


        String texto = "Hola, ¿como estas?";
        Number num = 6;

        boolean b = texto instanceof String;
        System.out.println(b);
        b = texto instanceof Object;
        System.out.println(b);
        b = num instanceof Integer;
        System.out.println(b);
        b = num instanceof Object;
        System.out.println(b);
        b = num instanceof Long;
        System.out.println(b);
        b = num instanceof Double;
        System.out.println(b);
        b = num instanceof Float;
        System.out.println(b);
        Double a = 2.56;
        b = a instanceof Double;
        System.out.println(b);

 */
        int a = 18;
        int b = 15;
        int c = 5;
        double promedio = (++a + --b + c)/3d;
        System.out.println("promedio = " + promedio);
    }
}
