import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_html/flutter_html.dart';
import 'package:flutter_mobil/api/article_api.dart';
import 'package:flutter_mobil/models/article.dart';


class MainScreen extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
    return MainScreenState();
  }

}

class MainScreenState extends State{
  List<Article> articles = List<Article>();

  @override
  void initState() {
    getArticles();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("deneme", style: TextStyle(color: Colors.orange),),
        backgroundColor: Colors.cyan,
        centerTitle: true,
      ),
      body: Padding(
        padding: EdgeInsets.all(20.0),
        child: Column(
          children: List.generate(this.articles.length,(index){
            return Padding(
              padding: const EdgeInsets.all(18.0),
              child: Column(
                children: [
                  Text(this.articles[index].name),
                  Html(data: this.articles[index].description,)
                ],
              ),
            );
          }),
        ),
      ),
    );
  }


  void getArticles() {
    ArticleApi.getArticle().then((response){
      setState(() {
        Iterable list = json.decode(utf8.decode(response.bodyBytes))["results"];
        this.articles = list.map((product) => Article.fromJson(product)).toList();
      });
    });
  }

}