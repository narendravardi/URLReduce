import boto3
from boto3.dynamodb.conditions import Key, Attr
import credentials

dynamodb = boto3.resource(
	'dynamodb',
		aws_access_key_id = credentials.aws_access_key_id,
			aws_secret_access_key = credentials.aws_secret_access_key,region_name = credentials.region_name)

table = dynamodb.Table('URLReduce')
DYNAMODB_CONSTANT_HASH_KEY = 'DO_NOT_CHANGE_ME'
#CAREFUL!!!

def get_latest_auto_incremented_value():
	global table;
	response = table.query(
		KeyConditionExpression=Key('static_value').eq('DO_NOT_CHANGE_ME'),
			ScanIndexForward=False,
				Limit=1)
	# response returns list of items. 
	# only one elements is there due to Limit, used direct index '0'
	# retrieve auto_increment from the selected limit
	return int(response[u'Items'][0][u'auto_increment'])

#CAREFUL!!!
#In this function, short_url refers to hash_value
def update_both_URLs_to_dynamodb(long_url,short_url,auto_increment_value):
	global table
	table.put_item(
	Item = {
		'static_value':DYNAMODB_CONSTANT_HASH_KEY,
		'auto_increment':str(auto_increment_value),
		'long_url':long_url,
		'short_url':short_url
	}
)

def get_long_url_from_auto_increment_value(auto_increment_value):
	global table
	response = table.query(
		KeyConditionExpression=Key('static_value').eq(DYNAMODB_CONSTANT_HASH_KEY) & Key('auto_increment').eq(auto_increment_value)
	)
	if len(response[u'Items']) != 0:
		return response[u'Items'][0][u'long_url']
	return None