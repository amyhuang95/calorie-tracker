document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('servings-form');
    const amountInput = document.getElementById('amount');
    const saveButton = document.getElementById('save-entry');
    const messageDiv = document.getElementById('message');
    
    const caloriesEl = document.getElementById('f_calories');
    const fatEl = document.getElementById('f_fat');
    const carbsEl = document.getElementById('f_carbs');
    const proteinEl = document.getElementById('f_protein');
        
    // Store initial values
    const name = document.getElementById('f_name').innerHTML;
    const id = document.getElementById('f_id').innerHTML;
    const initialCalories = parseFloat(caloriesEl.textContent.split(':')[1]);
    const initialFat = parseFloat(fatEl.textContent.split(':')[1]);
    const initialCarbs = parseFloat(carbsEl.textContent.split(':')[1]);
    const initialProtein = parseFloat(proteinEl.textContent.split(':')[1]);

    let currentServings = 1;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        currentServings = parseFloat(amountInput.value) || 1;
        
        // Update values
        caloriesEl.textContent = `Calories: ${(initialCalories * currentServings).toFixed(2)}`;
        fatEl.textContent = `Fat: ${(initialFat * currentServings).toFixed(2)}`;
        carbsEl.textContent = `Carbohydrates: ${(initialCarbs * currentServings).toFixed(2)}`;
        proteinEl.textContent = `Protein: ${(initialProtein * currentServings).toFixed(2)}`;
    });

    if (saveButton) {
        saveButton.addEventListener('click', function() {
            const calories = (initialCalories * currentServings).toFixed(2);
            const fat = (initialFat * currentServings).toFixed(2);
            const carbs = (initialCarbs * currentServings).toFixed(2);
            const protein = (initialProtein * currentServings).toFixed(2);

            fetch('{% url "save_entry" %}', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    'food_id': id,
                    'food_name': name,
                    'calories': calories,
                    'fat': fat,
                    'carbohydrates': carbs,
                    'protein': protein
                })
            })
            .then(response => response.json())
            .then(data => {
                messageDiv.textContent = data.message;
            })
            .catch(error => {
                console.error('Error:', error);
                messageDiv.textContent = 'An error occurred. Please try again.';
            });
        });
    }
});

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
