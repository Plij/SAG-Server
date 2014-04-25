from rest_framework import serializers
from server.models import Venue, UserProfile, Gang, Message
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):

	#TODO: Properly use depth for compiling these fields
	username  = serializers.Field(source = 'user.username')
	color = serializers.Field(source = 'gang.color')
	venues = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	full_name = serializers.Field()
	ranking = serializers.Field()

	class Meta:
		model = UserProfile
		fields = ('id', 'user', 'username','latitude', 'longitude', 'tags_created', 'tags_deleted', 'last_action','points', 'gang', 'color', 'busted', 'busts', 'full_name', 'ranking', 'venues', 'mood', 'spraying', 'bustedviapolice')


class MessageSerializer(serializers.ModelSerializer):
	#gangster = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Message
		fields = ('id', 'gangster', 'timestamp', 'text')



class GangSerializer(serializers.ModelSerializer):
	gangsters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

	class Meta:
		model = Gang
		fields = ('id', 'name', 'color', 'gangsters')


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email')


	def restore_object(self, attrs, instance=None):
		user = super(UserSerializer, self).restore_object(attrs, instance)
		user.set_password(attrs['password'])
		return user

	def to_native(self, obj):
		ret = super(UserSerializer, self).to_native(obj)
		del ret['password']
		return ret


class VenueSerializer(serializers.ModelSerializer):

	#TODO: Properly use depth for compiling these fields
	gang = serializers.Field(source='gangster.gang')

	class Meta:
		model = Venue
		fields = ('id', 'name', 'gangster', 'gangsterSpraying', 'gang', 'latitude', 'longitude', 'latestEditTimestamp', 'category', 'sprayinginitialized')
