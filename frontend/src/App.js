import React from 'react';
import axios from 'axios'
import { Line } from 'react-chartjs-2';

import './App.css';

class App extends React.Component {
  state = {
    pollList: []
  }

  componentDidMount() {
    return this.getDataFromApi()
  }

  async getDataFromApi() {
    const response = await axios.get('http://localhost:5000/api/v1/resources/congress-outlook')
    this.setState((state, props) => {
      return {
        pollList: response.data.poll_list
      }
    })
  }

  render() {
    const data = {
      labels: this.state.pollList.map((e) => e.createddate),
      datasets: [
        {
          label: 'Adjusted Dem',
          data: this.state.pollList.map((e) => e.adjusted_dem),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(15, 129, 242, 10)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        },
        {
          label: 'Adjusted Rep',
          data: this.state.pollList.map((e) => e.adjusted_rep),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(252, 3, 3, 10)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        },
        // {
        //   label: 'Dem',
        //   data: this.state.pollList.map((e) => e.dem),
        //   backgroundColor: 'rgba(116, 182, 247, 1)',
        //   borderColor: 'rgba(116, 182, 247, 1)',
        //   type: 'scatter'
        // },
        // {
        //   label: 'Rep',
        //   data: this.state.pollList.map((e) => e.rep),
        //   backgroundColor: 'rgba(252, 109, 109, 1)',
        //   borderColor: 'rgba(252, 109, 109, 1)',
        //   type: 'scatter'
        // },
      ]
    }

    const options = {
      scales: {
          yAxes: [{
              ticks: {
                  min: 30,
                  max: 70
              }
          }]
      }
    }

    return (
      <div className="app">
        <header className="header">
          <h1>Capitol Tracker</h1>
          <h6 className="sub-heading">Data driven political decisions</h6>
        </header>

        <Line 
          className="line-graph"
          data={data}
          options={options} />
      </div>
    );
  }
}

export default App;
