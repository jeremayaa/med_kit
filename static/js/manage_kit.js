function toggleEdit(id) {
    const row = document.getElementById('drug-' + id);
    const displayElems = row.querySelectorAll('.display');
    const editElems    = row.querySelectorAll('.edit');
    const takeBtn      = row.querySelector('.take-btn');
    const editBtn      = row.querySelector('.edit-toggle-btn');
    const confirmBtn   = row.querySelector('.confirm-btn');
    const deleteBtn    = row.querySelector('.delete-btn');
  
    const editing = (editBtn.textContent === 'Cancel');
  
    displayElems.forEach(el => el.hidden = !editing);
    editElems.forEach(el => el.hidden = editing);
  
    takeBtn.hidden    = !editing;    // hide Take in edit mode
    confirmBtn.hidden = editing;     // show Confirm only in edit mode
    deleteBtn.hidden  = editing;     // show Delete only in edit mode
  
    editBtn.textContent = editing ? 'Edit' : 'Cancel';
  }
  
  // Popup for “Show Description”
  const popup = document.getElementById('description-popup');
  function showDescriptionPopup(event, text) {
    popup.innerText = text || '(No description)';
    popup.style.left = (event.pageX + 10) + 'px';
    popup.style.top  = (event.pageY + 10) + 'px';
    popup.style.display = 'block';
    event.stopPropagation();
  }
  window.addEventListener('click', () => {
    popup.style.display = 'none';
  });
  popup.addEventListener('click', e => e.stopPropagation());
  
  // Confirm + submit the hidden delete form
  function confirmDelete(id) {
    const ok = window.confirm("Are you sure you want to delete this drug?");
    if (!ok) return;
    const form = document.getElementById('delete-form-' + id);
    if (form) form.submit();
  }
  