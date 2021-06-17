// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Aprovado", "Cursando", "A cursar", "Reprovado"],
    datasets: [{
      data: [35.02, 17.01, 24.48, 24.48],
 backgroundColor: ['#28a745', '#007bff', '#ffc107', '#dc3545'],
    }],
  },
});
