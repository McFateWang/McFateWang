import React, { Component } from 'react'

class Clock extends Component {
    constructor () {
        super()
        this.state = {
            date: new Date()
        }
    }

    componentWillMount () {
        this.timer = setInterval(() => {
            this.setState({ 
                date: new Date()
            })
        }, 1000);
    }

    componentDidMount () {
        console.log('233')
        this.input.focus()
    }

    componentWillUnmount () {
        clearInterval(this.timer)
    }

    render () {
        return (
            <div>
                <h1>
                    <p>现在的时间是</p>
                    {this.state.date.toLocaleTimeString()}
                    <hr />
                </h1>
                <input ref={
                        (input) => this.input = input
                    } />
            </div>
        )
    }
}

export default Clock