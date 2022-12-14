describe('empty spec', () => {
  it('passes', () => {
    cy.visit('http://localhost:8501/')
    cy.get('#pr-diction-de-prix-de-maison').should('exist');
  })
})

describe('form testing', () => {
  it('should submit the form with valid input', () => {
    cy.visit('http://localhost:8501/')

    cy.get('input[aria-label="Taille maison"]').clear().type('260.00');
    cy.get('input[aria-label="Nombre de chambre"]').clear().type('2.00');
    cy.get('input[aria-label="Y a un jardin"]').clear().type('0.00'); 

    // cy.get('#prediction').should('exist');
    cy.get('#pr-diction-de-prix-de-maison').should('exist');
  })
})
