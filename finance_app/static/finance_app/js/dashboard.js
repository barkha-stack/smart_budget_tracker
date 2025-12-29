const ctx = document.getElementById('expenseChart');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: categories,
        datasets: [{
            label: 'Expenses',
            data: totals,
        }]
    },
});
