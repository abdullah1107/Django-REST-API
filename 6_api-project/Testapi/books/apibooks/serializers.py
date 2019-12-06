from rest_framework import serializers
from books.models import Book

class BookUpdateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Book
		fields = ('pk','book_name','category', 'personid')

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('pk','book_name','category', 'personid')
		#depth = 1

class  BookCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('book_name','category', 'personid')
	def save(self):
		try:
			book_name          = self.validated_data['book_name']
			category           = self.validated_data['category']
			#book_file          = self.validated_data['book_file']
			personid           = self.validated_data['personid']
			bookinfo = Book(
								book_name=book_name,
								category=category,
								#book_file=book_file,
								personid= personid
								)
			bookinfo.save()
			return bookinfo
		except KeyError:
			raise serializers.ValidationError({"response": "this invalid somethings!!!!!"})