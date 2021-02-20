import React, { Component } from "react";
import axios from "axios";
import { API_URL } from "./constants";

export default class App extends Component {
  state ={
    articles:[],
  }

  componentDidMount() {
    this.getArticles()
  }
  
  getArticles = () => {
    axios.get(API_URL+"articles/")
    .then(res => (
      this.setState({articles: res.data.results})  
    ))
    .catch(err =>(
      alert(err)
    ));
  }


  render() {
    const articles = this.state.articles
    return (
      <div>
        {
        !articles || articles.length <= 0 ?
        (<div><p align="center"><b>Henüz yazı yok</b></p><br/></div>):
        (
          articles.map(article =>(
          <div id={article.id}>
            <h1>{article.name}-{article.author}</h1>
            <p>{article.description}</p>
          </div>
          ))
        )
        }
      </div>
    );
  }
  
}


