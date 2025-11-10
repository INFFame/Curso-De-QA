from typing import Generator
import pytest
from playwright.sync_api import Playwright, Page, APIRequestContext, expect


@pytest.fixture(scope="module")
def myIds():
    keys = []
    yield keys



@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    request_context.dispose()
    
    
def test_post_todo(api_request_context: APIRequestContext, myIds) -> None:
    data = {
        "completed" : False,
        "title" : "testApi",
    }
    response = api_request_context.post(f"/todos", data=data)
    assert response.ok
    
    todos_response = response.json()

    print(f"todo Var: {response}")
    print(f"todo_response Var: {todos_response}")
    print(f"todo_response Var: {todos_response['id']}")
    
    myIds.append(todos_response['id'])
    
def test_get_todo(api_request_context: APIRequestContext, myIds) -> None:
    get_todo = api_request_context.get(f"/todos/{myIds[0]}")
    assert get_todo.ok
    
    get_response = get_todo.json()
    
    print("")
    print(f"get Var: {get_todo}")
    print(f"get_response Var: {get_response}")
    
    assert get_response['title'] == "testApi"
    assert get_response['completed'] is False
    
def test_update_todo(api_request_context: APIRequestContext, myIds) -> None:
    payload = {
        "completed" : True,
    }
    patch_todo = api_request_context.patch(f"/todos/{myIds[0]}", data=payload)
    assert patch_todo.ok
    
    patch_response = patch_todo.json()
    
    print("")
    print(f"update Var: {patch_todo}")
    print(f"update_response Var: {patch_response}")
    
    assert patch_response['title'] == "testApi"
    assert patch_response['completed'] is True    
    

#@pytest.mark.skip(reason="Just for demo purposes")
def test_delete_todo(api_request_context: APIRequestContext, myIds) -> None:
    delete_todo = api_request_context.delete(f"/todos/{myIds[0]}")
    assert delete_todo.ok
    
    delete_todo_response = delete_todo.json()
    
    print("")
    print(f"delete Var: {delete_todo}")
    print(f"delete_todo_response Var: {delete_todo_response}")
    
