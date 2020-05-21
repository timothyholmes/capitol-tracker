<script>
  import Chart from 'svelte-frappe-charts';
  import { pollList } from '../store/state.js'
  import isNull from 'lodash/isNull'

  let data = null;
  
  pollList.subscribe(latestPolls => {
    let tmp = {
      labels: [],
      datasets: [
        {
          values: []
        },
        {
          values: []
        }
      ]
    }
    for (const poll of latestPolls) {
      tmp.labels.push(poll.createddate)
      tmp.datasets[0].values.push(poll.adjusted_dem)
      tmp.datasets[1].values.push(poll.adjusted_rep)
    }

    data = tmp
	});
</script>

{#if !isNull(data)}
  <Chart data={data} type="line" />
{/if}
