import 'package:http/http.dart' as http;

class ArticleApi{
  static Future getArticle(){
    return http.get("http://10.0.2.2:8000/api/articles/");
  }
  static Future getArticleByCategoryId(int id){
    return http.get("http://10.0.2.2:8000/api/categories/$id/");
  }
}