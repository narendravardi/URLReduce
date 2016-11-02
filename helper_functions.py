import re
import dynamodb_crud_operations
import hash_encode_and_decode
def is_valid_url(url):
	# url of the type http[s]://www.amazon.com
	# url of the type http[s]://amazon.com
	url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
	if not re.search(url_regex,url):
		return False
	else:
		return True

def update_new_url_to_db_and_get_short_url(long_url):
	auto_increment_value = dynamodb_crud_operations.get_latest_auto_incremented_value()
	new_auto_increment_value = auto_increment_value +1
	hash_value = hash_encode_and_decode.encode(new_auto_increment_value)
	dynamodb_crud_operations.update_both_URLs_to_dynamodb(long_url,hash_value,new_auto_increment_value)
	return hash_value

	
def get_long_url_from_hash_value(hash_value):
	auto_increment_value = hash_encode_and_decode.decode(hash_value)
	return dynamodb_crud_operations.get_long_url_from_auto_increment_value(str(auto_increment_value))