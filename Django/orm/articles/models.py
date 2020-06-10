from django.db import models

# Create your models here.
class Article(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): # f-string
        return f'{self.id}번 글 - {self.title} : {self.content}'

# 1. models.py 작성 및 변경(생성 및 수정)
# 2. python manage.py makemigrations -> migration(설계도) 파일 생성
# 3. python manage.py migrate -> 실제 Database에 적용 (테이블 생성)

# [Django shell]
# python manage.py shell

# 1. Model import
# from articles.models import Article

# 1. Create
# 1-1. instance
# article = Article()
# article.title = 'First'
# articel.content = 'Wow!'
# article.save()


# 1-2. 두번쨰
# article = Article(title='Second', content='Two!')
# article.save()

# 1-3. 세번쨰 -> CREATE
# article = Article.objects.create(title='Third', content='Three!')
# save할 필요없이 바로 저장하고 database에 할당 됨

# 2. Read
# 2-1. all() -> SELECT # 복수(0~여러개)
# articles = Article.objects.all()

# 2-2 filter() -> WHERE # 복수(0개~ 여러개) (list의 형태)
# articles = Article.objects.fitler(title='First')

# 2-3. .get() # 단수(1개) (instance) 무조건 1개만 리턴 필수
# article = Article.objects.get(id=1)
# article = Article.objects.get(pk=1) # id_exact
# article = Article.objects.get(title='First')  #Error
# article = Article.objects.get(pk=10) # Error
# article = Article.objects.filter(pk=10) # []


# 2-4. QuerySet (유사 리스트)
# articles = Article.objects.all()
# articles[0] # 첫번째 데이터
# articles.first() # 첫번째 데이터
# articles[-1] # 마지막 데이터
# articles.last() # 마지막 데이터
# articles[1:3] # 2번째 ~ 3번째 (OFFSET 1, LIMIT 2)
# 2, 3
# articles[OFFSET:OFFSET+LIMIT]


# 2-5. order_by()
# Article.objects.order_by('created_at') 생성된 시간대로 정렬 => 오름차순
# Article.objects.order_by('-created_at') 생성된 시간의 역으로 정렬 => 내림차순


# 3. Update
# (1) 데이터 가져오기 (<- DB)
# article = Article.objects.get(pk=1)
# (2) 인스턴스 수정
# article.content = 'Bye bye!'
# (3) 인스턴스 저장 (-> DB)
# article.save()


# 4. Delete
# (1) 데이터 가져오기 (<-DB)
# article = Article.objects.get(pk=1)
# (2) 인스턴스 삭제
# article.delete()
