import React, { Component } from 'react'


class Text extends Component {
    constructor () {
        super()
        console.log('文本-构建')
    }

    componentWillMount () {
        console.log('文本-准备挂载')
    }

    componentDidMount () {
        console.log('文本-挂载成功')
    }

    componentWillUnmount () {
        console.log('文本-取消挂载')
    }

    render () {
        console.log('文本render')
        return (
            <div>
                <p>胖胖出现了！</p>
            </div>
        )
    }
}


class Mount extends Component {
    constructor () {
        super()
        console.log('构建')
        this.state = {
            isShow: true
        }
    }

    componentWillMount () {
        console.log('准备挂载')
    }

    componentDidMount () {
        console.log('挂载成功')
    }

    componentWillUnmount () {
        console.log('取消挂载')
    }

    handleShow () {
        this.setState(
            {isShow: !this.state.isShow}
        )
    }

    render () {
        console.log('render')
        return (
            <div>
                {this.state.isShow ? <Text /> : null}
                <button onClick={this.handleShow.bind(this)}>点击</button>
            </div>
        )
    }
}

export default Mount 