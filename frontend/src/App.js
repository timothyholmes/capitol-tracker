import React from 'react';
import axios from 'axios'
import { Line } from 'react-chartjs-2';
import { uniq, map, filter, sortBy } from 'lodash'

import './App.css';

class App extends React.Component {
  state = {
    pollList: []
  }

  componentDidMount() {
    return this.getDataFromApi()
  }

  async getDataFromApi() {
    const { data } = await axios.get('http://localhost:5000/v1/measurements')
    const measurements = data.map((e) => e.name).join(',')
    const response = await axios.get(`http://localhost:5000/v1/poll-data?measurements=${measurements}`)
    this.setState((state, props) => {
      return {
        pollList: response.data
      }
    })
  }

  render() {
    const data = {
      labels: uniq(map(sortBy(this.state.pollList, ['time'],['asc']), (e) => e.time)),
      datasets: [
        {
          label: 'Adjusted Dem',
          data: map(filter(this.state.pollList, (e) => e.party === 'democrat'), (e) => ({ y: e.percentage, t: new Date(e.time) })),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(15, 129, 242, 0.5)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        },
        {
          label: 'Adjusted Rep',
          data: map(filter(this.state.pollList, (e) => e.party === 'republican'), (e) => ({ y: e.percentage, t: new Date(e.time) })),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(252, 3, 3, 0.5)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        },
        {
          label: 'Trump Approve',
          data: map(filter(this.state.pollList, (e) => e.stance === 'approve'), (e) => ({ y: e.percentage, t: new Date(e.time) })),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(50, 168, 78, 0.5)',
          borderWidth: 2,
          lineTension: 1,
          type: 'line'
        },
        {
          label: 'Trump Disapprove',
          data: map(filter(this.state.pollList, (e) => e.stance === 'disapprove'), (e) => ({ y: e.percentage, t: new Date(e.time) })),
          backgroundColor: 'rgba(0, 0, 0, 0)',
          borderColor: 'rgba(230, 118, 28, 0.5)',
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
          }],
          xAxes: [
            {
              type: 'time'
            }
          ]
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
