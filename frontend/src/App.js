import React from 'react';
import axios from 'axios'
import { Line } from 'react-chartjs-2';
import { uniq, map, sortBy, groupBy } from 'lodash'
import { RGBA } from './rgbaColor'

import './App.css';

const API_PROTOCOL = process.env.REACT_APP_API_PROTOCOL || 'http'
const API_HOST = process.env.REACT_APP_API_HOST || 'localhost'
const API_PORT = process.env.REACT_APP_API_PORT || 5000

class App extends React.Component {
  state = {
    time: [],
    polls: new Map()
  }

  componentDidMount() {
    return this.getDataFromApi()
  }

  async getDataFromApi() {
    const response = await axios.get(`${API_PROTOCOL}://${API_HOST}:${API_PORT}/v1/poll-data?measurements=cat,dog`)
    this.setState((state) => {
      const pollsByStance = groupBy(response.data, (pollNode) => pollNode.stance)
      return {
        time: uniq(map(sortBy(state.pollList, ['time'],['asc']), (e) => e.time)),
        polls: new Map(Object.entries(pollsByStance))
      }
    })
  }

  render() {
    const datasets = map([...this.state.polls], function([stance, value]) {
      const color = new RGBA(false, false, false, 0.5)
      return {
        label: stance,
        data: map(value, (e) => ({ y: e.percentage, t: new Date(e.time) })),
        backgroundColor: 'rgba(0, 0, 0, 0)',
        borderColor: color.getString(),
        borderWidth: 2,
        lineTension: 1,
        type: 'line'
      }
    })

    const data = {
      labels: this.state.time,
      datasets,
    }

    const options = {
      scales: {
          yAxes: [{
              ticks: {
                  min: 20,
                  max: 80
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
