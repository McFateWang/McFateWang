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
    renderGoodWord(goodWord, badWord) {
        const goodFlag = true
        return goodFlag ? goodWord : badWord
    }
    render() {
        var name = 'wangjie'
        var func = '=>'
        var className = 'myClass'
        var flag = true
        var yes = <h1>yes</h1>
        var no = <h1>no</h1>
        return (
            <div>
                <h1>学习 React by {name}</h1>
                <h2>{((n) => { return n })(func)}</h2>
                <h3 className={className}>233</h3>
                {flag ? <strong>it is true</strong> : <span>it is false</span>}
                {(() => {
                    if (name === 'wangjie') return yes
                    else return no
                }
                )()}
                {this.renderGoodWord(yes, no)}
            </div>
        )
    }
}

class Main extends Component {
    constructor() {
        super()
        this.state = { flag: 'yes' }
    }

    handleClickOnMain(list, e) {
        for (var i = 0; i < list.length; i++) {
            console.log(list[i])
        }
        console.log('HTML: ', e.target.innerHTML)
        this.setState({
            flag: 'no'
        })
        console.log(this.state.flag)
    }

    render() {
        const word = 'it is main'
        const list = ['a', 'b', 'c']
        return (
            <div>
                <h1 onClick={this.handleClickOnMain.bind(this, list)}>{word}</h1>
                {console.log(this)}
            </div>
        )
    }
}

class LikeButton extends Component {
    constructor() {
        super()
        this.state = { isLiked: false }
    }

    handleClickOnLikeButton() {
        this.setState({
            isLiked: !this.state.isLiked
        })
        if (this.props.onClick) {
            this.props.onClick()
        }
    }

    render() {
        console.log(this.props.onClick)
        const likedText = this.props.likedText || '取消'
        const unlikedText = this.props.unlikedText || '点赞'
        return (
            <button onClick={this.handleClickOnLikeButton.bind(this)}>
                {this.state.isLiked ? likedText : unlikedText} 👍
        </button>
        )
    }
}

class Index extends Component {
    static defaultProps = {
        myFlag: '1'
    }

    myClick () {
        console.log('有名字的函数')
    }

    render() {
        return (
            <div>
                <Header></Header>
                <Main></Main>
                <LikeButton likedText='已赞' unlikedText='取消' />
                <p>{this.props.myFlag}</p>
                <LikeButton 
                    likedText='胖胖' unlikedText='晗晗' 
                    onClick={
                        // () => console.log('传入的函数!!!')
                        this.myClick
                    }
                    />
            </div>
        )
    }
}

const users = [
    { username: '月半', age:22, gender: 'male'},
    { username: '晗晗', age:22, gender: 'female'}
]

class User extends Component {
    render () {
        // 这里props是一个对象，so
        // 方案1
        // console.log(this.props.user)
        // const  user  = this.props.user 
        // 方案2
        console.log(this.props)
        const  {user}  = this.props     
        console.log(user)
        return (
            <div>
                <div>姓名：{user.username}</div>
                <div>年龄：{user.age}</div>
                <div>性别：{user.gender}</div>
                <hr />
                <hr />
            </div>
        )
    }
}

class Map extends Component {
    render () {
        // const usersElements = []
        // for( let user of users) {
        //     usersElements.push(
        //         <div>
        //             <div>姓名：{user.username}</div>
        //             <div>年龄：{user.age}</div>
        //             <div>性别：{user.gender}</div>
        //             <hr />
        //         </div>
        //     )
        // }
        
        return (
            <div>
                {users.map(
                    (user, i) => <User key={i} user={user} ></User>
                )}
            </div>
        )

        // return (
        //     // <div>{usersElements}</div>
        //     <div>
        //         {users.map(
        //             (user) => {
        //                 return (
        //                     <div>
        //                         <div>姓名：{user.username}</div>
        //                         <div>年龄：{user.age}</div>
        //                         <div>性别：{user.gender}</div>
        //                         <hr />
        //                     </div>
        //                 )
        //             }
        //         )}
        //     </div>
        // )
    }
}

ReactDOM.render(
    <Map />,
    document.getElementById('root')
)