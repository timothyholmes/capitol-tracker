import React from 'react';
import axios from 'axios'
import { Line } from 'react-chartjs-2';
import { uniq, map, filter } from 'lodash'

import './App.css';

class App extends React.Component {
  state = {
    pollList: []
  }

  componentDidMount() {
    return this.getDataFromApi()
  }

  async getDataFromApi() {
    const response = await axios.get('http://capitol-tracker-api.capitol-network:5000/v1/resources/congress-outlook')
    this.setState((state, props) => {
      return {
        pollList: response.data
      }
    })
  }

  render() {
    const data = {
      labels: uniq(map(this.state.pollList, (e) => e.time)),
      datasets: [
        {
          label: 'Adjusted Dem',
          data: map(filter(this.state.pollList, (e) => e.party === 'democrat'), (e) => e.percentage),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(15, 129, 242, 10)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        },
        {
          label: 'Adjusted Rep',
          data: map(filter(this.state.pollList, (e) => e.party === 'republican'), (e) => e.percentage),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(252, 3, 3, 10)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        }
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
