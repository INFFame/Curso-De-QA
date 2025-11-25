// Importar modulo de sistema de ficheros y rutas
import * as fs from 'fs';
import * as path from 'path';

// Definir un tipo para los usuarios
type User = { username: string, password: string };

/* 
    Lee un CSV con columna username,password y devuelve un array de usuarios.
*/

export function readCSV(csvPath: string): User[] {
    // * Si la ruta es absoluta la usamos, si no la convertimos a absoluta mediante path.join con el directorio de trabajo actual (process.cwd()).
    // * Esto asegura que fs.readFileSync reciba una ruta correcta independientemente de cómo pases la ruta.
    const absolute = path.isAbsolute(csvPath) ? csvPath : path.join(process.cwd(), csvPath); 

    // * Leer el contenido del archivo de forma síncrona (bloqueante) como texto UTF-8
    const content = fs.readFileSync(absolute, { encoding: 'utf8' });

    // * Separar el contenido en líneas (split), quitar espacios alrededor (trim) y filtrar líneas vacías (filter(Boolean))
    // * Resultado: array de líneas no vacías y sin espacios sobrantes
    const lines = content.split(/\r?\n/).map(l => l.trim()).filter(Boolean);

    if (lines.length === 0) return []; // ! Si el archivo está vacío o solo tiene líneas vacías, devolvera array vacío

    // * Tomar la primera línea (cabecera), dividir por comas y normalizar cada campo (trim + toLowerCase)
    const header = lines[0].split(',').map(h => h.trim().toLowerCase());

    // * Buscar los indices de las columnas 'username' y 'password' en la cabecera
    const userIdIndex = header.indexOf('username');
    const passIdIndex = header.indexOf('password');

    // ! Si no se encuentran ambas cabeceras, lanzar un error
    if (userIdIndex === -1 || passIdIndex === -1) {
        throw new Error('El CSV debe incluir las cabeceras "username" y "password".');
    }

    // * Array para acumular los usuarios parseados (username + password)
    const users: User[] = [];

    // * Iterar sobre las líneas despues de la cabecera
    for (let i = 1; i < lines.length; i++) {
        // * Dividir cada línea en columnas por coma y trim a cada columna
        const cols = lines[i].split(',').map(col => col.trim());

        // ! Si la fila no tiene la cantidad de columnas segun los índices, se salta.
        // * Ejemplo: si userIdIndex=0 y passIdIndex=1, cols.length debe ser > 1
        if (cols.length <= Math.max(userIdIndex, passIdIndex)) continue;

        // * Agregar un objeto User con los valores extraídos de las columnas indicadas
        users.push({ username:cols[userIdIndex], password: cols[passIdIndex] });

    }

    // * Devolver el array con los usuarios parseados (username + password)
    return users;
 
}

// * Exportar la función por defecto para facilitar su importación a otros archivos.
export default readCSV;