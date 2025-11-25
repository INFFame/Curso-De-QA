describe('UI-DEMO', ()=>{
    beforeEach(()=>{
        cy.visit('/')
    })
    it('ADD a todo', () => {
        cy.get('#add-todo').type('test-todo{enter}')
        cy.get('.view label').eq(2).should('have.text','test-todo')
    });

    it('DELETE a todo', () => {
        cy.get('.destroy').eq(2).click({force: true})
    });
})