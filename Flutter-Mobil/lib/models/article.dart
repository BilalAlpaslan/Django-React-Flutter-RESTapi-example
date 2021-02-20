class Article{
  int id;
  String slug;
  int author;
  String name;
  String description;
  String image;
  // ignore: non_constant_identifier_names
  String created_date;

  Article(
      this.id,
      this.slug,
      this.author,
      this.name,
      this.description,
      this.image,
      this.created_date
      );


  Article.fromJson(Map json){
    id = json["id"];
    slug = json["slug"];
    author = json["author"];
    name = json["name"];
    description = json["description"];
    image = json["image"];
    created_date = json["created_date"];
  }

  Map toJson(){
    return {
      "id":id,
      "slug":slug,
      "author":author,
      "name":name,
      "description":description,
      "image":image,
      "created_date":created_date,
    };
  }
}
