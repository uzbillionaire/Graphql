import graphene
from graphene_django import DjangoObjectType

from apps.models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = '__all__'


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = '__all__'


class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)
    all_products = graphene.List(ProductType)

    def resolve_all_categories(self, info):
        return Category.objects.all()


class CreateCategory(graphene.Mutation):
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        title = graphene.String(required=True)

    def mutate(self, info, title):
        Category.objects.create(title=title)
        return CreateCategory(message = "Yaratildi", status=201)


class CreateProduct(graphene.Mutation):
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        title = graphene.String(required=True)
        price = graphene.Int(required=True)
        stock = graphene.Int(required=True)
        category = graphene.Int(required=True)

    def mutate(self, info, title, price, stock, category):
        Category.objects.create(title=title, price=price, stock=stock, category=category)
        return CreateCategory(message="Yaratildi", status=201)




class UpdateCategory(graphene.Mutation):
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()

    def mutate(self, info, id, title=None):
        category = Category.objects.get(pk=id)
        if title:
            category.title = title

        category.save()
        return UpdateCategory(message="Category o'zgartirildi", status=200)


class UpdateProduct(graphene.Mutation):
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        price = graphene.Int()
        stock = graphene.Int()
        category = graphene.Int()


    def mutate(self, info, id, title=None, price=None, category=None, stock=None):
        product = Product.objects.get(pk=id)
        if title:
            product.title = title
        if price:
            product.price = price
        if category:
            product.category = category
        if stock:
            product.stock = stock

        product.save()
        return UpdateProduct(message="Product o'zgartirildi", status=200)

class DeleteCategory(graphene.Mutation):
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        query = Category.objects.filter(pk=id)
        if query.exists():
            query.delete()
        return UpdateCategory(message="Post o'chirildi", status=200)


class DeleteProduct(graphene.Mutation):
    message = graphene.String()
    status = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        query = Product.objects.filter(pk=id)
        if query.exists():
            query.delete()
        return UpdateProduct(message="Post o'chirildi", status=200)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()


schema = graphene.Schema(query=Query , mutation=Mutation)





