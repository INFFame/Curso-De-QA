describe('Spiando una API', () => {
    beforeEach(() => {
        cy.visit('/')
    });

    it('Add new todo by UI', function(){
        cy.intercept('POST', '/todos').as('newTodo')

        cy.get('input#add-todo').type('new-todo{enter}')

        cy.wait('@newTodo').its('response.statusCode').should('eq', 201)

        cy.get('@newTodo').should(request => {
            cy.log(request)
            expect(request.response.body.title).to.eql('new-todo')

            const newTodoID = request.response.body.id

            cy.wrap(newTodoID).as('newTodoID')
        })
    })

    after(function(){
        cy.request('DELETE', `/todos/${this.newTodoID}`)
    })
});