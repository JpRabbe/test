import cypress from 'cypress'

describe('form testing', () => { it('should submit the form with valid input', () => { cypress.visit('http://localhost:8501/')

cypress.get('input[aria-label="taille maison"]').type('260.00');
cypress.get('input[aria-label="Nombre de chambre"]').type('2.00');
cypress.get('input[aria-label="Y a un jardin"]').type('0.00'); 

cypress.get('#prediction').should('exist');
})})

