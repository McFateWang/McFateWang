// import React from 'react';
// import ReactDOM from 'react-dom';
// import './index.css';
// import App from './App';
// import * as serviceWorker from './serviceWorker';

// ReactDOM.render(<App />, document.getElementById('root'));

// // If you want your app to work offline and load faster, you can change
// // unregister() to register() below. Note this comes with some pitfalls.
// // Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();

import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import './index.css'

class Header extends Component {
  render () {
    var name = 'wangjie'
    var func = '=>'
    var className = 'myClass'
    var flag = true
    var yes = <h1>yes</h1>
    var no = <h1>no</h1> 
    return (
      <div>
        <h1>学习 React by {name}</h1>
        <h2>{((n) => {return n})(func)}</h2>
        <h3 className={className}>233</h3>
        {flag?<strong>it is true</strong>:<span>it is false</span>}
        {(  () => {
            if(name === 'wangjie') return yes
            else return no
            }
        )()}
      </div>
    )
  }
}

ReactDOM.render(
  <Header />,
  document.getElementById('root')
)