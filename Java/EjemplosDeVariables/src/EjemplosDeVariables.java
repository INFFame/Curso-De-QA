import javax.swing.*;
import java.util.Scanner;

public class EjemplosDeVariables {
    public static void main(String[] args) {
/*      int edad = 7;
        int Edad = 9;
        System.out.println("Edad: " + edad);
        System.out.println("Edad: " + Edad);
        double indiceMasaCorporal = 22;
        double VALOR_PI = 3.14159;


        int a = 10;
        long b = 20;
        byte c = 25;
        System.out.println("La suma de los tres numeros es: " + (a + b + c));
        System.out.println(a/b);


        float variable = 2.5e2f;
        System.out.println("Variable: " + variable);
        double variable2 = 2.5d;
        System.out.println("Variable2: " + variable2);

        // UNICODE
        char simbolo3 = '\u0026';
        System.out.println(simbolo3);

        // ASCII
        char simbolo2 = 38;
        System.out.println(simbolo2);

        // CHAR
        char simbolo = '&';
        System.out.println(simbolo);
        char saltoDeLinea = '\n';
        char retroceso = '\b';
        char tabulador = '\t';
        char principioDeLinea = '\r';
        char nuevaPagina = '\f';
        char comillas = '\"';
        char comillaSimple = '\'';
        char barraInversa = '\\';

        boolean falso = false;
        boolean verificar = 3==2+1;
        System.out.println(verificar);

        int numero = 450;
        System.out.println("El numero es: " + numero);
        String numeroBinario = Integer.toBinaryString(numero);
        // Prefijo para binario : 0b
        System.out.println("El numero en binario: " + numeroBinario);
        System.out.println("El numero en binario escrito en JAVA: " + 0b111000010);
        // Prefijo para hexadecimal : 0x
        System.out.println("El numero en hexadecimal: " + Integer.toHexString(numero));
        System.out.println("El numero en hexadecimal escrito en JAVA: " + 0x1c2);
        // Prefijo para octal : 0
        System.out.println("El numero en octal: " + Integer.toOctalString(numero));
        System.out.println("El numero en octal escrito en JAVA: " + 0702);


        String numero = JOptionPane.showInputDialog("Ingresa um numero entero: ");
        int numeroReal = Integer.parseInt(numero);
            System.out.println("El numero es: " + numeroReal);
            System.out.println("El numero en binario: " + Integer.toBinaryString(numeroReal));
            System.out.println("El numero en hexadecimal: " + Integer.toHexString(numeroReal));
            System.out.println("El numero en octal: " + Integer.toOctalString(numeroReal));

            String resultados = "El numero es: " + numeroReal + "\nEl numero en binario: " + Integer.toBinaryString(numeroReal)
                + "\nEl numero en hexadecimal: " + Integer.toHexString(numeroReal) + "\nEl numero en octal: " + Integer.toOctalString(numeroReal);
            JOptionPane.showMessageDialog(null, resultados);


        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un numero entero: ");
        int numeroReal = entrada.nextInt();
        System.out.println("El numero es: " + numeroReal);
        System.out.println("El numero en binario: " + Integer.toBinaryString(numeroReal));
        System.out.println("El numero en hexadecimal: " + Integer.toHexString(numeroReal));
        System.out.println("El numero en octal: " + Integer.toOctalString(numeroReal));


        String booleano = "true";
        boolean booleanoConvertido = Boolean.parseBoolean(booleano);
            System.out.println(booleanoConvertido);

        String decimales = "2.56";
        double decimalesConvertidos = Double.parseDouble(decimales);
            System.out.println(decimalesConvertidos);

        String entero = "365";
        int enteroConvertido = Integer.parseInt(entero);
            System.out.println(enteroConvertido);

        String flotante = "2.56e2f";
        float flotanteConvertido = Float.parseFloat(flotante);
            System.out.println(flotanteConvertido);

        boolean cierto = true;
        String ciertoConvertido= Boolean.toString(cierto);

        int entero = 10;
        String enteroConvertido = Integer.toString(entero);

        float flotante = 2.56e2f;
        String flotanteConvertido = Float.toString(flotante);

        double decimal = 3.14;
        String decimalConvertido = Double.toString(decimal);

        String mensaje = ciertoConvertido + "\n" + enteroConvertido + "\n" + flotanteConvertido + "\n" + decimalConvertido;
        System.out.println(mensaje);

 */
        int i = 400;
        short s = (short)i;
        System.out.println(s);

        long l = i;
        System.out.println(l);

        char c = (char)i;
        System.out.println(c);
    }
}