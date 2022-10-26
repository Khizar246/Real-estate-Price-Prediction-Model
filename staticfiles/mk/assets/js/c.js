
var ctx = document.getElementById('myChart');

var genericOptions = {
  fill: false,
  interaction: {
    intersect: false
  },
  radius: 0,
};
// var skipped = (ctx, value) => ctx.p0.skip || ctx.p1.skip ? value : undefined;
const down = (ctx, value) => {console.log(ctx)};
const dataObj = {
  type: 'line',
  data: {
    labels: [0,1,2,3,0,1,0,1],
    datasets: [{
      label: 'My First Dataset',
      data: [1,2,1,0,0,1,0,1],
      borderColor: 'rgb(75, 192, 192)',
      segment: { borderColor: ctx =>   down(ctx, 'rgb(192,75,75)') ||  'rgb(75, 192, 192)'},
      // tension:0.4
      // spanGaps: true
    }]
  },
  options: genericOptions
};


var myChart =  new Chart(ctx,dataObj);
