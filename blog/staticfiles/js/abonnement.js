document.addEventListener('DOMContentLoaded', function() {
    // Sélectionnez tous les boutons d'abonnement
    const abonnerButtons = document.querySelectorAll('.btn-abonner');
    
    abonnerButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const offreId = this.getAttribute('data-offre-id');
            const messageContainer = this.closest('.ps-item').querySelector('.abonnement-message');
            
            // Désactiver le bouton pendant la requête
            this.disabled = true;
            
            fetch(`/abonner/${offreId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                credentials: 'same-origin'
            })
            .then(response => response.json())
            .then(data => {
                if(data.message) {
                    // Succès
                    messageContainer.innerHTML = `
                        <div class="alert alert-success">
                            ${data.message}
                            <br>Offre: ${data.offre_titre}
                        </div>
                    `;
                    // Optionnel : masquer le bouton ou modifier son état
                    this.style.display = 'none';
                } else if(data.error) {
                    // Erreur
                    messageContainer.innerHTML = `
                        <div class="alert alert-danger">
                            ${data.error}
                        </div>
                    `;
                }
            })
            .catch(error => {
                console.error('Erreur:', error);
                messageContainer.innerHTML = `
                    <div class="alert alert-danger">
                        Une erreur est survenue. Veuillez réessayer.
                    </div>
                `;
            })
            .finally(() => {
                // Réactiver le bouton
                this.disabled = false;
            });
        });
    });

    // Fonction pour récupérer le cookie CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});