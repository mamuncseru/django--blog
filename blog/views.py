from django.shortcuts import render
from  datetime import date
# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "Mamun.jpg",
        "author": "Mamun",
        "date" : date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views yo get when hiking in the mountains! And I wasn't even prepared for waht happened whilst I was enjoying the view!",
        "content": """
        Veniam nobis temporibus maiores iste facere, dolor quod alias, suscipit modi delectus ducimus consequuntur officia, repellendus quisquam recusandae excepturi, unde numquam voluptas?

Eum fuga cum, velit voluptatibus soluta doloremque eius aliquam, enim voluptatem est magnam consequuntur, aspernatur voluptatibus laborum amet, quas explicabo nam porro totam laboriosam eveniet inventore repudiandae? Blanditiis repellat facilis facere, molestiae unde facilis fugiat possimus recusandae ut accusantium perspiciatis architecto, ratione fugiat aliquid aliquam beatae veniam ut illo rem commodi similique voluptatum, architecto doloribus doloremque nesciunt id cum numquam.

Nam suscipit possimus soluta ea natus ratione laudantium eaque praesentium error. Maxime velit voluptates libero debitis repudiandae quisquam?

Dolores ea magnam necessitatibus perspiciatis repudiandae, eius ipsum neque. Quibusdam soluta repudiandae omnis expedita quae corrupti mollitia commodi magni provident, delectus totam assumenda eius natus in mollitia suscipit vero, facilis praesentium fuga eaque asperiores commodi vel totam. Quod explicabo minima provident illum sint at cum inventore quaerat dignissimos soluta.
        """
    },
    {
        "slug": "blind-man-see-colors",
        "image": "Mamun.jpg",
        "author": "Mamun",
        "date" : date(2021, 7, 24),
        "title": "Blind Man see colors",
        "excerpt": "There's nothing like the views yo get when hiking in the mountains! And I wasn't even prepared for waht happened whilst I was enjoying the view!",
        "content": """
        Veniam nobis temporibus maiores iste facere, dolor quod alias, suscipit modi delectus ducimus consequuntur officia, repellendus quisquam recusandae excepturi, unde numquam voluptas?

Eum fuga cum, velit voluptatibus soluta doloremque eius aliquam, enim voluptatem est magnam consequuntur, aspernatur voluptatibus laborum amet, quas explicabo nam porro totam laboriosam eveniet inventore repudiandae? Blanditiis repellat facilis facere, molestiae unde facilis fugiat possimus recusandae ut accusantium perspiciatis architecto, ratione fugiat aliquid aliquam beatae veniam ut illo rem commodi similique voluptatum, architecto doloribus doloremque nesciunt id cum numquam.

Nam suscipit possimus soluta ea natus ratione laudantium eaque praesentium error. Maxime velit voluptates libero debitis repudiandae quisquam?

Dolores ea magnam necessitatibus perspiciatis repudiandae, eius ipsum neque. Quibusdam soluta repudiandae omnis expedita quae corrupti mollitia commodi magni provident, delectus totam assumenda eius natus in mollitia suscipit vero, facilis praesentium fuga eaque asperiores commodi vel totam. Quod explicabo minima provident illum sint at cum inventore quaerat dignissimos soluta.
        """
    },
    {
        "slug": "monitor-not-working",
        "image": "Mamun.jpg",
        "author": "Mamun",
        "date" : date(2021, 4, 24),
        "title": "Monitor not working",
        "excerpt": "There's nothing like the views yo get when hiking in the mountains! And I wasn't even prepared for waht happened whilst I was enjoying the view!",
        "content": """
        Veniam nobis temporibus maiores iste facere, dolor quod alias, suscipit modi delectus ducimus consequuntur officia, repellendus quisquam recusandae excepturi, unde numquam voluptas?

Eum fuga cum, velit voluptatibus soluta doloremque eius aliquam, enim voluptatem est magnam consequuntur, aspernatur voluptatibus laborum amet, quas explicabo nam porro totam laboriosam eveniet inventore repudiandae? Blanditiis repellat facilis facere, molestiae unde facilis fugiat possimus recusandae ut accusantium perspiciatis architecto, ratione fugiat aliquid aliquam beatae veniam ut illo rem commodi similique voluptatum, architecto doloribus doloremque nesciunt id cum numquam.

Nam suscipit possimus soluta ea natus ratione laudantium eaque praesentium error. Maxime velit voluptates libero debitis repudiandae quisquam?

Dolores ea magnam necessitatibus perspiciatis repudiandae, eius ipsum neque. Quibusdam soluta repudiandae omnis expedita quae corrupti mollitia commodi magni provident, delectus totam assumenda eius natus in mollitia suscipit vero, facilis praesentium fuga eaque asperiores commodi vel totam. Quod explicabo minima provident illum sint at cum inventore quaerat dignissimos soluta.
        """
    },
    {
        "slug": "better-to-stay-way",
        "image": "Mamun.jpg",
        "author": "Mamun",
        "date" : date(2021, 3, 24),
        "title": "Better to stay way",
        "excerpt": "There's nothing like the views yo get when hiking in the mountains! And I wasn't even prepared for waht happened whilst I was enjoying the view!",
        "content": """
        Veniam nobis temporibus maiores iste facere, dolor quod alias, suscipit modi delectus ducimus consequuntur officia, repellendus quisquam recusandae excepturi, unde numquam voluptas?

Eum fuga cum, velit voluptatibus soluta doloremque eius aliquam, enim voluptatem est magnam consequuntur, aspernatur voluptatibus laborum amet, quas explicabo nam porro totam laboriosam eveniet inventore repudiandae? Blanditiis repellat facilis facere, molestiae unde facilis fugiat possimus recusandae ut accusantium perspiciatis architecto, ratione fugiat aliquid aliquam beatae veniam ut illo rem commodi similique voluptatum, architecto doloribus doloremque nesciunt id cum numquam.

Nam suscipit possimus soluta ea natus ratione laudantium eaque praesentium error. Maxime velit voluptates libero debitis repudiandae quisquam?

Dolores ea magnam necessitatibus perspiciatis repudiandae, eius ipsum neque. Quibusdam soluta repudiandae omnis expedita quae corrupti mollitia commodi magni provident, delectus totam assumenda eius natus in mollitia suscipit vero, facilis praesentium fuga eaque asperiores commodi vel totam. Quod explicabo minima provident illum sint at cum inventore quaerat dignissimos soluta.
        """
    },
    {
        "slug": "world-is-beautiful",
        "image": "Mamun.jpg",
        "author": "Mamun",
        "date" : date(2021, 11, 24),
        "title": "World is beautiful",
        "excerpt": "There's nothing like the views yo get when hiking in the mountains! And I wasn't even prepared for waht happened whilst I was enjoying the view!",
        "content": """
        Veniam nobis temporibus maiores iste facere, dolor quod alias, suscipit modi delectus ducimus consequuntur officia, repellendus quisquam recusandae excepturi, unde numquam voluptas?

Eum fuga cum, velit voluptatibus soluta doloremque eius aliquam, enim voluptatem est magnam consequuntur, aspernatur voluptatibus laborum amet, quas explicabo nam porro totam laboriosam eveniet inventore repudiandae? Blanditiis repellat facilis facere, molestiae unde facilis fugiat possimus recusandae ut accusantium perspiciatis architecto, ratione fugiat aliquid aliquam beatae veniam ut illo rem commodi similique voluptatum, architecto doloribus doloremque nesciunt id cum numquam.

Nam suscipit possimus soluta ea natus ratione laudantium eaque praesentium error. Maxime velit voluptates libero debitis repudiandae quisquam?

Dolores ea magnam necessitatibus perspiciatis repudiandae, eius ipsum neque. Quibusdam soluta repudiandae omnis expedita quae corrupti mollitia commodi magni provident, delectus totam assumenda eius natus in mollitia suscipit vero, facilis praesentium fuga eaque asperiores commodi vel totam. Quod explicabo minima provident illum sint at cum inventore quaerat dignissimos soluta.
        """
    }
]

def get_date(post):
    return post.get('date')


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })