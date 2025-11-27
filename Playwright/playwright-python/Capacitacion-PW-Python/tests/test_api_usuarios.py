from playwright.sync_api import APIRequestContext

# Test 1: Obtener la lista de usuarios y verificar el estado de la respuesta
def test_obtener_usuario_por_id(api_context: APIRequestContext):
    # Realizar una solicitud GET para obtener los usuarios
    response = api_context.get("/users")
    
    # Validar el codigo de estado de la respuesta
    assert response.ok
    
    # Validar el contenido de la respuesta
    assert "application/json" in response.headers["content-type"]
    
    # Validar la cantidad de usuarios en la respuesta
    usuarios = response.json()
    assert len(usuarios) == 10
    print(f"\nUsuarios obtenidos: {usuarios}")
    
# Test 2: Agregar un nuevo usuario y verificar la respuesta
def test_agregar_nuevo_usuario(api_context: APIRequestContext):
    # Datos del nuevo usuario a agregar
    nuevo_usuario = {
        "name": "Juan Perez",
        "username": "JuanP",
        "email": "juan.perez@example.com",
        "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
        }
    }
    
    # Realizar una solicitud POST para agregar el nuevo usuario
    response = api_context.post("/users", data=nuevo_usuario)
    
    # Validar el codigo de estado de la respuesta
    assert response.ok
    
    # Validar el contenido de la respuesta
    usuario_creado = response.json()
    assert usuario_creado["name"] == nuevo_usuario["name"]
    
    # Imprimir el ID del nuevo usuario creado
    print(f"\nID del nuevo usuario creado: {usuario_creado['id']}")
    print(f"El nombre del nuevo usuario creado: {usuario_creado['name']}")

# Test 3: Actualizar un usuario existente y verificar la respuesta
def test_actualizar_usuario_existente(api_context: APIRequestContext):
    # Datos actualizados del usuario
    usuario_actualizado = {
        "name": "Juan Perez Actualizado",
        "username": "JuanPActualizado",
        "email": "juan.perez.actualizado@example.com",
    }
    
    # Realizar una solicitud PATCH para actualizar el usuario con ID 11
    response = api_context.patch("/users/11", data=usuario_actualizado)
    
    # Validar el codigo de estado de la respuesta
    assert response.ok
    
    # Validar el contenido de la respuesta
    usuario = response.json()
    assert usuario["name"] == usuario_actualizado["name"]
    
    # Imprimir los datos del usuario actualizado
    print(f"\nUsuario actualizado: {usuario}")
    
# Test 4: Eliminar un usuario y verificar la respuesta
def test_eliminar_usuario(api_context: APIRequestContext):
    # Realizar una solicitud DELETE para eliminar el usuario con ID 11
    response = api_context.delete("/users/11")
    
    # Validar el codigo de estado de la respuesta
    assert response.ok
    
    # Imprimir mensaje de confirmación
    print("\nUsuario eliminado correctamente.")