import React from 'react';
import Food from './main.js';
import axios from "axios";
import './App.css';

/*
function App() {
  return (
    <div className="App">
      <h1>hello</h1>
      <Food fav = "kimchi"/>
    </div>
  );
}
*/


class App extends React.Component{
  state = {    //data that will change
      count: 0
  };
  add = () => {
      console.log("add");
      this.setState(current => ({count: current.count+1}));
  };    //javascript code
  minus = () => {
      console.log("minus");
      this.setState(current => ({count: current.count-1}));
  };    //javascript code
  render(){    //automatic
      return (
          <div>
              <h1>The number is:  {this.state.count}</h1>
              <button onClick={this.add}>Add</button>    
              <button onClick={this.minus}>Minus</button>    
          </div>
      );
  }
}


export default App;
