import React, { Component } from 'react'

class CommentInput extends Component {
    // 1
    constructor() {
        super()
        this.state = {
            username: '',
            content: ''
        }
    }

    // 2
    componentWillMount () {
        this._loadUername()
    }

    componentDidMount () {
        this.textarea.focus()
    }

    // 5
    _loadUername () {
        const username = localStorage.getItem('username')
        if (username) {
            this.setState({ username: username })
        }
    }

    _saveUsername (username) {
        localStorage.setItem('username', username)
    }

    // 6
    handleUsernameChange(event) {
        this.setState({
            username: event.target.value
        })
    }

    handleContentChange(event) {
        this.setState({
            content: event.target.value
        })
    }

    handleSubmit () {
        if (this.props.onSubmit) {
            // 检查，如果有这个函数
            // 先从子组件的state中提取变量
            // 传入到props的函数中
            const { username, content } = this.state
            this.props.onSubmit({ username, content })
        }
        this.setState({ content: '' })
    }

    handleUsernameBlur (event) {
        this._saveUsername(event.target.value)
    }

    // 8
    render() {
        return (
            <div className='comment-input'>
                <div className='comment-field'>
                    <span className='comment-field-name'>用户名：</span>
                    <div className='comment-field-input'>
                        <input
                            value={this.state.username}
                            onBlur={this.handleUsernameBlur.bind(this)}
                            onChange={this.handleUsernameChange.bind(this)}
                        />
                    </div>
                </div>
                <div className='comment-field'>
                    <span className='comment-field-name'>评论内容：</span>
                    <div className='comment-field-input'>
                        <textarea 
                            ref={(textarea) => this.textarea = textarea}
                            value={this.state.content}
                            onChange={this.handleContentChange.bind(this)}
                        />
                    </div>
                </div>
                <div className='comment-field-button'>
                    <button
                        onClick={this.handleSubmit.bind(this)}>
                        发布
                    </button>
                </div>
            </div>
        )
    }
}

export default CommentInput