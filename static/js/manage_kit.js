function toggleEdit(id) {
    const row = document.getElementById('drug-' + id);
    const displayElems = row.querySelectorAll('.display');
    const editElems = row.querySelectorAll('.edit');
    const confirmBtn = row.querySelector('.confirm-btn');
    const toggleBtn = row.querySelector('.edit-toggle-btn');

    const editing = toggleBtn.textContent === 'Cancel';

    displayElems.forEach(el => el.hidden = !editing);
    editElems.forEach(el => el.hidden = editing);
    confirmBtn.hidden = editing;
    toggleBtn.textContent = editing ? 'Edit' : 'Cancel';
}

const popup = document.getElementById('description-popup');

function showDescriptionPopup(event, text) {
    popup.innerText = text || '(No description)';
    popup.style.left = (event.pageX + 10) + 'px';
    popup.style.top = (event.pageY + 10) + 'px';
    popup.style.display = 'block';
    event.stopPropagation();
}

window.addEventListener('click', () => {
    popup.style.display = 'none';
});

popup.addEventListener('click', (e) => {
    e.stopPropagation();
});
