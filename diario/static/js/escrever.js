const input = document.getElementById('data');
const link = document.getElementById('link');
console.log(input)

input.addEventListener('input', () => {
    console.log("teste")
    const data = input.value;
    if (data) {
        link.href = `/diario/dia?data=${data}`;
    } else {
        link.href = "#";
    }

});
    link.addEventListener('click', (e) => {
        if (!input.value) {
            e.preventDefault();
            alert('Por favor, selecione uma data antes de continuar.');
        }
    });