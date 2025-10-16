import * as fs from 'fs';                // Importa el módulo de sistema de ficheros de Node.js (lectura/escritura de archivos).
import * as path from 'path';            // Importa el módulo para manejar rutas (unir, comprobar si es absoluta, etc).

type User = { username: string; password: string }; // Define un tipo TypeScript para representar un usuario (username + password).

/**
 * Lee un CSV simple con cabecera `username,password` y devuelve un array de usuarios.
 * Ignora líneas vacías y trim de valores.
 */
export function readUsersCsv(csvPath: string): User[] {
  const absolute = path.isAbsolute(csvPath) ? csvPath : path.join(process.cwd(), csvPath);
  // Si `csvPath` ya es absoluta la usamos; si no, la convierto a absoluta usando el directorio de trabajo actual (process.cwd()).
  // Esto garantiza que `fs.readFileSync` reciba una ruta correcta independientemente de cómo pases la ruta.

  const content = fs.readFileSync(absolute, { encoding: 'utf8' });
  // Lee de forma síncrona el contenido del archivo como texto UTF-8.
  // Nota: la versión síncrona bloquea el hilo; para scripts de test esto suele ser aceptable.

  const lines = content.split(/\r?\n/).map(l => l.trim()).filter(Boolean);
  // Separa el texto en líneas (compatible con Windows y Unix), quita espacios alrededor de cada línea (trim)
  // y filtra las líneas vacías (filter(Boolean) elimina strings vacíos).
  // Resultado: array de líneas no vacías y sin espacios sobrantes.

  if (lines.length === 0) return [];
  // Si el archivo estaba vacío (o solo tenía líneas vacías) devolvemos un array vacío.

  const header = lines[0].split(',').map(h => h.trim().toLowerCase());
  // Toma la primera línea (cabecera), la divide por comas y normaliza cada campo: trim + toLowerCase.
  // Así aceptamos cabeceras como "Username" o " username " y las tratamos igual.

  const userIdx = header.indexOf('username');
  const passIdx = header.indexOf('password');
  // Buscamos el índice de las columnas 'username' y 'password' en la cabecera.
  // userIdx/passIdx serán -1 si la cabecera correspondiente no existe.

  if (userIdx === -1 || passIdx === -1) {
    throw new Error('CSV debe incluir cabeceras "username" y "password"');
  }
  // Si no se encuentran ambas cabeceras, lanzamos un error claro para que el consumidor sepa qué falta.

  const users: User[] = [];
  // Array donde iremos acumulando los usuarios parseados.

  for (let i = 1; i < lines.length; i++) {
    const cols = lines[i].split(',').map(c => c.trim());
    // Para cada línea (desde la segunda, i=1), la dividimos en columnas por coma y trim a cada columna.

    // si la fila no tiene suficientes columnas la ignoramos
    if (cols.length <= Math.max(userIdx, passIdx)) continue;
    // Si la fila no tiene suficientes columnas para contener username o password (según los índices) la saltamos.
    // Ejemplo: si userIdx=0 y passIdx=1, cols.length debe ser > 1.

    users.push({ username: cols[userIdx], password: cols[passIdx] });
    // Agregamos un objeto User con los valores extraídos de las columnas indicadas.
  }

  return users;
  // Devolvemos el array con todos los usuarios parseados.
}

export default readUsersCsv; // Export por defecto para facilitar imports desde otros ficheros.