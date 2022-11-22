# URLReduce
[URLReduce](https://url-reduce.herokuapp.com) is an attempt to learn how to use Flask with AWS DynamoDB. I am new to Flask and wanted to build an application instead of reading about it. This is a simpliest version with even more simple UI. 

## Installation
* Create an `IAM User` dedicated for this project, which will be able to access `dynamodb` data.
* Create a table in a region and update the `region_name` variable in `credentials.py` file
* Schema that works for this project is 
	* Hash Key - `SOME_CONSTANT_VALUE`
	* Sort Key - `Random Number` which we will use, in order to create `short_url` 
The packages used for the development of the project are specified in `requirements.txt` file. Install them locally or globally depending on the your usage and run `app.py`. Change `aws_access_key_id,aws_secret_access_key,region_name` fields in `credentials.py`. 

## Usage
I have deployed that code in `heroku`. You can use this software using https://url-reduce.herokuapp.com/home

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License
Copyright (c) 2016 Narendra Vardi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
