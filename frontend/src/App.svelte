<script>
  import Router from 'svelte-spa-router'
  import routes from './routes'
  import { pollList } from './store/state.js'
  import GetDataFromApi from './resource/getDataFromApi.js'

  import { onMount } from 'svelte'

  onMount(async () => {
    const data = await GetDataFromApi('http://localhost:5000/api/v1/resources/congress-outlook')
    pollList.set(data.poll_list)
  })
</script>

<section class="wrap">
  <h1 class="heading">Python + Svelte</h1>
  <Router {routes} />
</section>

<style>
  .wrap {
    margin: 0 20% 0 20%;
    min-height: calc(100vh - 150px);
  }

  .heading {
    color: #fc8b65;
    font-size: 60px;
  }
</style>
