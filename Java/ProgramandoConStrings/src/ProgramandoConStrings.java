import java.util.Locale;

public class ProgramandoConStrings {
    public static void main(String[] args) {
/*
        String Hola = "Hola, gracias por la información";
        String Hola2 = "Hola, gracias por la información";
        String Hola1 = new String("Hola, gracias por la información");
        System.out.println(Hola);
        System.out.println(Hola1);
        System.out.println(Hola == Hola1);
        System.out.println(Hola == Hola2);
        System.out.println(Hola.equals(Hola1));


        String Saludo = "Hola, gracias por la información ";
        String Nombre = "Marco";
        String Nombre1 = "Marco";
        String SaludoPersonalizado = Saludo + Nombre;
        String SaludoPersonalizado2 = Saludo.concat("querido ").concat(Nombre);
        System.out.println(SaludoPersonalizado);
        System.out.println(SaludoPersonalizado2);

        Saludo = Saludo.transform(s -> {
            return s+"querido " + Nombre;
        });
        System.out.println(Saludo);
        Nombre1 = Nombre1.replace("a", "A");
        System.out.println(Nombre1);


        String nombre = "Marco";

        System.out.println(nombre.toUpperCase(Locale.ROOT));
        System.out.println(nombre.toLowerCase(Locale.ROOT));
        System.out.println(nombre.equals("marco"));
        System.out.println(nombre.equalsIgnoreCase("marco"));
        System.out.println(nombre.compareTo("Julian"));
        System.out.println(nombre.charAt(0));
        System.out.println(nombre.charAt(nombre.length() - 1));
        System.out.println(nombre.compareToIgnoreCase("Julian"));
        System.out.println(nombre.replace("a", "*" ));
        System.out.println(nombre.lastIndexOf('a'));
        System.out.println(nombre.indexOf("arco"));
        System.out.println(nombre.startsWith("Mar"));
        System.out.println(nombre.endsWith("co"));
        System.out.println(nombre.contains("rc"));
        System.out.println(nombre.trim()); // quita los espacios de la izquierda

 */

        String archivo = "Imagen_generica.png";
        int i = archivo.lastIndexOf(".");
        System.out.println(archivo.length());
        System.out.println(archivo.substring(i + 1));
    }
}
