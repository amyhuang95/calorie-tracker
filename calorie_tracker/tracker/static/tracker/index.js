document.addEventListener('DOMContentLoaded', function() {
    // Display search button in homepage
    const startBtn = document.querySelector('#start-btn');
    const startBtnArea = document.querySelector('#start-btn-area');
    const searchArea = document.querySelector('#search-area');

    startBtn.addEventListener('click', () => {
        searchArea.classList.add('show');
        startBtnArea.classList.add('d-none');
    });
});