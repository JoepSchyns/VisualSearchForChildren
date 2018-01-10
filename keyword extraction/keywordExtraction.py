from rake_nltk_master.rake_nltk import Rake
import json
import demjson
import os.path

inputFileName = input("json with text(..\\scrapy\\toystores\\toys - Copy.json): ") or "..\\scrapy\\toystores\\toys - Copy.json"
textItem = input("item(description): ") or "description"
outputFileName = input("Output file(output.json): ") or "output.json"
language = input("language(dutch): ") or "dutch"
r = Rake(language=language)


rankedPhrases = []

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, inputFileName)
with open(path, encoding='utf-8') as json_data:
    doc = json.load(json_data)
    for item in doc:
    	text = item[textItem][0]
    	name  = item["name"]
    	r.extract_keywords_from_text(text)
    	itemRankedPhrases = r.get_ranked_phrases_with_scores()[0]
    	itemResult = {"name":name,"rankedPhrases":itemRankedPhrases}
    	rankedPhrases.append(itemResult)

path = os.path.join(my_path, outputFileName)
with open(path, "w") as outputFile:
	outputFile.write(json.dumps(rankedPhrases))


 # To get keyword phrases ranked highest to lowest.