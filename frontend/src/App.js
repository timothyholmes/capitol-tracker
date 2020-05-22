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
      datasets: [{
        label: 'Adjusted Dem',
        data: this.state.pollList.map((e) => e.adjusted_dem),
        backgroundColor: 'rgba(0, 0, 0, 0)',
        borderColor: '#0377fc',
        borderWidth: 1
      }, {
        label: 'Adjusted Rep',
        data: this.state.pollList.map((e) => e.adjusted_rep),
        backgroundColor: 'rgba(0, 0, 0, 0)',
        borderColor: '#fc0303',
        borderWidth: 1
      }]
    }

    return (
      <div className="app">
        <header className="header">
          <h1>Capitol Tracker</h1>
          <h6 className="sub-heading">Data driven political decisions</h6>
        </header>

        <Line 
          className="line-graph"
          data={data} />
      </div>
    );
  }
}

export default App;
