from django.db import models


class Tag(models.Model):
    """Tags"""
    title = models.CharField("Tag", max_length=100, db_index=True)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Category(models.Model):
    """Categories"""
    title = models.CharField("Category", max_length=150, db_index=True)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Post(models.Model):
    """News"""
    title = models.CharField("Title", max_length=150, db_index=True)
    tag = models.ManyToManyField(Tag, verbose_name='Tag', related_name="posts")
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="news_posters/")
    public_time = models.DateTimeField(auto_now_add=True, verbose_name="Public Time", db_index=True)
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name="Modified Time")
    url = models.SlugField(max_length=150, unique=True)
    draft = models.BooleanField("Draft", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Comment(models.Model):
    """Comments to posts"""
    name = models.CharField("Name", max_length=100)
    email = models.EmailField()
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Parent", on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.name - self.post

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
