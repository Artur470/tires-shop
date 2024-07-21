from rest_framework import serializers
from .models import *
from .utils import *





class TiresSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    def get_profile(self, obj):
        return obj.profile.title

    class Meta:
        model = Tires
        # fields = '__all__'

        fields = [
            'id',
            'image',
            'title',
            'profile',
            'price',
            'promotion',
            'in_stock',
            'state',
            'reviews',

        ]


class TiresCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tires
        fields = '__all__'


class TiresidSerializer(serializers.ModelSerializer):
    # title = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    profile = serializers.SerializerMethodField()
    diameter = serializers.SerializerMethodField()
    # price = serializers.SerializerMethodField()
    # promotion = serializers.SerializerMethodField()
    # quantity = serializers.SerializerMethodField()
    car_type = serializers.SerializerMethodField()
    seasonality = serializers.SerializerMethodField()
    # state = serializers.SerializerMethodField()
    manufacturer = serializers.SerializerMethodField()
    # discount = serializers.SerializerMethodField()
    # runflat = serializers.SerializerMethodField()
    # offroad = serializers.SerializerMethodField()
    speed_index = serializers.SerializerMethodField()
    load_index = serializers.SerializerMethodField()
    fuel_economy = serializers.SerializerMethodField()
    grip_on_wet_surfaces = serializers.SerializerMethodField()
    external_noise_level = serializers.SerializerMethodField()
    # set = serializers.SerializerMethodField()
    # in_stock = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    load_index_for_dual = serializers.SerializerMethodField()



    class Meta:
        model = Tires
        # fields = '__all__'

        fields = [
            'id',
            'title',
            'category',
            'image',
            'width',
            'profile',
            'diameter',
            'price',
            'promotion',
            'quantity',
            'car_type',
            'seasonality',
            'state',
            'manufacturer',
            'discount',
            'runflat',
            'offroad',
            'speed_index',
            'load_index',
            'fuel_economy',
            'grip_on_wet_surfaces',
            'external_noise_level',
            'set',
            'in_stock',
            'model',
            'load_index_for_dual'

        ]

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        color_data = validated_data.pop('color')
        brand_data = validated_data.pop('brand')

        category_instance, _ = Category.objects.get_or_create(**category_data)
        color_instance, _ = Color.objects.get_or_create(**color_data)
        brand_instance, _ = Brand.objects.get_or_create(**brand_data)

        product = Tires.objects.create(
            category=category_instance,
            color=color_instance,
            brand=brand_instance,
            **validated_data

        )

        return product













#
#
#     # def get_set(self, obj):
#     #     return obj.set
#     #
#     # def get_in_stock(self, obj):
#     #     return obj.in_stock
#
#     def get_model(self, obj):
#         return obj.model.title
#
#     def get_load_index_for_dual(self, obj):
#         return obj.load_index_for_dual.title

    # def get_title(self, obj):
    #     return obj.title





    def get_category(self, obj):
        return obj.category.title

    def get_width(self, obj):
        return obj.width.title

    def get_profile(self, obj):
        return obj.profile.title

    def get_diameter(self, obj):
        return obj.diameter.title

    # def get_price(self, obj):
    #     return obj.price

    # def get_promotion(self, obj):
    #     return obj.promotion

    # def get_quantity(self, obj):
    #     return obj.quantity

    def get_car_type(self, obj):
        return obj.car_type.title

    def get_seasonality(self, obj):
        return obj.seasonality.title

    # def get_state(self, obj):
    #     return obj.state

    def get_manufacturer(self, obj):
        return obj.manufacturer.title

    # def get_discount(self, obj):
    #     return obj.discount
    #
    # def get_runflat(self, obj):
    #     return obj.runflat
    #
    # def get_offroad(self, obj):
    #     return obj.offroad

    def get_speed_index(self, obj):
        return obj.speed_index.title

    def get_load_index(self, obj):
        return obj.load_index.title

    def get_fuel_economy(self, obj):
        return obj.fuel_economy.title

    def get_grip_on_wet_surfaces(self, obj):
        return obj.grip_on_wet_surfaces.title

    def get_external_noise_level(self, obj):
        return obj.external_noise_level.title

    # def get_set(self, obj):
    #     return obj.set
    #
    # def get_in_stock(self, obj):
    #     return obj.in_stock

    def get_model(self, obj):
        return obj.model.title

    def get_load_index_for_dual(self, obj):
        return obj.load_index_for_dual.title


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# class Reviewsserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reviews
#         fields = '__all__'
#
#     def create(self, validated_data):
#         tir_id = self.context["tir_id"]
#         user_id = self.context["user_id"]
#         rating = Reviews.objects.create(tir_id=tir_id, user_id=user_id, **self.validated_data)
#         return rating


class ReviewsSerializer(serializers.ModelSerializer):
    tires = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_tires(self, obj):
        return obj.tires.title

    def get_user(self, obj):
        return obj.user.first_name

    class Meta:
        model = Reviews
        fields = '__all__'



class Reviewsaddserializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['id',
                  'user',
                  'tires',
                  'comment',
                  'rating',
                  ]


class FavoriteSerializer(serializers.ModelSerializer):
    tir_id = serializers.IntegerField(source='tires_id')
    class Meta:
        model = Favorite
        fields = [
            'tir_id',
            'user'
        ]

