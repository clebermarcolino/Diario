document.addEventListener('DOMContentLoaded', function () {

    console.log('JS carregado');

    const canvas = document.getElementById('myChart');
    if (!canvas) {
        console.error('Canvas myChart não encontrado');
        return;
    }

    const nomesScript = document.getElementById('nomes-data');
    const quantidadesScript = document.getElementById('quantidades-data');

    if (!nomesScript || !quantidadesScript) {
        console.error('Dados do gráfico não encontrados');
        return;
    }

    const nomes = JSON.parse(nomesScript.textContent);
    const quantidades = JSON.parse(quantidadesScript.textContent);

    console.log('Labels:', nomes);
    console.log('Valores:', quantidades);

    new Chart(canvas, {
        type: 'bar',
        data: {
            labels: nomes,
            datasets: [{
                label: 'Quantidade',
                data: quantidades,
                backgroundColor: 'rgba(99, 102, 241, 0.6)',
                borderColor: 'rgb(99, 102, 241)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

});
