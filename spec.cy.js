describe('empty spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8501/')
    cy.get('#pr-diction-de-prix-de-maison')
  })
})