const todoObject = {completed: false, id: '3', title: 'NewTodoFromPost'}
const patchObject = {completed: true, id: '3', title: 'NewTodoFromPost'}

describe('CY REQUEST DEMO', () => {
    it('POST Example', () => {
        cy
        .request('POST', '/todos', todoObject)
        .should(response => {
            expect(response.status).to.equal(201)
            expect(response.body['completed']).to.equal(false)
            expect(response.body).to.contains(todoObject)
        })
    })
    it('PATCH Example', () => {
        cy
        .request('PATCH', '/todos/3', patchObject)
        .should(response => {
            expect(response.status).to.equal(200)
            expect(response.body['completed']).to.equal(true)
            expect(response.body).to.contains(patchObject)
        })
    })
    it('DELETE Example', () => {
        cy
        .request('DELETE', '/todos/3')
        .should(response => {
            expect(response.status).to.equal(200)
        })
    })
    it('GET Example', () => {
        cy
        .request('GET', '/todos/')
        .should(response => {
            expect(response.status).to.equal(200)
        }).its('body')
        .should('have.length', 2)
    })
})
