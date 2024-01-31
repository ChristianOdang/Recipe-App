// get input element from field

const select = document.getElementById('select-idd')
const alert = document.getElementById('alert')

select.addEventListener('change', (e) => {
  e.preventDefault();
  document.getElementById('alert').innerHTML = '';

  if (select.value == 1) {
    display_hint('Hint: American, Asian, British, Chinese, French,...');
  }
  else if (select.value == 2) {
    display_hint('Hint: Balanced, Low-Sodium, Low-Fat, Low-Carb');
  }
  else if (select.value == 3) {
    display_hint('Hint: Enter 1 - 3 to search ingredients between that range');
  }
  else if (select.value == 0) {
    alert.style.animation = 'fade-out 2s'
  }
})