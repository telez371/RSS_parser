document.addEventListener('DOMContentLoaded', function() {
  const rssNameInput = document.querySelector('input[name="name"]');
  const rssUrlInput = document.querySelector('input[name="url"]');
  const saveButton = document.querySelector('.save-button');

  function updateSaveButtonState() {
    if (rssNameInput.value && rssUrlInput.value) {
      saveButton.disabled = false;
      saveButton.classList.add('button-active');
    } else {
      saveButton.disabled = true;
      saveButton.classList.remove('button-active');
    }
  }

  rssNameInput.addEventListener('input', updateSaveButtonState);
  rssUrlInput.addEventListener('input', updateSaveButtonState);
});
