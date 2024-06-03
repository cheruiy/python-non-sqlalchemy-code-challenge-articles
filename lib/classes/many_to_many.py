class Article:
    all = []  # Class-level list to keep track of all articles

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

        self.__author = author
        self.__magazine = magazine
        self.__title = title

        author._Author__articles.append(self)
        magazine.add_article(self)
        Article.all.append(self)  # Add this article to the class-level list

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self.__magazine = value

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self.__author = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set(article.magazine for article in self.__articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        if article not in self.__articles:
            self.__articles.append(article)
        return article

    def topic_areas(self):
        if not self.__articles:
            return None
        return list(set(article.magazine.category for article in self.__articles))

class Magazine:
    instances = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")

        self.__name = name
        self.__category = category
        self.__articles = []  # Initialize the __articles attribute
        Magazine.instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self.__name = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self.__category = value

    def add_article(self, article):
        if not isinstance(article, Article):
            raise Exception("Must be an instance of Article")
        self.__articles.append(article)

    def articles(self):
        return self.__articles

    def contributors(self):
        return list(set(article.author for article in self.__articles))

    def article_titles(self):
        if not self.__articles:
            return None
        return [article.title for article in self.__articles]

    def contributing_authors(self):
        author_count = {}
        for article in self.__articles: 
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1

        contributing_authors = [author for author, count in author_count.items() if count > 2]

        # Return None if no authors have written more than 2 articles
        return contributing_authors if contributing_authors else None